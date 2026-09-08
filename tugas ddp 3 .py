batas_nilai = (65, 100)
nilai_masuk = []
lulus = []
remedi = []

print("Pak Bruce Tolong Input Nilai nya Mas")

while True:
    masukan = input("Masukkan nilai: ")

    if masukan == "selesai":
        if len(nilai_masuk) < 5:
            print("Nilai masih kurang dari 5, tambah lagi")
            continue
        if len(lulus) == 0:
            print("Belum ada nilai lulus, tambah dulu")
            continue
        if len(remedi) == 0:
            print("Belum ada nilai remedi, tambah dulu")
            continue
        break

    elif masukan == "hapus":
        print("Nilai yang sudah ada:", nilai_masuk)
        hapus = input("Nilai berapa yang mau dihapus? ")
        hapus = float(hapus)

        if hapus in nilai_masuk:
            nilai_masuk.remove(hapus)
            if hapus in lulus:
                lulus.remove(hapus)
            if hapus in remedi:
                remedi.remove(hapus)
            print("sudah dihapus")
        

    else:
        nilai = float(masukan)

        if nilai < 0 or nilai > batas_nilai[1]:
            print("Nilai tidak boleh lebih dari 100 atau kurang dari 0")
        else:
            nilai_masuk.append(nilai)
            if nilai >= batas_nilai[0]:
                lulus.append(nilai)
                print("lulus")
            else:
                remedi.append(nilai)
                print("remidi")

print("Semua nilai :", nilai_masuk)
print("Nilai lulus :", lulus)
print("Nilai remedi:", remedi)