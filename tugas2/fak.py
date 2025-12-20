def faktorial(angka):
    if angka <= 0:
        print("Masukkan lebih besar")
    elif angka == 1:
        return 1
    else:
        print(angka)
        return faktorial(angka-1) * angka
    
print(faktorial(5))