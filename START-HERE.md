# START HERE (panduan pengisian; hapus file ini sebelum publish)

Satu repo, dua pintu masuk: **/web3** (Web3 Builder) dan **/sqa** (SQA Engineer), dengan studi kasus NILO bersama. Struktur QA-mu (01-planning … 05-reports) utuh di dalam `sqa/`.

Status jujur: tes sudah dijalankan hijau terhadap situs uji lokal (mock): 12 tes UI dan 18 tes API. Terhadap situs asli (SauceDemo, Restful-Booker) belum pernah dijalankan dari lingkungan pembuatnya. Isi halaman NILO yang bertanda `EXAMPLE` berasal dari draf percakapan dan **belum diverifikasi**.

## Aturan emas
Jangan tulis hasil tes, bug, metrik, atau klaim on-chain yang belum kamu jalankan atau buktikan. `TODO` dan `EXAMPLE` baru dihapus setelah kamu verifikasi sendiri.

## Jalur
| Jalur | Waktu | Hasil |
|---|---|---|
| **MVP 4 minggu** (mulai di sini) | ±6-8 jam/minggu | Halaman SQA berbukti + NILO + landing live di GitHub Pages |
| **Penuh 16 minggu** | ±6-8 jam/minggu | MVP + exploratory, AI experiment ≥20 tes, Web3 testing, video demo |

## Hari 1 (target: 1 jam, situs sudah live)
- [ ] Buat repo `<USERNAME>.github.io`, push isi folder ini
- [ ] Ganti `<USERNAME>` dan `<REPO>` di semua file: `grep -rn "USERNAME" .`
- [ ] Settings → Pages → Deploy from branch `main` / root
- [ ] Isi nama dan kontak di `index.html` dan `README.md`
- [ ] Buka situs; periksa di lebar ponsel

## Minggu 1: PLAN (SQA)
- [ ] Jelajahi SauceDemo dan Restful-Booker; isi `sqa/01-planning/00-product-summary.md`
- [ ] Verifikasi `sqa/01-planning/01-requirements.md` terhadap aplikasi asli
- [ ] Isi `02-test-plan.md` dan `03-risk-assessment.md`
- [ ] `cd sqa/web-ui-playwright && npm install && npm run test:mock` (cek lingkungan)

## Minggu 2: SPECIFY + manual
- [ ] 25-30 test case di `sqa/02-manual/test-cases.md` dan `.csv` (sinkron)
- [ ] Eksekusi manual, isi `execution-log.md`
- [ ] `python scripts/portfolio_status.py` tanpa error

## Minggu 3: BUILD
- [ ] `npm test` ke situs asli; perbaiki locator bila perlu; commit `package-lock.json`
- [ ] `cd sqa/api-testing && pytest` ke API asli; sesuaikan asersi dengan perilaku nyata
- [ ] Tes buatan AI wajib lolos `sqa/ai-testing/verification-gate.md`

## Minggu 4: TEST + NILO + publish
- [ ] Uji NILO milikmu sendiri secara manual; catat hasil nyata dengan tanggal dan bukti
- [ ] Ganti semua `EXAMPLE` di `projects/nilo.html` dan `web3/index.html` dengan observasi nyata atau hapus barisnya
- [ ] Laporkan bug nyata di `sqa/03-bug-reports/`
- [ ] Workflow Actions hijau; isi `sqa/05-reports/test-summary-report.md`
- [ ] Jalankan `PUBLISH-CHECKLIST.md`

## Jalur penuh (minggu 5-16)
- [ ] 2-3 sesi exploratory; AI experiment ≥20 tes; video demo 3-5 menit
- [ ] `sqa/web3-testing/` (Foundry lokal atau testnet saja)

## Ritual mingguan (±15 menit)
1. `python scripts/portfolio_status.py`
2. Isi `docs/thinking/weekly-review.md`
3. Tambah baris `docs/thinking/confidence-log.csv` untuk tiap penilaian yang dibantu AI (tebak dulu, verifikasi kemudian)
4. Catat keputusan yang mengubah cakupan di `decision-log.md`

## Perintah berguna
```bash
python scripts/portfolio_status.py            # konsistensi + traceability
python scripts/portfolio_status.py --strict   # gagal bila TODO/EXAMPLE/USERNAME masih ada
cd sqa/web-ui-playwright && npm run test:mock # self-test UI offline
npm run gate                                  # cek flaky: 5x ulang
python -m http.server 8000                    # lihat situs lokal di http://localhost:8000
```

## Commit pertama
```bash
git init && git add . && git commit -m "chore: scaffold portfolio"
git branch -M main
git remote add origin https://github.com/<USERNAME>/<USERNAME>.github.io.git
git push -u origin main
```
Konvensi: `docs:` · `test:` · `fix:` · `ci:` · `chore:` · `site:` (halaman web). Commit kecil dan rutin.
