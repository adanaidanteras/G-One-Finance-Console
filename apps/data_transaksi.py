list_trx = [
]  # [["KR0001","XXX","ADSDD","MT001", "MX KINGDDF",19000000, 12,1000000,200000]]


def get_data_trx():
    print('''
 +-----------------------------------------------------------------------------------------------------------------------------------------------------------+
 | Kode   | NIK              | Nama                    | Kode  | Nama Motor              | Harga Motor    | Jangka Waktu | Total Pembayaran | Angsuran       |
 | Kredit | Pelanggan        | Pelanggan               | Motor |                         |                | (Bulan)      | Pertama          | Perbulan       |
 +-----------------------------------------------------------------------------------------------------------------------------------------------------------+'''
          )

    if (len(list_trx) == 0):
        print(
            " |                                                                Data Kosong                                                                                |"
        )

    for i in range(len(list_trx)):

        kode_kredit = list_trx[i][0]

        nik = list_trx[i][1]
        nik += (" " * (16 - len(nik)))  # field length 16 char

        nama_pelanggan = list_trx[i][2]
        nama_pelanggan += (" " * (23 - len(nama_pelanggan))
                           )  # field length 23 char

        kode_motor = list_trx[i][4]

        nama_motor = list_trx[i][5]

        nama_motor += (" " * (23 - len(nama_motor)))  # field length 23 char

        harga_motor = list_trx[i][6]
        # field harga motor 12 char
        ket_harga_motor = "Rp. " + "{:,.0f}".format(harga_motor) + (
            " " * (14 - len("Rp. " + "{:,.0f}".format(harga_motor))))

        jangka_waktu = list_trx[i][7]

        ket_jangka_waktu = str(jangka_waktu) + (
            " " * (12 - len(str(jangka_waktu))))  # field length 12 char

        total_pembayaran = list_trx[i][8]
        ket_total_pembayaran = "Rp. " + "{:,.0f}".format(total_pembayaran) + (
            " " * (16 - len("Rp. " + "{:,.0f}".format(total_pembayaran)))
        )  # field length 12 char

        angsuran_perbulan = list_trx[i][9]
        ket_angsuran_perbulan = "Rp. " + "{:,.0f}".format(
            angsuran_perbulan) + (
                " " * (14 - len("Rp. " + "{:,.0f}".format(angsuran_perbulan))))

        print(" | " + kode_kredit + " | " + nik + " | " + nama_pelanggan +
              " | " + kode_motor + " | " + nama_motor + " | " +
              ket_harga_motor + " | " + ket_jangka_waktu + " | " +
              ket_total_pembayaran + " | " + ket_angsuran_perbulan + " |")

    print(
        " +-----------------------------------------------------------------------------------------------------------------------------------------------------------+"
    )
    print()


def generate_kode_trx():
    last_number = "KR0001"

    if (len(list_trx) > 0):
        last_kode = list_trx[-1][0]
        last_number = str(int(last_kode[-4:6]) + 1)
        if (len(last_number) == 1):
            last_number = "KR000" + last_number
        elif (len(last_number) == 2):
            last_number = "KR00" + last_number
        elif (len(last_number) == 3):
            last_number = "KR0" + last_number
        else:
            last_number = "KR" + last_number
    return last_number


def save_data_trx(kode, nik, nama_pel, alamat_pel, kode_mtr, nama_mtr,
                  harga_mtr, jangka_waktu, total_pembayaran_pertama,
                  angsuran_perbulan):

    new_trx = [
        kode, nik, nama_pel, alamat_pel, kode_mtr, nama_mtr, harga_mtr,
        jangka_waktu, total_pembayaran_pertama, angsuran_perbulan
    ]
    list_trx.append(new_trx)


def generate_reporting_by_kode(key_kode):
    for i in range(len(list_trx)):
        kode = list_trx[i][0]
        if (key_kode == kode):
            nik = list_trx[i][1]
            nama_pel = list_trx[i][2]
            alamat_pel = list_trx[i][3]
            kode_mtr = list_trx[i][4]
            nama_mtr = list_trx[i][5]
            harga_mtr = list_trx[i][6]
            jangka_waktu = list_trx[i][7]
            total_pembayaran_pertama = list_trx[i][8]
            angsuran_perbulan = list_trx[i][9]
            print("*" * 40)
            print("        Berhasil Menyimpan   ")
            print("       Detail Data Transaksi   ")
            print("*" * 40)
            print(" - Kode Kredit              : " + kode)
            print("Data Pelanggan")
            print(" - No Idenstitas            : " + nik)
            print(" - Nama Lengkap             : " + nama_pel)
            print(" - Alamat                   : " + alamat_pel)
            print("Data Kendaraan")
            print(" - Kode Motor               : " + kode_mtr)
            print(" - Nama Motor               : " + nama_mtr)
            print(" - Harga Motor              : Rp. " +
                  "{:,.0f}".format(harga_mtr))
            print("Data Kredit  ")
            print(" - Angsuran Perbulan        : Rp. " +
                  "{:,.0f}".format(angsuran_perbulan))
            print(" - Jangka Waktu             : " + str(jangka_waktu) +
                  " Bulan")
            print(" - Total Pembayaran Pertama : Rp. " +
                  "{:,.0f}".format(total_pembayaran_pertama))
            print("*" * 40)
