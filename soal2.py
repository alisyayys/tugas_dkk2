#konversi nilai angka ke huruf
#(percabangan)

nilai = int(input("masukkan nilai: "))
if nilai > 100 or nilai < 0:
    print("nilai tidak valid")
elif nilai >= 85:
    print("Grade: A")
elif nilai >= 70:
    print("Grade: B")
elif nilai >= 55:
    print("Grade: C")
elif nilai >= 40:
    print("Grade: D")
else:
    print("Grade: E")