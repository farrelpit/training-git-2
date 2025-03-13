import os
from dataclasses import dataclass

@dataclass
class Barang:
    nama : str
    harga : float
    jumlah : int

barang_list = []

def add_barang():
    while True:
        nama = input("Nama barang: ")
        harga = float(input("Harga barang: "))
        jumlah = int(input("Jumlah barang: "))

        barang_list.append(Barang(nama,harga,jumlah))
        Opsi = input("Lanjut?(Y/n): ")

        if Opsi == "n":
            break
    input("Tekan tombol enter untuk lanjut...")

def lihat_barang():
    if not barang_list:
        print("Error! Gudang sedang kosong!")
    else:
        print("List Barang")
        print("=============")
        for barang in barang_list:
            print(f"Nama: {barang.nama}, Harga: {barang.harga}, Jumlah: {barang.jumlah}")
        input("Tekan tombol enter untuk lanjut...")

while True:
    os.system("cls")
    print("\n=============")
    print("Storage Menu")
    print("=============")
    print("1. Tambah Barang")
    print("2. Lihat Barang")
    print("3. Exit Program")
    print("=============")

    user_select = int(input(">> "))

    if user_select == 1:
        add_barang()
    elif user_select == 2:
        lihat_barang()
    elif user_select == 3:
        print("Keluar dari program...")
        input("Tekan enter untuk lanjut")
        break
    else:
        print("Error! Pastikan input diantara range 1 - 3")







