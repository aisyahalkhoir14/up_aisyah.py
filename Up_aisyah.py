
# APLIKASI PEMBAYARAN PARKIR KENDARAAN

ulang = "y"

while ulang == "y":

    # Judul program
    print("===== APLIKASI PEMBAYARAN PARKIR =====")

    # Input jumlah kendaraan
    jumlah_kendaraan = int(input("Masukkan jumlah kendaraan: "))

    total_semua = 0

    # Perulangan kendaraan
    for i in range(jumlah_kendaraan):

        print("\nKendaraan ke-", i + 1)

        # Input data kendaraan
        jenis = input("Jenis kendaraan (motor/mobil/bus): ").lower()
        lama = int(input("Lama parkir (jam): "))

        # Menentukan tarif parkir
        if jenis == "motor":
            tarif = 2000
        elif jenis == "mobil":
            tarif = 5000
        elif jenis == "bus":
            tarif = 10000
        else:
            print("Jenis kendaraan tidak tersedia!")
            continue

        # Menghitung biaya parkir
        biaya = tarif * lama

        # Menghitung biaya tambahan
        if lama > 5:
            biaya_tambahan = 5000
        else:
            biaya_tambahan = 0

        # Menghitung total pembayaran
        total_bayar = biaya + biaya_tambahan

        # Menjumlahkan seluruh pembayaran
        total_semua = total_semua + total_bayar

        # Menampilkan struk pembayaran
        print("\n===== STRUK PARKIR =====")
        print("Jenis kendaraan  :", jenis)
        print("Lama parkir      :", lama, "jam")
        print("Tarif per jam    : Rp", tarif)
        print("Biaya parkir     : Rp", biaya)
        print("Biaya tambahan   : Rp", biaya_tambahan)
        print("Total pembayaran : Rp", total_bayar)

    # Menampilkan total seluruh pembayaran
    print("\n================================")
    print("TOTAL SELURUH PEMBAYARAN: Rp", total_semua)
    print("================================")

    # Pilihan mengulang program
    ulang = input("\nIngin menghitung lagi? (y/t): ").lower()

print("\nAnda Keluar")
print("Terima kasih telah menggunakan aplikasi parkir!")
