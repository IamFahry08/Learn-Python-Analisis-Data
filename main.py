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
print(tabulate(data.describe(), headers='keys', tablefmt='fancy_grid'))


print("\n=== Hitung Rata-rata, median, modus ===")
print("Rata-rata: ", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

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


print("\n=== Nilai Maksimum & Minimum per Mata Pelajaran ===")
print(tabulate(data.groupby('Matpel')['Nilai'].agg(['max', 'min']), headers='keys', tablefmt='fancy_grid'))

print("\n=== Grafik Rata-Rata Nilai per Mata Pelajaran ===")
rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Rata-Rata Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.tight_layout()
plt.show()


print("\n=== Boxplot Sebaran Nilai per Mata Pelajaran ===")
sns.boxplot(x='Matpel', y='Nilai', data=data, palette='Set2')
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai')
plt.tight_layout()
plt.show()
