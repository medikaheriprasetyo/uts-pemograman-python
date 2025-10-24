def hitung_ongkir(berat_kg, kota, asuransi=False):
    """Menghitung ongkir berdasarkan kota, berat, dan opsi asuransi."""
    tarif_dasar = {
        "Jakarta": 10000,
        "Bandung": 12000,
        "Surabaya": 15000
    }
    if kota not in tarif_dasar:
        return "Kota tidak terdaftar"
    
    total = tarif_dasar[kota] + 2000 * berat_kg
    if asuransi:
        total += 3000
    return total

# Contoh pemanggilan
print(hitung_ongkir(3, "Jakarta"))
print(hitung_ongkir(2, "Surabaya", asuransi=True))
