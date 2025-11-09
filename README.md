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
<img width="310" height="441" alt="Screenshot 2025-11-09 145016" src="https://github.com/user-attachments/assets/2c1a4ab5-9258-4a9b-8114-6e63bc9a49e0" />

## 7. Menghitung Rata-Rata, Median, dan Modus
```bash
print("\n=== Hitung Rata-rata, Median, Modus ===")
print("Rata-rata: ", data['Nilai'].mean())
print("Median: ", data['Nilai'].median())
print("Modus: ", data['Nilai'].mode()[0])
```
📘 Penjelasan:
Di bagian ini, kita menghitung tiga ukuran utama data:
Rata-rata (Mean) → jumlah semua nilai dibagi total data
Median → nilai tengah dari seluruh data
Modus → nilai yang paling sering muncul
Ketiganya bisa bantu kita melihat kecenderungan nilai siswa secara umum.
### Screenshoot Output
<img width="387" height="109" alt="Screenshot 2025-11-09 145128" src="https://github.com/user-attachments/assets/8d54e1ba-49dc-4ef4-81d7-249492dd427d" />

## 8. Menampilkan Nilai Per Mata Pelajaran
```bash
print("\n=== Tampilkan Nilai per Mata Pelajaran ===")

matematika = data[data['Matpel'] == 'Matematika']
print("\nMatematika:")
print(tabulate(matematika, headers='keys', tablefmt='fancy_grid', showindex=False))

bahasa_indonesia = data[data['Matpel'] == 'Bahasa Indonesia']
print("\nBahasa Indonesia:")
print(tabulate(bahasa_indonesia, headers='keys', tablefmt='fancy_grid', showindex=False))

bahasa_inggris = data[data['Matpel'] == 'Bahasa Inggris']
print("\nBahasa Inggris:")
print(tabulate(bahasa_inggris, headers='keys', tablefmt='fancy_grid', showindex=False))

produktif = data[data['Matpel'] == 'Produktif']
print("\nProduktif:")
print(tabulate(produktif, headers='keys', tablefmt='fancy_grid', showindex=False))
```
📘 Penjelasan:
Kode di atas memfilter data berdasarkan kolom Matpel.
Setiap mata pelajaran ditampilkan secara terpisah agar mudah dilihat siapa saja yang nilainya tinggi atau rendah.
Dengan tabulate, tampilannya jadi kayak tabel beneran — bersih dan jelas.
### Screenshoot Output
<img width="291" height="892" alt="Screenshot 2025-11-09 145400" src="https://github.com/user-attachments/assets/6b911cb9-8280-48a0-8c97-f41a8dbf7a6e" />

## 9. Menampilkan Nilai Maksimum & Minimum per Mata Pelajaran
```bash
print("\n=== Nilai Maksimum & Minimum per Mata Pelajaran ===")
print(tabulate(data.groupby('Matpel')['Nilai'].agg(['max', 'min']), headers='keys', tablefmt='fancy_grid'))
```
📘 Penjelasan:
Di sini kita pakai groupby() untuk mengelompokkan data berdasarkan mata pelajaran.
Fungsi agg(['max', 'min']) menampilkan nilai tertinggi dan terendah dari masing-masing mapel.
### Screenshoot Output
<img width="491" height="308" alt="Screenshot 2025-11-09 145609" src="https://github.com/user-attachments/assets/9a772e8d-dcab-4d75-9b33-f6022f860e43" />

## 10. Membuat Grafik Rata-Rata Nilai per Mata Pelajaran
```bash
print("\n=== Grafik Rata-Rata Nilai per Mata Pelajaran ===")
rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Rata-Rata Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.tight_layout()
plt.show()
```
📈 Penjelasan:
Bagian ini menampilkan grafik batang (bar chart) untuk membandingkan nilai rata-rata tiap mapel.
Warna biru muda (skyblue) bikin grafiknya terlihat lembut dan jelas.
tight_layout() memastikan teks di sekitar grafik gak terpotong.
### Screenshoot Output
<img width="642" height="555" alt="Screenshot 2025-11-09 145952" src="https://github.com/user-attachments/assets/41de67a9-aa49-4ffa-aef9-dfb47622915a" />

## 11. Membuat Boxplot Sebaran Nilai per Mata Pelajaran
```bash
print("\n=== Boxplot Sebaran Nilai per Mata Pelajaran ===")
sns.boxplot(x='Matpel', y='Nilai', data=data, palette='Set2')
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai')
plt.tight_layout()
plt.show()
```
📊 Penjelasan:
Boxplot ini menampilkan sebaran nilai tiap mata pelajaran,
jadi kamu bisa lihat:
Titik median (garis tengah)
Nilai tertinggi & terendah
Nilai-nilai yang menyimpang (outlier)
Warna dari palette='Set2' bikin visualnya lebih menarik dan lembut.
### Screenshoot Output
<img width="636" height="548" alt="Screenshot 2025-11-09 150148" src="https://github.com/user-attachments/assets/ee5b99a6-90e8-40f3-87e0-f5bfc880ca15" />

---

## 🧠 **Analisis dan Pertanyaan**

1. **Mapel mana yang memiliki rata-rata nilai tertinggi?**
   Yang paling tinggi itu **mapel Produktif**, soalnya hampir semua nilainya di atas rata-rata, jarang banget yang rendah.

2. **Mapel mana yang memiliki nilai terendah?**
   Yang paling rendah itu **Bahasa Inggris**, karena ada beberapa siswa nilainya masih di bawah pelajaran lain.

3. **Bagaimana visualisasi membantu dalam memahami data?**
   Grafik sama boxplot itu bantu banget, jadi kita bisa langsung lihat mana pelajaran yang nilainya tinggi atau rendah tanpa harus baca angka satu-satu. Lebih cepat paham juga.

---

## 🧩 **Refleksi Siswa**

1. **Apa hal baru yang kamu pelajari dari kegiatan analisis dan visualisasi data?**
   👉 Aku jadi tahu cara ngolah data pakai Python, terus bisa bikin grafik juga biar hasilnya lebih gampang dibaca.

2. **Kesulitan apa yang kamu alami dalam membuat grafik?**
   👉 Awalnya sempet bingung karena error di library sama data CSV-nya gak kebaca, tapi setelah tahu pakai `sep=';'` dan install library, akhirnya bisa jalan juga.

3. **Menurut kamu AI apa membantu dalam analisis sebuah data?**
   👉 Jelas bantu banget, soalnya AI bisa ngitung dan nampilin data lebih cepat, kita tinggal lihat hasilnya aja. Lebih efisien daripada ngitung manual.

---

# 👨‍💻 Author
## Fahry Irvan Yudiansyah
## Kelas: XI RPL 2
## Sekolah: SMK Telkom Malang
## Proyek: Analisis Data dan Visualisasi Nilai Siswa






