# spamphising

---

# 💬 Telegram Dummy Data Sender

Script ini digunakan untuk **mengirim data dummy (simulasi BRImo)** ke bot Telegram. Data yang dikirim mencakup nama nasabah, nomor HP, saldo acak, dan OTP acak. Cocok digunakan untuk **pengujian bot Telegram, simulasi load, atau keperluan edukasi.**

⚠️ **PERINGATAN**: Script ini hanya untuk keperluan **testing dan edukasi**. Penyalahgunaan untuk tujuan phishing atau penipuan adalah tindakan ilegal dan dilarang.

---

## 🧾 Fitur

* Menghasilkan nama acak menggunakan library `names`
* Menghasilkan nomor HP, saldo, dan OTP palsu
* Mengirim dua pesan ke bot Telegram untuk setiap data dummy
* Bisa mengatur jumlah dummy data yang dikirim
* Terdapat delay agar tidak spamming terlalu cepat

---

## 📦 Instalasi

1. **Clone repositori ini:**

   ```bash
   git clone https://github.com/afzan354/spamphising.git
   cd spamphising
   ```

2. **Install dependensi:**
   Script ini memerlukan `requests` dan `names`.

   ```bash
   pip install requests names
   ```

---

## ⚙️ Konfigurasi

Edit bagian berikut di dalam file Python:

```python
BOT_TOKEN = "TOKEN_BOT_KAMU"
CHAT_ID = "CHAT_ID_KAMU"
```

* **BOT\_TOKEN**: Token dari [@BotFather](https://t.me/BotFather)
* **CHAT\_ID**: ID pengguna atau grup tempat data akan dikirim.

  * Kamu bisa pakai [@userinfobot](https://t.me/userinfobot) untuk mendapatkan `chat_id` kamu.

---

## ▶️ Cara Menjalankan

```bash
python spam.py
```

Contoh ketika dijalankan:

```
Masukkan jumlah dummy data yang ingin dikirim: 3

--- Kirim ke-1 ---
[+] Data terkirim:
( BRImo | Data )

- Nama Nasabah : Michael Stewart
- Nomor HP     : 08123456789
- Saldo        : Rp 15677288

[+] Data terkirim:
( BRImo | OTP )

- Code OTP : 739284
```

---

## 📄 Format Pesan ke Telegram

**Pesan 1 (Data BRImo)**:

```
( BRImo | Data )

- Nama Nasabah : John Doe
- Nomor HP     : 08123456789
- Saldo        : Rp 12345678
```

**Pesan 2 (OTP)**:

```
( BRImo | OTP )

- Code OTP : 987654
```

---

## 📌 Catatan

* Script ini menggunakan `time.sleep(1)` agar tidak dianggap spam oleh Telegram.
* Cocok untuk simulasi bot banking, training, atau load test.

---

## ⚠️ Disclaimer

Penggunaan script ini **hanya diperbolehkan untuk keperluan edukatif dan pengujian pribadi**. Jangan gunakan untuk aktivitas ilegal atau menyesatkan yang dapat melanggar hukum.

---

Kalau kamu mau, aku bisa bantu sekalian buatkan `requirements.txt` juga. Mau?
