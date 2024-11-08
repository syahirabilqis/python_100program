# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  8 November 2024
# Program Cek Khodam

print("*"*40)
print("Program Cek Khodam")
print("*"*40)

import random
import time

def cek_khodam(nama):
    print("Mengecek keberadaan khodam...")
    time.sleep(2)  
    
    hasil = random.choice([
        "Anda memiliki khodam penjaga!", 
        "Tidak terdeteksi adanya khodam.", 
        "Khodam pendamping Anda adalah sosok berjubah hitam.", 
        "Khodam Anda memiliki energi yang sangat kuat!", 
        "Energi spiritual Anda bersih, tanpa adanya khodam."
        "Kursi Goyang"
    ])
    
    print(f"Hasil untuk {nama}: {hasil}")

nama_user = input("Masukkan nama Anda: ")
cek_khodam(nama_user)

# time.sleep untuk Memberikan efek seolah-olah sedang memproses
# random.choice untuk memilih satu elemen secara acak dari sebuah list