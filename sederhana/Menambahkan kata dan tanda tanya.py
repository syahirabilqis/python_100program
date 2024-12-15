# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 12 Desember 2024
# Program Menambahkan kata dan tanda tanya

print("*" * 40)
print("Menambahkan kata dan tanda tanya")
print("*" * 40)

def ubah_kalimat(kalimat):
    if not kalimat.lower().startswith("apakah"):
        kalimat = "Apakah " + kalimat
    
    if not kalimat.endswith("?"):
        kalimat = kalimat.rstrip(".!?") + "?"
    
    return kalimat

kalimat_input = input("Masukkan kalimat: ")
kalimat_output = ubah_kalimat(kalimat_input)

print("Output:", kalimat_output)