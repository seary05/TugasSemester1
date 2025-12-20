# import library os untuk hapus layar
# import os # Commented out as cls is not used

import datetime # Import datetime module for date objects

# deklarasi class untuk membuat objek Buku
class Buku:
    # inisialisasi objek Buku
    def __init__ (self,judul,penulis,isbn,stok,stok_pinjam = 0) :
        self.judul = judul
        self.penulis = penulis
        self.isbn = int(isbn)
        self.stok = int(stok)
        self.stok_pinjam = int(stok_pinjam)

    # fungsi untuk input data data_buku
    def get_input_for_new_book() :
        judul = input("Masukan Judul Buku : ")
        penulis = input("Masukan Nama Penulis : ")
        stok = input_int("Jumlah Stok")
        

        return judul,penulis,stok

    def get_input_for_update() :
        judul_baru = input("Masukan Judul Buku Baru : ")
        penulis_baru = input("Masukan Nama Penulis Baru: ")
        stok_baru = input_int("Jumlah Stok Baru")

        return judul_baru,penulis_baru,stok_baru

class Peminjaman:
    def __init__(self, isbn, peminjam, tanggal_pinjam=None, tanggal_kembali=None):
        self.isbn = isbn
        self.peminjam = peminjam
        self.tanggal_pinjam = tanggal_pinjam if tanggal_pinjam is not None else datetime.date.today()
        self.tanggal_kembali = tanggal_kembali

def input_int(var) :
    inputan = ""
    while True :
        try :
            inputan = input(f"Masukan {var} : ")
            return int(inputan)
        except ValueError :
            print(f"{var} Harus Berupa Angka Bulat!!!")
            continue


# fungsi untuk menampilkan tabel
def tabel_buku() :
    no = 1
    print("------------------------------------------------------------------------------------------------------------")
    print("| %-3s | %-20s | %-20s | %10s | %-3s | %-3s |"%("No","judul","penulis","isbn","stok", "stck"))
    print("----------------------------------------------------------------------------------------------------------------------")
    # Ensure data_buku is not empty before iterating
    if not data_buku:
        print("|                                              Tidak Ada Data Buku                                                    |")
    for i in data_buku : # i is the isbn key (int)
        print("| %3s | %-20s | %-20s | %10s | %-3s | %-3s |"%(no,data_buku[i].judul[:20],data_buku[i].penulis[:20],
                                                                              data_buku[i].isbn,data_buku[i].stok, data_buku[i].stok_pinjam))
        no += 1
    print("-----------------------------------------------------------------------------------------------------------------")

def tabel_peminjaman() :
    
    no = 1
    print("------------------------------------------------------------------------------------------------------------")
    print("| %-3s | %-10s | %-20s | %10s | %-10s | %-10s |"%("No","Peminjam","Judul","ISBN","Tgl pinjam", "Tgl Kembali"))
    print("----------------------------------------------------------------------------------------------------------------------")
    # Ensure data_buku is not empty before iterating
    if not daftar_peminjaman:
        print("|                                              Tidak Ada Data Peminjaman                                             |")
    for i in daftar_peminjaman : # i is the isbn key (int)
        idx = 0
        print("| %3s | %-20s | %-20s | %10s | %-3s | %-3s |"%(no,daftar_peminjaman[idx][1],data_buku[i].judul[:20],
                                                                              daftar_peminjaman[idx][0],daftar_peminjaman[idx][2], daftar_peminjaman[idx][3]))
        no += 1
    print("-----------------------------------------------------------------------------------------------------------------")

# fungsi untuk menampilkan menu
def menu():
    while True :
        # os.system("cls") # Commented out for Colab compatibility
        tabel_buku()
        print("Mau Ngapain Bang?")
        print("A. Input Data")
        print("B. Ubah Data")
        print("C. Hapus Data")
        print("P. Pinjam Buku")
        print("K. Kembalikan Buku") # Added new option for returning
        print("D. Keluar")
        print(">> ",end="")
        pilihan = input().lower()
        # os.system("cls") # Commented out for Colab compatibility
        # tabel() # No need to show table again immediately after menu choice
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
                for i_key in data_buku : # Iterate over keys (ISBNs)
                    book = data_buku[i_key]
                    file.write(f"{book.isbn},{book.judul},{book.penulis},{book.stok},{book.stok_pinjam}\n")
                file.close()

                # Save borrowing data
                file_peminjaman = open("./Data_Peminjaman.csv", "w")
                for peminjaman_obj in daftar_peminjaman:
                    file_peminjaman.write(f"{peminjaman_obj.isbn},{peminjaman_obj.peminjam},{peminjaman_obj.tanggal_pinjam},{peminjaman_obj.tanggal_kembali if peminjaman_obj.tanggal_kembali else 'None'}\n")
                file_peminjaman.close()
                break
            case _ :
                print("Pilihan Tidak Valid!!!\nTekan Enter Untuk Lanjut...")
                input()

# fungsi untuk input data
def input_data() :
    print("Input Data Buku")
    isbn = input_int("ISBN Buku\t")
    if isbn in data_buku:
        print("ISBN sudah ada dalam daftar. Tekan enter untuk lanjut...")
        input()
        return
    judul,penulis,stok= Buku.get_input_for_new_book()
    data_buku[isbn] = Buku(judul,penulis,isbn,stok)

# fungsi untuk hapus data
def ubah_data():
    print("Ubah Data Buku")
    # print(data_buku.keys()) # For debugging, can be removed
    isbn_to_ubah = input_int("ISBN Buku yang akan diubah\t")

    if isbn_to_ubah in data_buku:
        print(f"Mengubah data buku {data_buku[isbn_to_ubah].judul}")
        judul_baru, penulis_baru, stok_baru = Buku.get_input_for_update()
        # Update the attributes of the existing Buku object
        data_buku[isbn_to_ubah].judul = judul_baru
        data_buku[isbn_to_ubah].penulis = penulis_baru
        data_buku[isbn_to_ubah].stok = stok_baru
        print("Data buku berhasil diubah!")
        input("Tekan enter untuk lanjut...")
    else :
        print("ISBN Tidak ada dalam daftar data buku")
        print("Tekan enter untuk lanjut...",end="")
        input()


# Fungsi Untuk Hapus Data
def hapus_data():
    print("Hapus Data Buku")
    isbn_to_hapus = input_int("Masukan ISBN Buku yang akan dihapus\t")

    if isbn_to_hapus in data_buku:
        print(f"Menghapus buku: {data_buku[isbn_to_hapus].judul}")
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
            # if not book.is_borrowed:
            peminjam_name = input("Masukkan nama peminjam : ")
            new_peminjaman = Peminjaman(isbn_to_borrow, peminjam_name)
            daftar_peminjaman.append(new_peminjaman)
            book.stok -= 1
            book.stok_pinjam += 1
            print(f"Buku '{book.judul}' berhasil dipinjam oleh {peminjam_name}!")
            # else:
            #     print(f"Buku '{book.judul}' saat ini sedang dipinjam oleh {book.borrowed_by}.")
        else:
            print("Semua stok buku sedang dipinjam")
            print("Tekan enter untuk lanjut...",end="")
            input()
    else:
        print("ISBN buku tidak ditemukan.")
    input("Tekan enter untuk lanjut...")

def kembalikan_buku():
    print("\n--- Pengembalian Buku ---")
    tabel_peminjaman()
    isbn_to_return = input_int("ISBN buku yang ingin dikembalikan")

    if isbn_to_return in data_buku:
        book = data_buku[isbn_to_return]

        # Find and update the corresponding Peminjaman record
        for peminjaman_record in daftar_peminjaman:
            if peminjaman_record.isbn == isbn_to_return:
                # and peminjaman_record.tanggal_kembali is None:
                nama_peminjam = input("Nama Peminjam")
                if nama_peminjam in peminjaman_record[1]:
                    peminjaman_record.tanggal_kembali = datetime.date.today()
                    break # Assuming only one active borrowing for a book at a time
                else:
                    print("Data Peminjaman tidak ditemukan")
                    print("Tekan enter untuk lanjut...",end="")
                    input()

        print(f"Buku '{book.judul}' berhasil dikembalikan!")
        book.stok += 1
        book.stok_pinjam -= 1
    else:
        print("ISBN buku tidak ditemukan.")
    input("Tekan enter untuk lanjut...")


# Load Data
data_buku = {}
daftar_peminjaman = [] # New list to store Peminjaman objects

# Load Buku Data
file = open("./Data_Buku.csv","a+")
file.seek(0) # Move cursor to the beginning of the file to read
for line in file.readlines() :
    line = line.strip() # Remove newline character
    if not line: continue # Skip empty lines
    try:
        parts = line.split(",")
        isbn_str,judul,penulis,stok_str,stok_pinjam_str = parts[0], parts[1], parts[2], parts[3], parts[4]
        isbn = int(isbn_str)
        stok = int(stok_str)
        stok_pinjam = int(stok_pinjam_str)
        
        data_buku[isbn] = Buku(judul,penulis,isbn,stok,stok_pinjam)
    except ValueError as e:
        print(f"Error parsing line in book data: {line}. Skipping. Error: {e}")

file.close()

# Load Peminjaman Data (New)
try:
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
except FileNotFoundError:
    print("File data peminjaman belum ada, akan dibuat saat keluar.")

# Print Watermark
print("+------------------------------------------+")
print("|                                          |")
print("|     Program Pencatat Nilai data_buku     |") # Should be "Buku" not "data_buku"
print("|                                          |")
print("|          By Deskafim_ ,Ionian            |")
print("|                                          |")
print("+------------------------------------------+")
print()
print("Tekan enter untuk lanjut...",end="")
input()
menu()
# os.system("cls") # Commented out for Colab compatibility
print("===== Program Selesai ====")