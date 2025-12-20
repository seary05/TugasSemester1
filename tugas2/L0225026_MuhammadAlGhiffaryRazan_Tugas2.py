def valid_input(limit):
    while True:
        jumlah_angka_str = input(f"Masukkan angka (minimal {limit}) yang ingin dihitung: ")

        while '.' in jumlah_angka_str:
            print("Input harus bilangan bulat")
            jumlah_angka_str = input("Masukkan bilangan bulat: ")

        try:
            jumlah_angka = int(jumlah_angka_str)

            if jumlah_angka < limit:
                print(f"Masukkan angka yang lebih besar dari atau sama dengan {limit}")
                continue 

            return jumlah_angka 

        except ValueError:
            print("Format Angka tidak Valid")

def menu():
    while True:
        print("\nPilih Jenis perhitungan yang ingin dilakukan")
        print("A. Fibonacci")
        print("B. Faktorial")
        print("C. Keluar dari Program")
        print()

        pilihan = input("Masukkan Pilihan: ").lower().strip()

        match pilihan:
            case "a":
                print("Menghitung hasil bilangan fibonacci")
                inputan = valid_input(1) 
                result = fibonacci(inputan)
                return f"Bilangan Fibonacci ke-{inputan} adalah: {result}"
            case "b":
                print("Menghitung hasil faktorial")
                inputan = valid_input(0) 
                result = faktorial(inputan)
                return f"Faktorial dari {inputan} adalah: {result}"
            case "c":
                return "Terima kasih"
            case _:
                print("\n" + "Input tidak diketahui. Silakan pilih A, B, atau C.")

def fibonacci(jumlah_angka):
    list_fibo = []

    for i in range(1,jumlah_angka+1):
        if i == 1:
            list_fibo.append(0)
        elif i == 2:
            list_fibo.append(1)
        else:
            list_fibo.append(list_fibo[i-2] + list_fibo[i-3])
        
    return list_fibo[-1]
def faktorial(angka):

    if angka <= 1:
        return 1 
    else:
        return faktorial(angka-1) * angka 

print(menu())