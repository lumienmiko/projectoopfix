#Kelompok13
from abc import ABC, abstractmethod

# Interface produksi
class ProduksiInterface(ABC):
    @abstractmethod
    def pengadonan(self): pass

    @abstractmethod
    def pengembangan(self): pass

    @abstractmethod
    def pemanggangan(self): pass

    @abstractmethod
    def topping(self): pass

# Abstract superclass
class ProdukRoti(ProduksiInterface):
    def __init__(self, nama, kode, bahan_baku, biaya, harga):
        self.nama_produk = nama
        self.kode_produk = kode
        self.bahan_baku = bahan_baku  # dict: {'tepung': '200g', 'gula': '50g'}
        self.biaya_produksi = biaya
        self.harga_jual = harga

    def calculate_profit(self, jumlah):
        total_biaya = self.biaya_produksi * jumlah
        total_penjualan = self.harga_jual * jumlah
        return total_penjualan - total_biaya

    @abstractmethod
    def simulate_production(self): pass

# Subclass: Roti Manis
class RotiManis(ProdukRoti):
    def pengadonan(self):
        print("Roti Manis - Pengadonan")

    def pengembangan(self):
        print("Roti Manis - Pengembangan")

    def pemanggangan(self):
        print("Roti Manis - Pemanggangan")

    def topping(self):
        print("Roti Manis - Tidak pakai topping")

    def simulate_production(self):
        self.pengadonan()
        self.pengembangan()
        self.pemanggangan()
        self.topping()

# Subclass: Croissant
class Croissant(ProdukRoti):
    def pengadonan(self):
        print("Croissant - Pengadonan")

    def pengembangan(self):
        print("Croissant - Pengembangan")

    def pemanggangan(self):
        print("Croissant - Pemanggangan")

    def topping(self):
        print("Croissant - Tidak pakai topping")

    def simulate_production(self):
        self.pengadonan()
        self.pengembangan()
        self.pemanggangan()
        self.topping()

# Subclass: Butter Cookies
class ButterCookies(ProdukRoti):
    def pengadonan(self):
        print("Butter Cookies - Pengadonan")

    def pengembangan(self):
        pass 

    def pemanggangan(self):
        print("Butter Cookies - Pemanggangan")

    def topping(self):
        print("Butter Cookies - Topping taburan gula")

    def simulate_production(self):
        self.pengadonan()
        self.pemanggangan()
        self.topping()

# Subclass: Muffin
class Muffin(ProdukRoti):
    def pengadonan(self):
        print("Muffin - Pengadonan")

    def pengembangan(self):
        print("Muffin - Pengembangan")

    def pemanggangan(self):
        print("Muffin - Pemanggangan")

    def topping(self):
        print("Muffin - Topping choco chips")

    def simulate_production(self):
        self.pengadonan()
        self.pengembangan()
        self.pemanggangan()
        self.topping()

# List penyimpanan produk
produk_list = []

def tambah_produk():
    print("\nPilih jenis produk:")
    print("1. Roti Manis\n2. Croissant\n3. Butter Cookies\n4. Muffin")
    pilihan = input("Pilihan: ")
    nama = input("Nama Produk: ")
    kode = input("Kode Produk: ")
    bahan_baku = {}
    while True:
        bahan = input("Masukkan nama bahan (atau 'done' untuk selesai): ")
        if bahan.lower() == 'done': break
        jumlah = input(f"Jumlah {bahan}: ")
        bahan_baku[bahan] = jumlah
    biaya = int(input("Biaya produksi per pcs: "))
    harga = int(input("Harga jual per pcs: "))

    if pilihan == '1':
        produk = RotiManis(nama, kode, bahan_baku, biaya, harga)
    elif pilihan == '2':
        produk = Croissant(nama, kode, bahan_baku, biaya, harga)
    elif pilihan == '3':
        produk = ButterCookies(nama, kode, bahan_baku, biaya, harga)
    elif pilihan == '4':
        produk = Muffin(nama, kode, bahan_baku, biaya, harga)
    else:
        print("Pilihan tidak valid.")
        return

    produk_list.append(produk)
    print("Produk berhasil ditambahkan!\n")

def tampilkan_produk():
    if not produk_list:
        print("Belum ada produk.")
        return
    for p in produk_list:
        print(f"\nNama: {p.nama_produk}\nKode: {p.kode_produk}\nHarga: {p.harga_jual}\nBiaya: {p.biaya_produksi}")
        print("Bahan:")
        for b, j in p.bahan_baku.items():
            print(f"  - {b}: {j}")

def kalkulasi_profit():
    if not produk_list:
        print("Belum ada produk.")
        return
    for idx, p in enumerate(produk_list):
        print(f"{idx+1}. {p.nama_produk}")
    idx = int(input("Pilih produk: ")) - 1
    jumlah = int(input("Jumlah pcs: "))
    profit = produk_list[idx].calculate_profit(jumlah)
    print(f"Estimasi profit: Rp {profit}\n")

def simulasi():
    if not produk_list:
        print("Belum ada produk.")
        return
    for idx, p in enumerate(produk_list):
        print(f"{idx+1}. {p.nama_produk}")
    idx = int(input("Pilih produk: ")) - 1
    produk_list[idx].simulate_production()

# Main loop
if __name__ == "__main__":
    while True:
        print("\n==== SISTEM PRODUKSI HANARI BAKERY ====")
        print("1. Tambah Produk Baru")
        print("2. Tampilkan Semua Produk")
        print("3. Kalkulator Estimasi Profit")
        print("4. Simulasi Proses Produksi")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tambah_produk()
        elif pilihan == '2':
            tampilkan_produk()
        elif pilihan == '3':
            kalkulasi_profit()
        elif pilihan == '4':
            simulasi()
        elif pilihan == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")
