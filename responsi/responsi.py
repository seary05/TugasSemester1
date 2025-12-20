import os

class Book:
    def __init__(self, judul, penulis, isbn,jumlah):
        self.Title = judul
        self.Author = penulis
        self.ISBN = int(isbn)
        self.Stock = int(jumlah)

    def input_data():
        Title = input("Masukkan Judul: ")
        Author = input("Masukkan Nama Penulis: ")
        Jumlah = input_int("Masukkan Jumlah Stok: ")
        return Title, Author, Jumlah

def input_int(prompt):
    inputan = "0.0"
    while inputan.isdigit() != True:
        inputan = input(prompt)
    else:
        inputan = int(inputan)

def input_data_buku():
    ISBN = input("Masukan ISBN Mahasiswa\t: ")
    Title, Author, Stock = Book.input_data()
    data[ISBN] = Book(Title, Author, Stock)
    data[ISBN] = Book(data[ISBN].Title,data[ISBN].Author,data[ISBN].ISBN,data[ISBN].Stock)

def pinjam():
    print("Ketik ISBN buku yang akan ")

def tabel(buku):
    no = 1
    for i in buku:
        print("| %3s | %-20s | %-20s | %13i | %5d |"%(no,buku[i].Title[:20],buku[i].Author[:20],buku[i].ISBN,buku[i].Stock))
        no+=1

def list_buku(buku):
    print("List Buku")
    print("+"+("-"*75)+"+")
    print("| %-3s | %-20s | %-20s | %-13s | %5s |" %("No","Judul","Penulis","ISBN","Stock"))
    print("+"+("-"*75)+"+")
    tabel(buku)

def menu(buku):
    while True:
        os.system("cls")

        print("+"+("-"*75)+"+")
        print("|"+(" "*75)+"|")
        print("|"+"Peminjaman Buku".center(75)+"|")
        print("|"+(" "*75)+"|")
        print("|"+"By Razan L0225026".center(75)+"|")
        print("|"+(" "*75)+"|")
        print("+"+("-"*75)+"+")

        print()

        print("Pilih opsi di bawahL")
        print("A. Masukkan Data Baru")
        print("B. Peminjaman Buku")
        print("C. List Buku")
        print("D. Keluar")
        print(" >> ", end="")

        pilihan = input().lower()

        match pilihan:
            case "a":
                print("Masukkan Data Baru: ")
                input_data_buku()

            case "b":
                print("Peminjaman Buku")
                pinjam()
                return
            
            case "c":
                list_buku(buku)
                return
            case "d":
                print("Terima kasih")
                return
            case _:
                print("Opsi tidak valid!")
                print("Tekan ENTER untuk lanjut...")
                input()

data = {}
data["1234567891013"] = Book("Don Quixote", "Roberto", 1234567891013, 3)
data["1234567891014"] = Book("Don ", "Roberto", 1234567891013, 3)
data["1234567891015"] = Book("Don ", "Roberto", 1234567891013, 3)
data["1234567891016"] = Book("Don ", "Roberto", 1234567891013, 3)

menu(data)