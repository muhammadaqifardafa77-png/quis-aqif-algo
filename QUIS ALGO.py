# 1. Input nama mahasiswa
nama = input("Nama : ")

# Menentukan target nilai sesuai data mahasiswa (menggunakan percabangan if-elif-else)
if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80
else:
    print("Data mahasiswa tidak ditemukan.")
    exit()

# Menampilkan target nilai mahasiswa
print(f"Targetku {target}!")

# 2 & 3. Perulangan while untuk meminta input nilai maksimal 3 kali percobaan
percobaan = 0
lulus = False

while percobaan < 3:
    percobaan += 1
    nilai = int(input(f"Nilai {percobaan} : "))
    
    # Pengecekan nilai terhadap target
    if nilai >= target:
        lulus = True
        break

# 4. Menampilkan pesan hasil akhir sesuai kondisi kelulusan
if lulus:
    print(f"{nama.capitalize()} berhasil lulus setelah {percobaan} kali percobaan!")
else:
    print(f"{nama.capitalize()} tidak lulus setelah {percobaan} kali percobaan!")