# Publish checklist (gate terakhir sebelum repo publik)

- [ ] `python scripts/portfolio_status.py --strict` lulus (tidak ada TODO/EXAMPLE/<USERNAME>)
- [ ] Tidak ada rahasia: cari `.env`, token, kunci; hanya `.env.example` yang ter-commit
- [ ] Tidak ada materi NDA (nama produk, tangkapan layar, detail bug dari crowdtesting)
- [ ] Semua angka di README berasal dari run nyata dan tanggalnya jelas
- [ ] Bug yang dipublikasikan sudah dilaporkan ke pemilik dan diberi kesempatan memperbaiki
- [ ] Workflow Actions hijau; badge menunjuk ke repo yang benar
- [ ] `package-lock.json` ter-commit
- [ ] Setiap klaim di `index.html`, `web3/`, `sqa/index.html`, `projects/nilo.html` punya tautan bukti; tidak ada klaim on-chain tanpa alamat testnet
- [ ] Semua tautan di halaman web bekerja (klik satu per satu) dan halaman tidak overflow di lebar 390 px
- [ ] Settings → Pages aktif dan situs terbuka
- [ ] `START-HERE.md` dan file ini sudah dihapus
- [ ] Video demo (jika ada) tidak menampilkan data pribadi
- [ ] Baca ulang README sebagai perekrut yang punya 2 menit
