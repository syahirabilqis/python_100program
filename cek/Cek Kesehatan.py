# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 7 januari 2025
# Program Cek Kesehatan

print("*"*40)
print("Program Cek Kesehatan")
print("*"*40)

import random

def cek_kesehatan():
    responses = [
        "Kesehatanmu dalam kondisi baik, tetap jaga pola hidup sehat!",
        "Ada sedikit kelelahan, istirahatlah lebih banyak.",
        "Periksa kondisi tubuhmu lebih sering untuk menjaga kesehatan.",
        "Kesehatanmu stabil, tapi tetap waspada dengan cuaca."
    ]
    return random.choice(responses)

def main():
    print("Selamat datang di program cek kesehatan!")
    while True:
        print("\nPilih cek yang ingin dilakukan:")
        print("1. Cek Kesehatan")
        print("2. Keluar")
        
        choice = input("Masukkan pilihan (1/2): ")

        if choice == '1':
            print(cek_kesehatan())
        elif choice == '2':
            print("Terima kasih telah menggunakan program ini. Semoga sehat selalu!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()