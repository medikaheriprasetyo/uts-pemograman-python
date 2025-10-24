def jadwal_hari(hari):
    jadwal = {
        "Senin": ["Matematika", "Algoritma"],
        "Selasa": ["Basis Data", "Bahasa Inggris"],
        "Rabu": ["Pemrograman Visual", "Statistika"]
    }

    if hari in jadwal:
        return jadwal[hari]
    else:
        return ["Tidak ada jadwal"]


print(jadwal_hari("Selasa"))
print(jadwal_hari("sabtu"))
