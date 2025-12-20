def cek_operator(angka1, angka2, operator):
    if operator == "+":
        print(f"{angka1} {operator} {angka2} : {angka1 + angka2}")

    elif operator == "-":
        print(f"{angka1} {operator} {angka2} : {angka1 - angka2}")
    
    elif operator == "*":
        print(f"{angka1} {operator} {angka2} : {angka1 * angka2}")

    elif operator == "/":
        print(f"{angka1} {operator} {angka2} : {angka1 / angka2}")
    
    else:
        print("operator tidak didukung")

try:
    angka1 = int(input("masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
except ValueError:
    print("Harus memasukkan angka")
    exit()

operator = input("Masukkan operator:  ")
cek_operator(angka1, angka2, operator)