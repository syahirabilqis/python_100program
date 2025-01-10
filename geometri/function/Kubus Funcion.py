# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  9 Januari 2025
# Program Kubus Function

print("*"*40)
print ('Program Kubus Function')
print("*"*40)

def kubus():
  s = int(input('sisi: '))
  luas_permukaan = 6 * s * s
  v = s * s * s
  print('Luas Permukaan =', luas_permukaan, "m2")
  print('Volume =', v, "m3")
kubus()