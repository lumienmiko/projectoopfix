#Bagian ini dikerjakan oleh Jinan Ramadhan Atallah
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