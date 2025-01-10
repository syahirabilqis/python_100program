# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 10 Januari 2025
# Program Menghitung Energi listrik

def hitung_energi_listrik():
    print("*" * 40)
    print("Program Menghitung Energi Listrik")
    print("*" * 40)
    
    daya = float(input("Masukkan daya listrik (dalam watt): "))
    waktu = float(input("Masukkan waktu penggunaan (dalam jam): "))
    
    energi = daya * waktu
    
    print(f"Energi listrik yang digunakan: {energi} watt-jam")
    print(f"Atau setara dengan: {energi / 1000} kWh (kilowatt-jam)")

hitung_energi_listrik()