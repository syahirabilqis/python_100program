# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  7 November 2024
# Program Bola Function

print("*"*40)
print("Program Bola Lambda")
print("*"*40)

def bola():
    r = float(input("Masukan Jari2: "))
    PHI = 3.14
    lp = lambda r : 4 * PHI * r
    kp = lambda r : 4/3 * PHI * r
    
    print("Luas Bola: ",lp (r), "cm2")
    print("Keliling Bola: ",kp (r), "m")
    
bola()
