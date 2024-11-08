# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  8 November 2024
# Program Limas Segitiga Function

print("*"*40)
print("Program Limas Segitiga Function")
print("*"*40)

def LimasSegitiga():
    a = float(input("Masukan Luas alas Segitiga: "))
    s = float(input("Masukan Luas Sisi Tegak:  "))
    t = float (input("Masukan Tinggi limas: "))
    
    v = lambda a,s,t : (1/3) * a * t
    lp = lambda a,s,t: a + s
    la = lambda a,s,t : 1/2 * a * t
    
    print("Volume Limas Segitiga: ",v (a,s,t),"vol")
    print("Luas Permukaan Limas Segitiga: ",lp (a,s,t),"m2")
    print("Luas Alas Segitiga: ",la (a,s,t),"m2")

LimasSegitiga()