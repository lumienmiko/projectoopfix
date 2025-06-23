#Bagian ini dikerjakan oleh Maulana Mikola A dan Estu Setyoadi Galih Ramadani
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