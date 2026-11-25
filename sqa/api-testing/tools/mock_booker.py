"""Local stand-in for the Restful-Booker API (stdlib only).

Encodes only behavior that the public API documents (ping 201, auth, CRUD, 403 without
token, 500 on invalid POST). It exists to self-test this framework offline.
A green run against it says nothing about the real service.

Usage: python tools/mock_booker.py [port]     (default 3001)
"""

import json
import secrets
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BOOKINGS: dict[int, dict] = {}
TOKENS: set[str] = set()
NEXT_ID = 1
REQUIRED = ("firstname", "lastname", "totalprice", "depositpaid", "bookingdates")


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):  # keep test output quiet
        pass

    def _send(self, code: int, body=None, raw: str | None = None):
        data = raw if raw is not None else (json.dumps(body) if body is not None else "")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data.encode())))
        self.end_headers()
        self.wfile.write(data.encode())

    def _json(self):
        length = int(self.headers.get("Content-Length") or 0)
        try:
            return json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            return None

    def _authorized(self) -> bool:
        cookie = self.headers.get("Cookie", "")
        return any(part.strip() == f"token={t}" for t in TOKENS for part in cookie.split(";"))

    def _booking_id(self):
        tail = self.path.split("?")[0].rsplit("/", 1)[-1]
        return int(tail) if tail.isdigit() else None

    def do_GET(self):
        path = self.path.split("?")[0]
        if path == "/ping":
            return self._send(201, raw="Created")
        if path == "/booking":
            items = [{"bookingid": i} for i, b in BOOKINGS.items() if self._match(b)]
            return self._send(200, items)
        if path.startswith("/booking/"):
            bid = self._booking_id()
            if bid in BOOKINGS:
                return self._send(200, BOOKINGS[bid])
            return self._send(404, raw="Not Found")
        self._send(404, raw="Not Found")

    def _match(self, booking: dict) -> bool:
        if "?" not in self.path:
            return True
        query = dict(p.split("=", 1) for p in self.path.split("?", 1)[1].split("&") if "=" in p)
        return all(
            str(booking.get(k)) == v for k, v in query.items() if k in ("firstname", "lastname")
        )

    def do_POST(self):
        global NEXT_ID
        path = self.path.split("?")[0]
        body = self._json()
        if path == "/auth":
            if body and body.get("username") == "admin" and body.get("password") == "password123":
                token = secrets.token_hex(8)
                TOKENS.add(token)
                return self._send(200, {"token": token})
            return self._send(200, {"reason": "Bad credentials"})
        if path == "/booking":
            if not body or any(k not in body for k in REQUIRED):
                return self._send(500, raw="Internal Server Error")
            bid, NEXT_ID = NEXT_ID, NEXT_ID + 1
            BOOKINGS[bid] = body
            return self._send(200, {"bookingid": bid, "booking": body})
        self._send(404, raw="Not Found")

    def do_PUT(self):
        self._modify(replace=True)

    def do_PATCH(self):
        self._modify(replace=False)

    def _modify(self, replace: bool):
        if not self._authorized():
            return self._send(403, raw="Forbidden")
        bid = self._booking_id()
        if bid not in BOOKINGS:
            return self._send(405, raw="Method Not Allowed")
        body = self._json() or {}
        BOOKINGS[bid] = body if replace else {**BOOKINGS[bid], **body}
        self._send(200, BOOKINGS[bid])

    def do_DELETE(self):
        if not self._authorized():
            return self._send(403, raw="Forbidden")
        bid = self._booking_id()
        if bid not in BOOKINGS:
            return self._send(405, raw="Method Not Allowed")
        del BOOKINGS[bid]
        self._send(201, raw="Created")


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 3001
    print(f"Mock Restful-Booker on http://localhost:{port}")
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
