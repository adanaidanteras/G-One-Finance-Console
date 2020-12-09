list_motors = [["MT001", "Yamaha Gear 125       ", 16750000],
               ["MT002", "Yamaha Nmax           ", 33750000],
               ["MT003", "Suzuki NEX Crossover  ", 17990000],
               ["MT004", "Vespa Bugang          ", 18500000],
               ["MT005", "Honda Scoopy          ", 19950000],
               ["MT006", "Yamaha Aerox VVA      ", 25500000],
               ["MT007", "Honda Vario 125       ", 20600000],
               ["MT008", "Honda PCX             ", 32840000],
               ["MT009", "Honda Beat Street     ", 17150000],
               ["MT010", "Yamaha R15            ", 36080000],
               ["MT011", "Honda ADV 150         ", 34740000],
               ["MT012", "Honda CRF150L         ", 34450000]]


def get_data_motor():

    print(" +----------------------------------------------------+")
    print(" | Kode  | Nama Motor              | Harga            |")
    print(" +----------------------------------------------------+")

    for i in range(len(list_motors)):
        kode = list_motors[i][0]
        nama = list_motors[i][1]
        # field nama motor 23 char
        nama += (" " * (23 - len(nama)))
        harga = list_motors[i][2]
        # field harga motor 12 char
        print(" | " + kode + " | " + nama + " | Rp. " +
              "{:,.0f}".format(harga) +
              (" " * (12 - len("{:,.0f}".format(float(harga))))) + " |")
    print(" +----------------------------------------------------+")
    print()


def get_data_motor_by_kode(key_kode):
    list_finded = []
    for i in range(len(list_motors)):
        kode = list_motors[i][0]
        if (key_kode == kode):
            list_finded = list_motors[i]
    return list_finded
