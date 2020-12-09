import os

from os import system, name
from time import sleep


def msg_keluar():

    print("************************************************************")
    print()
    print()
    print("        Terimakasih Telah Menggunakan Program Ini          ")
    print("        G-One Finance © Kelompok 1 UBSI - 19.1E.07          ")
    print()
    print()
    print("************************************************************")
    print()
    print()
    print()
    print()
    print("             Tunggu 5 detik untuk menutup...")
    sleep(5)
    clear()
    quit()


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def check_width():
    cmd = ''' 
    mode con: cols=220 lines=50
    '''
    os.system(cmd)
