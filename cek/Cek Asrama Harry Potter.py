# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 7 januari 2025
# Program Cek Asrama

print("*"*40)
print("Asrama Harry Potter")
print("*"*40)

import random
import time

def cek_asrama(nama):
    print("Mencocokan karaktermu dan Asramamu...")
    time.sleep(2)
    
    hasil = random.choice([
        "Gryffindor",
        "Hufflepuff",
        "Ravenclaw",
        "Slytherin",
    ])
    
    print(f"Hasil Asrama untuk {nama}: {hasil}")

nama_user = input("Masukkan nama Anda: ")
cek_asrama(nama_user)