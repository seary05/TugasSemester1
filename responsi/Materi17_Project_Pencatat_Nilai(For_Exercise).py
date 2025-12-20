# deklarasi class untuk membuat objek data_mahasiswa
import os

class data_mahasiswa:
    def __init__(self, nama, ssd, oak, mtk, dpm):
        self.nama = nama
        self.ssd = float(ssd)
        self.oak = float(oak)
        self.mtk = float(mtk)
        self.dpm = float(dpm)

    def rata2(self):    # Method
        return (self.ssd + self.oak + self.mtk + self.dpm) / 4

nama = "Muhammad Al Ghiffary"

def tabel(mahasiswa):
    print("-"*70)
    print("| %-8s | %-20s | %-5s | %3s | %3s | %3s | %5s |" %("NIM","Nama","SSD","OAK","MTK","DPM","Rata2"))
    print("-"*70)
    for i in mahasiswa:
        print("| %8s | %-20s | %5.1f | %5.1f | %5.1f | %5.1f | %5.1f|"%(i,mahasiswa[i].nama[:20],mahasiswa[i].ssd,mahasiswa[i].oak,mahasiswa[i].mtk,mahasiswa[i].dpm, mahasiswa[i].rata2()))

def menu(mahasiswa):
    while True:
        os.system("cls")
        tabel(mahasiswa)

        print("Pilih opsi di bawahL")
        print("A. Masukkan Data Baru")
        print("B. Keluar")
        print(" >> ", end="")

        pilihan = input().upper()

        match pilihan:
            case "A":
                print("Masukkan Data Baru: ")
                input_data_mahasiswa()
            case "B":
                return
            case _:
                print("Opsi tidak valid!")
                print("Tekan ENTER untuk lanjut...")
                input()

def input_float(var):
    while True:
        try:
            return float(input(f"Masukkan nilai {var}: "))
        except ValueError:
            print("Nilai harus berupa angka desimal!!!!")

def input_data_mahasiswa():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    nilai_ssd = input_float("SSD")
    nilai_oak = input_float("OAK")
    nilai_mtk = input_float("MTK")
    nilai_dpm = input_float("DPM")

    mahasiswa[nim] = data_mahasiswa(mahasiswa[nim].nama, mahasiswa[nim].ssd, mahasiswa[nim].oak, mahasiswa[nim].mtk, mahasiswa[nim].dpm)


mahasiswa = {}
mahasiswa["L0225026"] = data_mahasiswa("Muhammad Al Ghiffary Razan", 90, 89, 93, 95)
mahasiswa["L0225024"] = data_mahasiswa("Istiqaamah Hamiidah", 92, 87, 98, 99)
menu(mahasiswa)

# Kelebihan Program :
# 1. Program dilengkapi menu dengan pilihan ganda untuk memudahkan pengguna
# 2. Program dilengkapi fitur ubah dan hapus data untuk mengatasi terjadinya salah input
# 3. Program dilengkapi dengan error handling saat penginputan nilai
# 4. Program akan menyimpan data kedalam file agar data tidak hilang setelah prograam ditutup

# Kekurangan Program :
# 1. Program tidak dilengkapi GUI dan tampilan hanya berupa karakter didalam terminal
# 2. Program tidak menyediakan fitur penghapusan atau penambahan mata kuliah tertentu
# 3. Program tidak menyediakan fitur SKS sehingga tidak dapat menghitung IP Semester
# 4. Program tidak menyediakan adanya fitur kategori nilai Tugas, project, Ujian
# 5. Program tidak menyediakan fitur penghitungan nilai tingkat lanjut seperti tugas 10%, project 50%, Ujian 40%