import pandas as pd

print("--- Program Input Kota Sederhana ---")

# 1. Mengambil input dari kamu di terminal
kota1 = input("Masukkan nama kota pertama: ")
kota2 = input("Masukkan nama kota kedua: ")
kota3 = input("Masukkan nama kota ketiga (sama dengan salah satu di atas boleh): ")

# 2. Masukkan ke dalam list
daftar_kota = [kota1, kota2, kota3]
df = pd.DataFrame({'Kota': daftar_kota})

# 3. Proses One-Hot Encoding
# Kita pakai dtype=int agar hasilnya angka 1 dan 0
df_hasil = pd.get_dummies(df, columns=['Kota'], dtype=int)

print("\n--- Hasil Tabel One-Hot Encoding Anda ---")
print(df_hasil)