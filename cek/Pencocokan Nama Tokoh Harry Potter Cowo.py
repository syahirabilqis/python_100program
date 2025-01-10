# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 7 januari 2025
# Program Pencocokan Tokoh harry Potter

print("*"*40)
print("Pencocokan Nama Tokoh Harry Potter (Cowo)")
print("*"*40)

import random
import time

def cek_cowo(nama):
    print("Mencocokan...")
    time.sleep(2)
    
    hasil = random.choice([
        "Harry Potter",
        "Ron Weasley",
        "Draco Malfoy",
        "Neville Longbottom",
        "Fred Weasley",
        "George Weasley",
        "Albus Dumbledore",
        "Severus Snape",
        "Rubeus Hagrid",
        "Sirius Black",
        "Remus Lupin",
        "James Potter",
        "Cedric Diggory",
        "Tom Riddle",
        "Lucius Malfoy",
    ])
    
    print(f"Hasil Pencocokkan untuk {nama}: {hasil}")

nama_user = input("Masukkan nama Anda: ")
cek_cowo(nama_user)