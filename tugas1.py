def cek_nol_mutlak(tipe, temperatur):
    tipe_suhu = tipe
    suhu = temperatur

    match tipe_suhu:
        case "Celcius":
            if suhu < -273.15:
                print("masukkan suhu yang lebih besar")
                exit()
        case "Fahrenheit":
            if suhu < -459.67:
                print("masukkan suhu yang lebih besar")
                exit()
        case "Reamur":
            if suhu < -218.52:
                print("masukkan suhu yang lebih besar")
                exit()
        case "Kelvin":
            if suhu < 0:          
                print("masukkan suhu yang lebih besar")
                exit()
        case _ :
            print("Input tidak sesuai")

def cek_tipe(tipe):
    tipe_suhu = tipe
    match tipe_suhu:
        case "1":
            return "Celcius"
        case "2":
            return "Fahrenheit"
        case "3":
            return "Kelvin"
        case "4":
            return "Reamur"
        case _:
            print("Suhu tidak didukung")
            exit()

def hitung_konversi_suhu(temperatur, tipe_awal, tipe_akhir):
    tipe_suhu_awal = tipe_awal
    tipe_suhu_akhir = tipe_akhir
    suhu = temperatur
    

    if ((tipe_suhu_awal == "celcius" or "c") or "c") and (tipe_suhu_akhir == "reamur" or "r"):
        return suhu * 4/5
    elif (tipe_suhu_awal == "celcius" or "c") and (tipe_suhu_akhir == "fahrenheit" or "f"):
        return (suhu * 9/5) + 32
    elif (tipe_suhu_awal == "celcius" or "c") and (tipe_suhu_akhir == "kelvin" or "k"):
        return suhu + 273.15

    elif (tipe_suhu_awal == "fahrenheit" or "f") and (tipe_suhu_akhir == "celcius" or "c"):
        return (suhu-32) * 5/9
    elif (tipe_suhu_awal == "fahrenheit" or "f") and (tipe_suhu_akhir == "reamur" or "r"):
        return (suhu-32) * 4/9
    elif (tipe_suhu_awal == "fahrenheit" or "f") and (tipe_suhu_akhir == "kelvin" or "k"):
        return (suhu + 459.67) * 5/9

    elif (tipe_suhu_awal == "kelvin" or "k") and (tipe_suhu_akhir == "celcius" or "c"):
        return suhu - 273.15
    elif (tipe_suhu_awal == "kelvin" or "k") and (tipe_suhu_akhir == "reamur" or "r"):
        return (suhu - 273.15) * 4/5
    elif (tipe_suhu_awal == "kelvin" or "k") and (tipe_suhu_akhir == "fahrenheit" or "f"):
        return suhu * 9/5 - 459.67 
    
    elif (tipe_suhu_awal == "reamur" or "r") and (tipe_suhu_akhir == "celcius" or "c"):
        return suhu * 5/4
    elif (tipe_suhu_awal == "reamur" or "r") and (tipe_suhu_akhir == "fahrenheit" or "f"):
        return (suhu * 9/4) + 32
    elif (tipe_suhu_awal == "reamur" or "r") and (tipe_suhu_akhir == "kelvin" or "k"):
        return (suhu * 5/4) + 273.15

    else:
        print("Konversi tidak bisa dilakukan")



try:
    suhu = float(
input("""
KETENTUAN:
Celcius >= -273.15
Fahrenheit >= -459.67
Kelvin >= 0
Reamur >= -218.52
      
Suhu yang ingin dirubah: """))
except ValueError:
    print("suhu harus angka boleh desimal")
    exit(0)
    
tipe_suhu_awal = input("""
Masukkan tipe suhu awal: 
    1. Celcius
    2. Fahrenheit
    3. Kelvin
    4. Reamur 
""")
tipe_suhu_awal = cek_tipe(tipe_suhu_awal)

cek_nol_mutlak(tipe_suhu_awal, suhu)


tipe_suhu_akhir = input("""
Masukkan tipe suhu akhir: 
    1. Celcius
    2. Fahrenheit
    3. Kelvin
    4. Reamur 
""")
tipe_suhu_akhir = cek_tipe(tipe_suhu_akhir)

suhu_akhir = hitung_konversi_suhu(suhu, tipe_suhu_awal, tipe_suhu_akhir)

print("Hasil Konversi".center(50))
print("-"*50)
print(f"Suhu Awal : {suhu} {tipe_suhu_awal}".center(50))
print(f"Suhu Akhir : {suhu_akhir} {tipe_suhu_akhir}".center(50))