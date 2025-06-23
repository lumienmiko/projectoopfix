#Bagian ini dikerjakan oleh Hammam Dhiyaulhaq
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