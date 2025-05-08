import requests
import random
import time
import names

# ========== SETUP BOT TELEGRAM ==========
BOT_TOKEN = "8199495447:AAEnyreset839g940vQ0nnNhAeJ_H-aaWsnw"
CHAT_ID = "163544reset8"
SEND_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


# ========== GENERATOR DUMMY DATA ==========

def generate_nama():
    return names.get_full_name()

def generate_nohp():
    return "08" + "".join([str(random.randint(0,9)) for _ in range(9)])

def generate_saldo():
    return str(random.randint(100000, 99999999))

def generate_otp():
    return str(random.randint(100000, 999999))


# ========== KIRIM SIMULASI DATA KE BOT ==========

def kirim_data_dummy():
    nama = generate_nama()
    nohp = generate_nohp()
    saldo = generate_saldo()
    otp = generate_otp()

    # Simulasi data dari `data.html`
    pesan_data = (
        f"( BRImo | Data )\n\n"
        f"- Nama Nasabah : {nama}\n"
        f"- Nomor HP     : {nohp}\n"
        f"- Saldo        : Rp {saldo}"
    )

    # Simulasi data dari `ver.html`
    pesan_otp = (
        f"( BRImo | OTP )\n\n"
        f"- Code OTP : {otp}"
    )

    for pesan in [pesan_data, pesan_otp]:
        response = requests.post(SEND_URL, data={
            "chat_id": CHAT_ID,
            "text": pesan,
            "parse_mode": "html"
        })

        if response.status_code == 200:
            print(f"[+] Data terkirim:\n{pesan}\n")
        else:
            print(f"[-] Gagal kirim. Status code: {response.status_code}\n")

        time.sleep(1)  # Biar nggak terlalu cepat spamming


# ========== MAIN PROGRAM ==========
if __name__ == "__main__":
    jumlah = int(input("Masukkan jumlah dummy data yang ingin dikirim: "))
    for i in range(jumlah):
        print(f"\n--- Kirim ke-{i+1} ---")
        kirim_data_dummy()
