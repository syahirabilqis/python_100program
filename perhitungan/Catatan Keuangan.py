# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 12 Desember 2024
# Program Catatan Keuangan

print("*" * 40)
print("Catatan Keuangan")
print("*" * 40)

def tampilkan_menu():
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran")
    print("3. Lihat Saldo")
    print("4. Keluar")

def tambah_keuangan(jenis, jumlah):
    if jenis == "pemasukan":
        catatan_keuangan.append(jumlah)
    elif jenis == "pengeluaran":
        catatan_keuangan.append(-jumlah)

def hitung_saldo():
    return sum(catatan_keuangan)

catatan_keuangan = []
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        jumlah = float(input("Masukkan jumlah pemasukan: "))
        tambah_keuangan("pemasukan", jumlah)
        print("Pemasukan berhasil ditambahkan.")
    elif pilihan == "2":
        jumlah = float(input("Masukkan jumlah pengeluaran: "))
        tambah_keuangan("pengeluaran", jumlah)
        print("Pengeluaran berhasil ditambahkan.")
    elif pilihan == "3":
        saldo = hitung_saldo()
        print(f"Saldo Anda saat ini: Rp{saldo:.2f}")
    elif pilihan == "4":
        print("Terima kasih telah menggunakan Catatan Keuangan!")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")