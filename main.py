import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate


data = pd.read_csv('Analisis Data dan Visualisasi/nilai_siswa.csv', sep=';')

print("=== Informasi Dataset ===")
print(data.info())

print("\n=== 5 Data Pertama ===")
print(tabulate(data.head(), headers='keys', tablefmt='fancy_grid', showindex=False))

print("\n=== Statistik Deskriptif ===")
print(data.describe())

print("\n=== Hitung Rata-rata, median, modus ===")
print("Rata-rata: ", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

print("\n=== Tampilkan Nilai per mata pelajaran ===")

#Matematika
matematika = data[data['Matpel'] == 'Matematika']
print("\nMatematika:")
print(matematika)

#Bahasa Indonesia
BahasaIndonesia = data[data['Matpel'] == 'Bahasa Indonesia']
print("\nBahasa Indonesia : ")
print(BahasaIndonesia)

# Bahasa Inggris
inggris = data[data['Matpel'] == 'Bahasa Inggris']
print("\nBahasa Inggris:")
print(inggris)

# Produktif (kalau ada di datamu)
produktif = data[data['Matpel'] == 'Produktif']
print("\nProduktif:")
print(produktif)

# === Nilai Maksimum dan Minimum per Mata Pelajaran ===
print("\n=== Nilai Maksimum & Minimum per Mata Pelajaran ===")
print(data.groupby('Matpel')['Nilai'].agg(['max', 'min']))

print("\n=== Grafik Rata-Rata Nilai per Mata Pelajaran ===")
rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

sns.boxplot(x='Matpel', y='Nilai', data=data, palette='Set2')
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai')
plt.tight_layout()
plt.show()