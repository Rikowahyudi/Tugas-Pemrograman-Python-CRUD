import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


list_data = []

def show_menu():
    clear_screen()
    print("=== APLIKASI KONTAK ===")
    print("[1] Lihat Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("[0] Exit")
    print("---------------------")
    menu = input("Pilih menu> ")
    
    if menu == '1':
        menu1()
    elif menu == '2':
        menu2()
    elif menu == '3':
        menu3()
    elif menu == '4':
        menu4()
    elif menu == '0':
        print("Terimakasih Telah Berkunjung")
        exit()
    else:
        print("Menu yang anda masukkan tidak ada, Masukkan pilihan yang tersedia")
        kembali()
        
def menu1():
        print('NIM  || Nama')
        if not list_data:
            print('Data Masih Kosong')
        else:
            for data in list_data :
                print(f"{data['NIM']} || {data['Nama']}")
        kembali()

def menu2():
    NIM = input("Masukka NIM Anda : ")
    Nama = input("Masukkan Nama Anda : ")
    for data in list_data:
        if data['NIM'] == NIM:
            print("NIM sudah ada dalam data")
            kembali()
            return
    list_data.append({"NIM":NIM, "Nama":Nama})
    print("Data Berhasil Ditambahkan")
    kembali()

def menu3():
    NIM = input("Masukkan NIM Anda : ")
    found = False
    for data in list_data:
        if data['NIM'] == NIM:
            found = True
            nama_baru = input("Masukkan Nama Baru : ")
            data['Nama'] = nama_baru
            print("Data Anda Telah Dirubah")
            break
    if not found:
        print("NIM Tidak Ditemukan")
    kembali()
def menu4():
    NIM = input("Masukkan NIM Anda : ")
    found = False
    for data in list_data:
        if data['NIM'] == NIM:
            found = True
            nama_baru = input("Masukkan Nama Baru : ")
            data['Nama'] = nama_baru
            print("Data Anda Telah Dirubah")
            break
        if not found:
            print("NIM Tidak Ditemukan")
    kembali()
def kembali():
    print("\n")
    input("Tekan Enter untuk kembali")
    show_menu()
while(True):
    show_menu()