from apps.custom_console import *
from apps.data_transaksi import *
from apps.data_motor import *
from apps.tentang import *
from apps.header import *
from apps.warning import *

check_width()


def select_main_menu():
    menu = 0
    try:
        menu = int(input("- Pilih Menu   : "))

        if (menu == 1):
            clear()
            generate_data_trx()
        elif (menu == 2):
            clear()
            get_data_trx()
        elif (menu == 3):
            clear()
            get_data_motor()
        elif (menu == 4):
            clear()
            show_header()
            tentang()
        elif (menu == 0):
            clear()
            msg_keluar()
        else:
            msg_waring("Warning : Maaf Menu Tidak tersedia !")

        if (menu != 0):
            input("\nTekan enter untuk kembali... ")
            clear()
            main_menu()
    except:
        if (menu != 0):
            msg_waring("\n\nWarning : Maaf Menu yang anda input Tidak Ada !\n")
            msg_keluar()


def generate_data_trx():
    try:
        print("*" * 40)
        print("       Generate Data Transaksi   ")
        print("*" * 40)
        kode = generate_kode_trx()
        print(" - Kode Kredit                : " + kode + " (autogenerate)")
        print("Input Data Pelanggan")
        nik = input(" - NIK                        : ")
        nama_pel = input(" - Nama Pelanggan             : ")
        alamat_pel = input(" - Alamat                     : ")
        print("Input Data Kendaraan")
        get_data_motor()

        # inisialisai awal
        kode_mtr = ""
        list_detail_motor = []
        nama_mtr = ""
        harga_mtr = 0

        while True:
            kode_mtr = input(" - Kode Motor                : ")
            list_detail_motor = get_data_motor_by_kode(kode_mtr)
            # validasi untuk menggambil data motor
            if (len(list_detail_motor) == 0):
                msg_waring("Waring : Maaf Data Motor tidak diketahui !")
                continue
            else:
                nama_mtr = list_detail_motor[1]
                harga_mtr = list_detail_motor[2]
                print(" - Nama Motor                : " + nama_mtr)
                print(" - Harga Motor               : Rp. " +
                      "{:,.0f}".format(harga_mtr))
                break

        print("Input Data Kredit ")
        print("  Acuan Perhitungan : ")
        print("    1. Total Pembayaran Pertama")
        print("    2. Angsuran Perbulan")
        acuan_perhitungan = int(input(" - Pilih Acuan Perhitungan   : "))

        list_opsi_angsuran = []

        if (acuan_perhitungan == 1):
            print(
                " - Note                      : Minimal Pembayaran pertama 20% dari Harga Motor"
            )

            minimal_pembayaran_pertama = harga_mtr * 20 / 100
            print(
                "                               Minimal Pembayaran pertama Rp. "
                + "{:,.2f}".format(minimal_pembayaran_pertama))
            total_pebayaran_pertama = 0
            while True:
                total_pebayaran_pertama = float(
                    input(" - Total Pembayaran Pertama  : "))
                persentase_minimal_pembayaran = total_pebayaran_pertama / harga_mtr * 100

                # Validasi tambahan
                if persentase_minimal_pembayaran >= harga_mtr:
                    msg_waring(
                        "Waring : Maaf Minimal Pembayaran Pertama melebihi Harga Motor !"
                    )
                    continue

                if persentase_minimal_pembayaran >= 20:
                    break
                else:
                    msg_waring(
                        "Waring : Maaf Minimal Pembayaran Pertama Kurang dari 20% !"
                    )
                    continue
            print("Input Data Opsi Kredit ")
            print(
                " +--------------------------------------------------------------------+"
            )
            print(
                " | Opsi | Total Pembayaran       | Jangka Waktu  | Angsuran Perbulan  |"
            )
            print(
                " |      | Pertama                | (Bulan)       |                    |"
            )
            print(
                " +--------------------------------------------------------------------+"
            )

            for i in range(3):
                range_tahun = i + 1
                range_bulan = range_tahun * 12
                angsuran_perbulan = (harga_mtr -
                                     total_pebayaran_pertama) / range_bulan

                list_opsi_angsuran.append([
                    range_tahun, total_pebayaran_pertama, range_bulan,
                    angsuran_perbulan
                ])

                print(" |  " + str(range_tahun) + "   | Rp. " +
                      "{:,.0f}".format(total_pebayaran_pertama) +
                      (" " *
                       (18 -
                        len(str("{:,.0f}".format(total_pebayaran_pertama))))) +
                      " | " + str(range_bulan) + "            | Rp. " +
                      "{:,.0f}".format(angsuran_perbulan) +
                      (" " *
                       (14 - len(str("{:,.0f}".format(angsuran_perbulan))))) +
                      " |")
            print(
                " +--------------------------------------------------------------------+"
            )
            opsi_kredit = int(input(" - Opsi Kredit               : "))
        else:
            angsuran_perbulan = float(input(" - Angsuran Perbulan         : "))
            print(
                " +--------------------------------------------------------------------+"
            )
            print(
                " | Opsi | Angsuran Perbulan    | Jangka Waktu  | Total Pembayaran     |"
            )
            print(
                " |      |                      | (Bulan)       | Pertama              |"
            )
            print(
                " +--------------------------------------------------------------------+"
            )
            for i in range(3):
                range_tahun = i + 1
                range_bulan = range_tahun * 12
                total_pebayaran_pertama = harga_mtr - (angsuran_perbulan *
                                                       range_bulan)
                if (total_pebayaran_pertama > angsuran_perbulan):

                    list_opsi_angsuran.append([
                        range_tahun, total_pebayaran_pertama, range_bulan,
                        angsuran_perbulan
                    ])

                    print(" |  " + str(range_tahun) + "   | Rp. " +
                          "{:,.0f}".format(angsuran_perbulan) +
                          (" " *
                           (16 -
                            len(str("{:,.0f}".format(angsuran_perbulan))))) +
                          " | " + str(range_bulan) + "            | Rp. " +
                          "{:,.0f}".format(total_pebayaran_pertama) +
                          (" " *
                           (16 -
                            len(str("{:,.0f}".format(total_pebayaran_pertama)))
                            )) + " |")
            print(
                " +--------------------------------------------------------------------+"
            )
            opsi_kredit = int(input(" - Opsi Kredit               : "))

        print("Simpan Data Opsi Kredit ")
        while True:
            lanjut_proses = input(
                " - Apakah Anda Akan menyimpan data ini ? [y/n] : ")
            clear()
            if (lanjut_proses == "y"):
                index_opsi = opsi_kredit - 1
                jangka_waktu = list_opsi_angsuran[index_opsi][2]
                total_pembayaran_pertama = list_opsi_angsuran[index_opsi][1]
                angsuran_perbulan = list_opsi_angsuran[index_opsi][3]

                # save data
                save_data_trx(kode, nik, nama_pel, alamat_pel, kode_mtr,
                              nama_mtr, harga_mtr, jangka_waktu,
                              total_pembayaran_pertama, angsuran_perbulan)
                # print report
                generate_reporting_by_kode(kode)
                break
            elif (lanjut_proses == "n"):
                # back to Home
                main_menu()
                break
            else:
                msg_waring("Waring : Maaf Inputan Salah !")
                continue
    except:
        msg_waring("\nWarning : Maaf terjadi kesalahan saat memasukan input !")


def sim_kredit_motor():
    get_data_trx()


def inv_motor():
    get_data_motor()


def main_menu():
    show_header()

    print("+----------------------------------------------------------+")
    print("|  Menu  |  Menu Utama                                     |")
    print("+----------------------------------------------------------+")
    print("|    1   |  Generate Transaksi Kredit Motor Syariah        |")
    print("|    2   |  Data Transaksi Kredit Motor Syariah            |")
    print("|    3   |  Data Inventory Motor                           |")
    print("|    4   |  Tentang Aplikasi                               |")
    print("|    0   |  Keluar                                         |")
    print("+----------------------------------------------------------+")

    select_main_menu()


main_menu()