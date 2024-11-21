# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  9 November 2024
# Program Konversi Suhu

print("*"*40)
print("Program Konversi Suhu")
print("*"*40)

#untuk Celsius ke Fahrenheit
def celsius_ke_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# untuk Fahrenheit ke Celsius
def fahrenheit_ke_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Pilih konversi suhu:")
print("1. Celsius ke Fahrenheit")
print("2. Fahrenheit ke Celsius")

pilihan = int(input("Masukkan pilihan (1/2): "))

if pilihan == 1:
    celsius = float(input("Masukkan suhu dalam Celsius: "))
    fahrenheit = celsius_ke_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit}°F")
elif pilihan == 2:
    fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
    celsius = fahrenheit_ke_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {celsius}°C")
else:
    print("Pilihan tidak valid!")
