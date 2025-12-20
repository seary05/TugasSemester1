
import os
import datetime 

class Buku:
    def __init__ (self,judul,penulis,isbn,stok,stok_pinjam = 0) :
        self.judul = judul
        self.penulis = penulis
        self.isbn = int(isbn)
        self.stok = int(stok)
        self.stok_pinjam = int(stok_pinjam)

    def input_data_baru() :
        judul = input_str("Judul Buku").lower()
        penulis = input_str("Nama Penulis").lower()
        stok = input_int("Jumlah Stok")
        
        return judul,penulis,stok

    def input_data_update() :
        judul_baru = input_str("Judul Buku Baru").lower()
        penulis_baru = input_str("Nama Penulis Baru").lower()
        stok_baru = input_int("Jumlah Stok Baru")

        return judul_baru,penulis_baru,stok_baru

class Peminjaman:
    def __init__(self, isbn, peminjam, tanggal_pinjam=None, tanggal_kembali=None):
        self.isbn = isbn
        self.peminjam = peminjam
        self.tanggal_pinjam = tanggal_pinjam if tanggal_pinjam is not None else datetime.date.today()
        self.tanggal_kembali = tanggal_kembali

def input_str(var):
    inputan = ""
    while len(inputan.strip()) <= 0 :
        inputan = input(f"Masukkan {var} : ")
    return inputan


def input_int(var) :
    inputan = ""
    while True :
        try :
            inputan = input(f"Masukkan {var} : ")
            return int(inputan)
        except ValueError :
            print(f"{var} Harus Berupa Angka Bulat!!!")
            continue

def tabel_buku() :
    no = 1
    print("-"*89)
    print("| %-3s | %-20s | %-20s | %10s | %-4s | %-13s |"%("No","judul","penulis","isbn","stok", "stok dipinjam"))
    print("-"*89)
    if not data_buku:
        print("|" +"Tidak Ada Data Buku".center(87)+"|")
    for i in data_buku : 
        print("| %3s | %-20s | %-20s | %10s | %-4s | %-13s |"%(no,data_buku[i].judul[:20].title(),data_buku[i].penulis[:20].title(),
                                                                              data_buku[i].isbn,data_buku[i].stok, data_buku[i].stok_pinjam))
        no += 1
    print("-"*89)

def menu():
    while True :
        os.system("cls") 
        tabel_buku()
        print("Mau Ngapain?")
        print("A. Input Data")
        print("B. Ubah Data")
        print("C. Hapus Data")
        print("P. Pinjam Buku")
        print("K. Kembalikan Buku") 
        print("D. Keluar")
        print(">> ",end="")
        pilihan = input().lower()

        match pilihan :
            case "a" :
                input_data()
            case "b" :
                ubah_data()
            case "c" :
                hapus_data()
            case "p" :
                pinjam_buku()
            case "k" :
                kembalikan_buku()
            case "d" :
                file = open("./Data_Buku.csv","w")
                for i_key in data_buku : 
                    book = data_buku[i_key]
                    file.write(f"{book.isbn},{book.judul},{book.penulis},{book.stok},{book.stok_pinjam}\n")
                file.close()

                file_peminjaman = open("./Data_Peminjaman.csv", "w")
                for peminjaman_obj in daftar_peminjaman:
                    file_peminjaman.write(f"{peminjaman_obj.isbn},{peminjaman_obj.peminjam},{peminjaman_obj.tanggal_pinjam},{peminjaman_obj.tanggal_kembali if peminjaman_obj.tanggal_kembali else 'None'}\n")
                file_peminjaman.close()
                break
            case _ :
                print("Pilihan Tidak Valid!!!\nTekan Enter Untuk Lanjut...")
                input()


def input_data() :
    print("--Input Data Buku--")
    isbn = input_int("ISBN Buku\t")
    if isbn in data_buku:
        print("ISBN sudah ada dalam daftar. Tekan enter untuk lanjut...")
        input()
        return
    judul,penulis,stok= Buku.input_data_baru()
    data_buku[isbn] = Buku(judul,penulis,isbn,stok)
    print("Data buku berhasil diubah!")
    input("Tekan enter untuk lanjut...")

def ubah_data():
    print("--Ubah Data Buku--")
    isbn_update = input_int("ISBN Buku yang akan diubah\t")

    if isbn_update in data_buku:
        print(f"Mengubah data buku {data_buku[isbn_update].judul.title()}")
        judul_baru, penulis_baru, stok_baru = Buku.input_data_update()
        data_buku[isbn_update].judul = judul_baru
        data_buku[isbn_update].penulis = penulis_baru
        data_buku[isbn_update].stok = stok_baru
        print("Data buku berhasil diubah!")
        input("Tekan enter untuk lanjut...")
    else :
        print("ISBN Tidak ada dalam daftar data buku")
        print("Tekan enter untuk lanjut...",end="")
        input()

def hapus_data():
    print("Hapus Data Buku")
    isbn_to_hapus = input_int("Masukkan ISBN Buku yang akan dihapus\t")

    if isbn_to_hapus in data_buku:
        print(f"Menghapus buku: {data_buku[isbn_to_hapus].judul.title()}")
        del data_buku[isbn_to_hapus]
        print("Buku berhasil dihapus!")
        input("Tekan enter untuk lanjut...")
    else :
        print("ISBN Tidak ada dalam daftar data buku")
        print("Tekan enter untuk lanjut...",end="")
        input()

def pinjam_buku():
    print("\n--- Peminjaman Buku ---")
    isbn_to_borrow = input_int("ISBN buku yang ingin dipinjam")

    if isbn_to_borrow in data_buku:
        book = data_buku[isbn_to_borrow]
        if book.stok >= 1:
            peminjam_name = input("Masukkan nama peminjam : ")
            new_peminjaman = Peminjaman(isbn_to_borrow, peminjam_name)
            daftar_peminjaman.append(new_peminjaman)
            book.stok -= 1
            book.stok_pinjam += 1
            print(f"Buku '{book.judul.title()}' berhasil dipinjam oleh {peminjam_name}!")
        else:
            print(f"Semua stok buku {book.judul.title()} sedang dipinjam")
    else:
        print("ISBN buku tidak ditemukan.")
    input("Tekan enter untuk lanjut...")

def kembalikan_buku():
    print("\n--- Pengembalian Buku ---")
    isbn_to_return = input_int("ISBN buku yang ingin dikembalikan")

    if isbn_to_return in data_buku:
        book = data_buku[isbn_to_return]
        if book.stok_pinjam >= 1:
            nama_peminjam = input("Siapa nama peminjam? ").lower()
            for peminjaman_record in daftar_peminjaman:
                if peminjaman_record.isbn == book.isbn:
                    if peminjaman_record.tanggal_kembali:
                        continue
                    else:
                        if peminjaman_record.peminjam.lower() == nama_peminjam:
                            peminjaman_record.tanggal_kembali = datetime.date.today()
                            print(f"Buku '{book.judul.title()}' berhasil dikembalikan!")
                            book.stok += 1
                            book.stok_pinjam -= 1
                            break
                        else:
                            continue
                else:
                    continue
            else:
                print("Data Peminjaman tidak ditemukan")
        else:
            print(f"Tidak ada buku {book.judul.title()} yang dipinjam")
    else:
        print("ISBN buku tidak ditemukan.")
    
    input("Tekan enter untuk lanjut...")


data_buku = {}
daftar_peminjaman = []

file = open("./Data_Buku.csv","a+")
file.seek(0) 
for line in file.readlines() :
    line = line.strip() 
    if not line: 
        continue 
    try:
        bagian = line.split(",")
        isbn_str,judul,penulis,stok_str,stok_pinjam_str = bagian[0], bagian[1], bagian[2], bagian[3], bagian[4]
        isbn = int(isbn_str)
        stok = int(stok_str)
        stok_pinjam = int(stok_pinjam_str)
        
        data_buku[isbn] = Buku(judul,penulis,isbn,stok,stok_pinjam)
    except ValueError as e:
        print(f"Error parsing line in book data: {line}. Skipping. Error: {e}")

file.close()

file_peminjaman = open("./Data_Peminjaman.csv", "a+")
file_peminjaman.seek(0)
for line in file_peminjaman.readlines():
    line = line.strip()
    if not line: continue
    try:
        parts = line.split(",")
        isbn_peminjaman = int(parts[0])
        peminjam_name = parts[1]
        tanggal_pinjam_str = parts[2]
        tanggal_kembali_str = parts[3]

        tanggal_pinjam = datetime.datetime.strptime(tanggal_pinjam_str, '%Y-%m-%d').date()
        tanggal_kembali = datetime.datetime.strptime(tanggal_kembali_str, '%Y-%m-%d').date() if tanggal_kembali_str != 'None' else None

        daftar_peminjaman.append(Peminjaman(isbn_peminjaman, peminjam_name, tanggal_pinjam, tanggal_kembali))
    except Exception as e:
        print(f"Error parsing line in borrowing data: {line}. Skipping. Error: {e}")

file_peminjaman.close()

os.system("cls")
print("+"+ "-"*66 + "+")
print("|" + " "*66 + "|")
print("|"+  "Program Peminjaman Buku Gratis".center(66) + "|")
print("|" + " "*66 + "|")
print("|"+  "By Muhammad Al Ghiffary Razan (L0225026)".center(66) + "|")
print("|" + " "*66 + "|")
print("+"+ "-"*66 + "+")
print()
print("Tekan enter untuk lanjut...",end="")
input()
menu()

os.system("cls")
print("===== Program Selesai ====")