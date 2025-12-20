
def valid_input(limit):
    while True:
        jumlah_angka = 0
        jumlah_angka= input("Masukkan angka yang ingin dihitung: ")
        while '.' in jumlah_angka:
            print("Input harus bilangan bulat")
            jumlah_angka= input("Masukkan bilangan bulat: ")
        else:
            try:
                jumlah_angka = int(jumlah_angka)
                while jumlah_angka < limit:
                    print("Masukkan angka yang lebih besar")
                    jumlah_angka = int(input("Masukkan angka yang besar: "))
                else:
                    return jumlah_angka
            except ValueError:
                print("Format Angka tidak Valid")
                jumlah_angka = input("Masukkan angka yang benar: ")

            
        
def menu():
    print("Pilih Jenis perhitungan yang ingin dilakukan")
    print("A. Fibonacci")
    print("B. Faktorial")
    print("C. Keluar dari Program")
    print()

    pilihan = input("Masukkan Pilihan: ").lower().strip()
    
    match pilihan:
        case "a":
            print("Menghitung hasil bilangan fibonacci")
            inputan = valid_input(1)
            return fibonacci(inputan)
        case "b":
            print("Menghitung hasil faktorial")
            inputan = valid_input(0)
            return faktorial(inputan)
        case "c":
            print("Terima kasih")
            exit()
        case _:
            print("\n" + "Input tidak diketahui" + "\n")
            menu()

def fibonacci(jumlah_angka):
    list_fibo = []

    if jumlah_angka < 1:
        print("Berikan jumlah angka yang lebih besar")
        exit()
    else:
        for i in range(1,jumlah_angka+1):
            if i == 1:
                list_fibo.append(0)
            elif i == 2:
                list_fibo.append(1)
            else:
                list_fibo.append(list_fibo[i-2] + list_fibo[i-3])
    return list_fibo[-1]  

def faktorial(angka):
    if angka < 0:
        print("Masukkan lebih besar")
    elif angka <= 1:
        return 1
    else:
        return faktorial(angka-1) * angka

print(menu())
