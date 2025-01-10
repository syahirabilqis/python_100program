# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 9 Januari 2025
# Program Angka Double 1-9

print("*" * 40)
print("Angka Double 1-9")
print("*" * 40)

line_to_print = ''
for i in range (1, 10):
    for j in range (0, 9):
        line_to_print += str(i)
    print(line_to_print)
    line_to_print = ''