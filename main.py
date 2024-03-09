'''Latihan Fungsi'''

import os

# program menghitung luas dan keliling persegi panjang

# membuat header program
# os.system("cls") # windows
# # os.system("clear") Linux dll
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # mengambil input user
# LEBAR = int(input("Masukkan Nilai lebar : "))
# PANJANG = int(input("Masukkan Nilai panjang : "))

# # Program menghitung luas
# LUAS = PANJANG*LEBAR
# KELILING =  2*(PANJANG+LEBAR)

# # tampilkan hasil
# print(f"Hasil perhitungan luas = {LUAS}")
# print(f"Hasil perhitungan = {KELILING}")

def header():
    '''fungsi Header'''
    os.system("cls") # windows
    # os.system("clear") Linux dll
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")
    
def input_user():
    '''fungsi input user'''
    # mengambil input user
    lebar = int(input("Masukkan Nilai lebar \t: "))
    panjang = int(input("Masukkan Nilai panjang \t: "))
    
    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''fungsi luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''fungsi keliling'''
    return 2*(panjang+lebar)

def display(message,value):
    '''fungsi display'''
    print(f"hasil perhitungan {message} = {value}")

# Program utama
while True:
    header()
    LEBAR,PANJANG = input_user()
    print(22*"=")
    opsi = input("1. Hitung Luas \n2. Hitung Keliling \n3. Hitung keduanya \npilih salah satu : ")
    print(22*"=")

    if opsi == '1':
        LUAS = hitung_luas(LEBAR,PANJANG)
        display("luas", LUAS)
    elif opsi == '2':
        KELILING = hitung_keliling(LEBAR,PANJANG)
        display("keliling", KELILING)
    elif opsi == '3':
        LUAS = hitung_luas(LEBAR,PANJANG)
        display("luas", LUAS)
        KELILING = hitung_keliling(LEBAR,PANJANG)
        display("keliling", KELILING)
    else:
        print("pilih opsi 1 - 3")

    print(f"{'-'*40:^40}")
    isContinue = input("\nMau lagi? (y/n) ")
    if isContinue == "n":
        break

print(f"\n{"~~~~ Program selesai, terima kasih ~~~~":^40}\n")