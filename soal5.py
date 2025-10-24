import os, csv, json, logging

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# 1) Membuat folder data
os.makedirs("data", exist_ok=True)

# 2) Menulis CSV
data_presensi = [
    ["nim", "nama", "hadir_uts"],
    ["231001", "Andi", 1],
    ["231002", "Budi", 0],
    ["231003", "Citra", 1]
]

try:
    logging.info("Menulis file CSV...")
    with open("data/presensi.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data_presensi)
    logging.info("File CSV berhasil ditulis.")

    # 3) Membaca kembali dan hitung ringkasan
    hadir = 0
    total = 0
    with open("data/presensi.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += 1
            if row["hadir_uts"] == "1":
                hadir += 1

    persentase = (hadir / total) * 100
    ringkasan = {
        "total_data": total,
        "hadir": hadir,
        "persentase": f"{persentase:.2f}%"
    }

    # 4) Simpan ke JSON
    with open("data/ringkasan.json", "w") as f:
        json.dump(ringkasan, f, indent=4)
    logging.info("Ringkasan JSON berhasil dibuat.")

except Exception as e:
    logging.error(f"Gagal memproses file: {e}")
