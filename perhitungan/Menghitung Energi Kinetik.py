# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 10 Januari 2025
# Program Menghitung Energi Kinitik

def hitung_energi_kinetik():
    print("*"* 40)
    print("Program Menghitung Energi Kinetik")
    print("*"* 40)
    
    massa = float(input("Masukkan massa benda (dalam kilogram): "))
    kecepatan = float(input("Masukkan kecepatan benda (dalam meter per detik): "))
    
    energi_kinetik = 0.5 * massa * kecepatan**2
    
    print(f"Energi kinetik benda: {energi_kinetik:.2f} joule")

hitung_energi_kinetik()