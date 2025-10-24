s1 = input("Masukkan setoran 1: ")
s2 = input("Masukkan setoran 2: ")
s3 = input("Masukkan setoran 3: ")

if s1.isdigit() and s2.isdigit() and s3.isdigit():
    s1 = int(s1)
    s2 = int(s2)
    s3 = int(s3)
    if s1 <= 0 or s2 <= 0 or s3 <= 0:
        print("Input tidak valid")
    else:
        total = s1 + s2 + s3
        print("Total setoran:", total)
        if total < 300000:
            print("Kategori: Rendah")
        elif total < 600000:
            print("Kategori: Sedang")
        else:
            print("Kategori: Tinggi")
else:
    print("Input harus berupa angka!")
