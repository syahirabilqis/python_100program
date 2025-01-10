# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 7 januari 2025
# Program Pencocokan Tokoh harry Potter Cewe

print("*"*40)
print("Pencocokan Nama Tokoh Harry Potter (Cewe)")
print("*"*40)

import random
import time

def cek_cewe(nama):
    print("Mencocokan...")
    time.sleep(2)
    
    hasil = random.choice([
        "Hermione Granger",
        "Ginny Weasley",
        "Luna Lovegood",
        "Cho Chang",
        "Molly Weasley",
        "Bellatrix Lestrange",
        "Nymphadora Tonks",
        "Minerva McGonagall",
        "Lily Potter",
        "Fleur Delacour",
        "Narcissa Malfoy",
        "Pansy Parkinson",
        "Helena Ravenclaw",
        "Petunia Dursley",
        "Rita Skeeter",
    ])
    
    print(f"Hasil Pencocokkan untuk {nama}: {hasil}")

nama_user = input("Masukkan nama Anda: ")
cek_cewe(nama_user)