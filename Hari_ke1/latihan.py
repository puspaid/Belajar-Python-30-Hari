# --- KALKULATOR INTERAKTIF HARI 1 ---

#1. Mengambil input dari user (Anda)
print("=== PROGRAM MENYAPA & KALKULATOR ===")
nama = input("Masukkan nama anda: ")
print("Halo " + nama + ", mari kita berhitung!")

#2. Input angka (perlu diubah ke 'int' agar bisa dijumlahkan)
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

# 3. Proses Perhitungan
tambah = angka1 + angka2
kurang = angka1 - angka2
kali = angka1 * angka2
bagi = angka1 / angka2

# 4. Menampilkan Hasil yang Rapi
print("-" * 30)
print("HASIL PERHITUNGAN UNTUK", nama.upper())
print("-" * 30)
print("Penjumlahan:", angka1, "+", angka2, "=", tambah)
print("Pengurangan:", angka1, "-", angka2, "=", kurang)
print("Perkalian  :", angka1, "x", angka2, "=", kali)
print("Pembagian  :", angka1, "/", angka2, "=", bagi)
print("-" * 30)
print("Terima kasih sudah mencoba!")