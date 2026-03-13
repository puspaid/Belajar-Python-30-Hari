from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import pandas as pd

# 1. Data contoh: Nama, Tingkat Pendidikan, dan Skor Tes
data = {
    'Pendidikan': ['SMA', 'SMP', 'SD', 'SMA', 'SMP'],
    'Skor_Tes': [85, 70, 60, 90, 75]
}
df = pd.DataFrame(data)

# 2. Label Encoding (Mengubah teks pendidikan jadi angka)
le = LabelEncoder()
df['Pendidikan_Angka'] = le.fit_transform(df['Pendidikan'])

# 3. Scaling (Mengubah Skor_Tes menjadi skala 0 sampai 1)
scaler = MinMaxScaler()
# Kita gunakan [[]] karena scaler minta data dalam bentuk tabel (2D)
df['Skor_Normal'] = scaler.fit_transform(df[['Skor_Tes']])

print("--- Data Hasil Olahan Scikit-Learn ---")
print(df)