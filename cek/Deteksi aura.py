# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  8 November 2024
# Program Deteksi Aura

print("*"*40)
print("Program Deteksi Aura")
print("*"*40)

import random

def deteksi_aura(nama):
    warna_aura = random.choice([
        "Merah (Berani dan penuh semangat)", 
        "Biru (Tenang dan penuh kedamaian)", 
        "Hijau (Penyembuh dan penuh kasih sayang)", 
        "Kuning (Kreatif dan cerdas)", 
        "Ungu (Spiritual dan intuitif)"
    ])
    
    print(f"Aura Anda, {nama}, adalah {warna_aura}.")

nama_user = input("Masukkan nama Anda: ")
deteksi_aura(nama_user)