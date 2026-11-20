#penentu bilangan ganjil/genap dan positif/negatif
#percabangan

bilangan = int(input("masukkan bilangan: "))

if bilangan == 0:
    print("bilangan nol")
else:
    if bilangan > 0:
        jenis = "positif"
    else:
        jenis = "negatif"

    if bilangan % 2 == 0:
        status = "genap"
    else: 
        status = "ganjil"

    print(f"bilangan {jenis} dan {status}")