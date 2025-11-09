# 🧠 Analisis Data dan Visualisasi Nilai Siswa

Project ini dibuat sebagai tugas **Analisis Data dan Visualisasi Data** menggunakan bahasa pemrograman **Python**.  
Tujuan project ini adalah untuk menganalisis data nilai siswa dari berbagai mata pelajaran dan menampilkan hasilnya dalam bentuk **tabel dan grafik interaktif**.  

---

# ⚙️ Persiapan Awal

## 1. Instalasi Library
Sebelum menjalankan program, pastikan semua library yang dibutuhkan sudah terinstall.

```bash
pip install pandas matplotlib seaborn tabulate
```
## 2. Import Library
```bash
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
```
## 3. Membaca Dataset
```bash
data = pd.read_csv('Analisis Data dan Visualisasi/nilai_siswa.csv', sep=';')
```
📘 Penjelasan:
Kita baca file CSV menggunakan pandas.
Karena datanya dipisahkan pakai titik koma ;, maka perlu menambahkan sep=';'.

## 4. Menampilkan Informasi Dataset
```bash
print("=== Informasi Dataset ===")
print(data.info())
```
📘 Penjelasan:
Perintah ini menampilkan info dasar dataset seperti jumlah kolom, tipe data, dan jumlah baris.
### Screenshoot Output
<img width="379" height="263" alt="Screenshot 2025-11-09 143833" src="https://github.com/user-attachments/assets/8099a54f-9f47-4123-9be9-de079d55f31b" />

## 5. Menampilkan 5 Data Pertama
```bash
print("\n=== 5 Data Pertama ===")
print(tabulate(data.head(), headers='keys', tablefmt='fancy_grid', showindex=False))
```
Menampilkan 5 baris pertama dari dataset biar kita tahu struktur datanya.
Pakai tabulate supaya tampilannya rapi seperti tabel.
### Screenshoot Output 
<img width="370" height="303" alt="Screenshot 2025-11-09 144144" src="https://github.com/user-attachments/assets/631caa91-8e87-4b6b-a96e-a1a8109ee9a5" />

## 6. Menampilkan Statistik Deskriptif
```bash
print("\n=== Statistik Deskriptif ===")
print(tabulate(data.describe(), headers='keys', tablefmt='fancy_grid'))
```
📘 Penjelasan:
describe() menampilkan ringkasan statistik seperti rata-rata, nilai minimum, maksimum, dan standar deviasi.
### Screenshoot Output




