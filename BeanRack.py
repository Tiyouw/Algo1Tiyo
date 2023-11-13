import pandas as pd
import json
import csv
import os 
import sys
import prettytable
import getpass

path = 'BeanRack\coffee_stock.csv'
file = pd.read_csv(path)
pathLogin = "BeanRack\database.json"

hijau = '\033[92m'
merah = '\033[91m'
end = '\033[0m'

#CLEAR TERMINAL
def clear():
    os.system("cls")

#KEMBALI KE MENU
def kembali():
    input('Tekan Enter untuk kembali ke Menu ')
    clear()
    main()

#MENU DISPLAY
def display_menu():
    print('''
        +============================+
        |                            |
        |    WELCOME TO BEAN-RACK    |
        |                            |
        +============================+ 
        1. Stok Kopi
        2. Tambah Stok
        3. Hapus Stok
        4. Ubah Stok\n
        0.Keluar
          ''')

#STOK KOPI DISPLAY
def display_stok_kopi():
    print('''
+=============================+
|                             |
|     STOK KOPI BEAN-RACK     |
|                             |
+=============================+ 
          ''')

#TABEL DARI CSV
def tabel():
    with open(path) as tabel:
      print(prettytable.from_csv(tabel))

#PILIHAN MENU
def pilihan():
    while True:
        pilihan = int(input("\tMasukkan pilihan menu anda (1/2/3/4/5/0) "))
        if pilihan == 1:
            stok_kopi()
        if pilihan == 2:
            tambah_stok()
        if pilihan == 3:
            hapus_stok()
        if pilihan == 4:
            ubah_stok()
        # if pilihan == 5:
        #     laporan() GAJADI
        if pilihan == 0:
            keluar()
        else:
            clear()
            print(merah+"\tPilihan tidak valid!"+end)
            main()
            continue

#PILIHAN 1 MENUNJUKKAN LIST STOK KOPI
def stok_kopi():
    clear()
    display_stok_kopi()
    while True:
        tabel()
        break
    kembali()

#PILIHAN 2 MENAMBAH JENIS BIJI KOPI BARU
def tambah_stok():
    with open(path, 'a', newline= '') as tambah:
        csvTambah = csv.writer(tambah)
        jenis_kopi = input("Masukkan jenis kopi baru : ")
        if cek_kopi(jenis_kopi):
            print("Jenis Kopi sudah ada dalam stok!")
        else:
            stok_kopi = input("Masukkan jumlah stok kopi: ")
            with open(path, 'r') as file:
                nomor = len(list(csv.reader(file)))
            csvTambah.writerow([
                nomor,jenis_kopi,stok_kopi])
            tambah.close()
            clear()
            print(hijau+"Jenis Kopi berhasil ditambahkan! \n"+end)
        input("\nEnter untuk lanjutkan")
        clear()
        main()

##MENGECEK APAKAH JENIS BIJI KOPI SUDAH ADA
def cek_kopi(jenis_kopi):
    with open(path, 'r', newline='') as fileBaca:
        csvReader = csv.reader(fileBaca)
        for row in csvReader:
            if jenis_kopi == row[1]:
                return True
    return False
#PILIHAN 3 MENGHAPUS JENIS BIJI KOPI DARI TABEL
def hapus_stok():
        file = pd.read_csv(path)
        clear()
        tabel()
        hapus_no = int(input("Nomor Berapa Yang Ingin DiHapus? = "))
        file.drop(hapus_no-1,inplace = True)
        # file.index=list(range(len(file))) #type:ignore)
        file.to_csv(path,index = False)
        clear()
        print(hijau+f"Nomor {hapus_no} Berhasil Terhapus!"+end)
        tabel()
        kembali()

#PILIHAN 4 MENGUBAH JUMLAH STOK JENIS KOPI TERTENTU
def ubah_stok():
    clear()
    tabel()
    nomor_ubah = int(input("Masukkan nomor jenis kopi yang ingin diubah = "))
    cekNomer = cek_nomor_kopi(nomor_ubah)
    if cekNomer == True:
        stok_baru = int(input("Masukkan jumlah stok baru = "))
        file.iloc[nomor_ubah-1,2] = stok_baru
        file.to_csv(path, index = False)
        print("Jumlah stok telah diubah!")
        kembali()
    else :
        print("Tidak ada jenis kopi yang bisa diubah!")
        kembali()
        tabel()
#MENGECEK APAKAH NOMOR ADA, 
def cek_nomor_kopi(nomor_ubah):
    with open(path, 'r',) as fileBaca:
        csvReader = csv.reader(fileBaca)
        for row in csvReader:
            # print(row)
            if str(nomor_ubah) in row[0]:
                return True

#Keluar dari Program
def keluar():
    clear()
    print('''
        +===========================+
        |        TERIMA KASIH       |
        |         BEAN--RACK        |
        +===========================+
        ''')
    exit()
    

#LOGIN
def login(name, pw):
    with open(pathLogin, "r") as data:
        user_data = json.load(data)
    user_dict = {}
    for i in user_data:
        if name in i["nama"]:
            user_dict["username"] = i["nama"]
            user_dict["password"] = i["pw"]
    if pw != user_dict["password"]:
        print("Login Gagal")
        sys.exit(1)
    return "Login sukses"

def main():
    if login(nama, password):
        while True:
            display_menu()
            pilihan()

print(f'''
        +============================+
        |                            |
        |    WELCOME TO BEAN-RACK    |
        |                            |
        +============================+ 
          ''')
nama = input("\n\tMasukan nama: ")
password = getpass.getpass("\tMasukan password: ")
clear()
main()


# slicing bara rklom nomer
# simpan variabel
# len dari variabel
# masukin ke csv lagi