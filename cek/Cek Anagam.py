# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 9 Januari 2025
# Program Cek Anagam

print("*"*40)
print("Program Cek Anagram")
print("*"*40)

kata1 = input("Masukkan kata pertama: ").lower()
kata2 = input("Masukkan kata kedua: ").lower()

def cek_anagram(kata1, kata2):
    return sorted(kata1) == sorted(kata2)

if cek_anagram(kata1, kata2):
    print(f"{kata1} dan {kata2} adalah anagram.")
else:
    print(f"{kata1} dan {kata2} bukan anagram.")