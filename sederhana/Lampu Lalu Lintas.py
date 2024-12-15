# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  8 November 2024
# Program Lampu Lalu Lintas

print("*"*40)
print("Program Lampu Lalu Lintas")
print("*"*40)

merah = 'Berhenti'
kuning = 'Bersiap-siap'
hijau = 'Maju'

warna = input('Masukan lampu lalu lintas: ')

if warna == 'merah':
    print('Kamu harus berhenti')
elif warna == 'kuning' :
    print('Ayo bersiap-siap')
elif warna == 'hijau':
    print('jalan!')
else :
    print('salah')