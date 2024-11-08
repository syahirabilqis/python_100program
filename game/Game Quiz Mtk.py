# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  8 November 2024
# Game Quiz Matematika

print("*"*40)
print("Game Quiz Matematika")
print("*"*40)

import random

def buat_soal():
    angka1 = random.randint(1, 10)
    angka2 = random.randint(1, 10)
    operasi = random.choice(['+', '-', '*'])

    if operasi == '+':
        jawaban = angka1 + angka2
    elif operasi == '-':
        jawaban = angka1 - angka2
    else: 
        jawaban = angka1 * angka2

    soal = f"{angka1} {operasi} {angka2}"
    return soal, jawaban

def main_kuis():
    print("=== Selamat datang di Kuis Matematika! ===")
    skor = 0
    jumlah_soal = 5

    for i in range(jumlah_soal):
        soal, jawaban_benar = buat_soal()
        print(f"Soal {i + 1}: {soal} = ?")
        
        jawaban_pemain = input("Jawaban Anda: ")

        if jawaban_pemain.isdigit():
            jawaban_pemain = int(jawaban_pemain)

            if jawaban_pemain == jawaban_benar:
                print("Benar!")
                skor += 1
            else:
                print(f"Salah! Jawaban yang benar adalah {jawaban_benar}")
        else:
            print("Masukkan angka yang benar.")


    print(f"Skor Anda: {skor} dari {jumlah_soal} soal.")
    if skor == jumlah_soal:
        print("Luar biasa! Semua jawaban benar!")
    elif skor >= 3:
        print("Bagus! Anda menjawab lebih dari setengahnya dengan benar.")
    else:
        print("Jangan menyerah, terus berlatih ya!")


main_kuis()