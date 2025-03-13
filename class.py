from dataclasses import dataclass

@dataclass
class Barang:
    nama : str
    harga : float
    jumlah : int

barang_list = []


while True:
    nama = input("Nama barang: ")
    harga = float(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))

    barang_list.append(Barang(nama,harga,jumlah))
    Opsi = input("Lanjut?(Y/n): ")

    if Opsi == "n":
        break

for barang in barang_list:
    print(f"Nama: {barang.nama}, Harga: {barang.harga}, Jumlah: {barang.jumlah}")



