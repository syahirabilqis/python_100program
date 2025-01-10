print("*" *40)
print("Program Game Pet Cermin")
print("*"*40)

import random

print("Selamat datang di Game Pet Cermin!")
print("Perintahmu akan terbalik seperti cermin. Misalnya, 'atas' akan menjadi 'bawah'!")
print("Tujuanmu adalah mengumpulkan 5 poin dengan mencapai lokasi target (T).")

size = 5
peta = [["-" for _ in range(size)] for _ in range(size)]

pet_x, pet_y = random.randint(0, size-1), random.randint(0, size-1)
target_x, target_y = random.randint(0, size-1), random.randint(0, size-1)

while (pet_x, pet_y) == (target_x, target_y):
    target_x, target_y = random.randint(0, size-1), random.randint(0, size-1)

poin = 0

def tampilkan_peta():
    for i in range(size):
        for j in range(size):
            if (i, j) == (pet_x, pet_y):
                print("P", end=" ") 
            elif (i, j) == (target_x, target_y):
                print("T", end=" ") 
            else:
                print("-", end=" ")
        print()

while poin < 5:
    tampilkan_peta()
    print(f"Poin saat ini: {poin}")
    print("Gunakan perintah: atas, bawah, kiri, kanan")
    perintah = input("Masukkan perintah: ").lower()

    if perintah == "bawah":
        pet_x = min(size-1, pet_x + 1)  #bawah
    elif perintah == "atas":
        pet_x = max(0, pet_x - 1)  #atas
    elif perintah == "kanan":
        pet_y = min(size-1, pet_y + 1) #kanan
    elif perintah == "kiri":
        pet_y = max(0, pet_y - 1)  #kiri
    else:
        print("Perintah tidak valid!")
        continue

    if (pet_x, pet_y) == (target_x, target_y):
        poin += 1
        print("Selamat! Kamu mencapai target dan mendapatkan 1 poin!")
        while (target_x, target_y) == (pet_x, pet_y):
            target_x, target_y = random.randint(0, size-1), random.randint(0, size-1)

print("Selamat! Kamu mengumpulkan 5 poin dan memenangkan permainan!")