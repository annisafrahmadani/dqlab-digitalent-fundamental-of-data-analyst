# ====================================================================
# PROJECT: DATA STORYTELLING & GDP VISUALIZATION (WORLDBANK DATASET)
# MODUL: Pengantar Storytelling dengan Visualisasi menggunakan Python
# Skenario kasus oleh: DQLab x Digitalent Komdigi
# ====================================================================

import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------------------------
# STEP 1: Data Preparation & Cleaning (Data Wrangling)
# --------------------------------------------------------------------
pd.set_option('display.max_columns', 10)

url = 'https://googleapis.com'
dataset_worldbank = pd.read_csv(url, delimiter=',', encoding='cp1252')

# Mengatasi missing values dengan mengisi nilai 0
dataset_worldbank = dataset_worldbank.fillna(0)


# --------------------------------------------------------------------
# STEP 2: Analisis Tren GDP per Kapita Negara ASEAN (Line Chart)
# --------------------------------------------------------------------
# Memfilter data spesifik untuk negara Indonesia, Malaysia, Singapura, dan Thailand
dataset_indonesia = dataset_worldbank[dataset_worldbank['country'] == 'Indonesia']
dataset_malaysia = dataset_worldbank[dataset_worldbank['country'] == 'Malaysia']
dataset_singapore = dataset_worldbank[dataset_worldbank['country'] == 'Singapore']
dataset_thailand = dataset_worldbank[dataset_worldbank['country'] == 'Thailand']

# Inisialisasi kanvas grafik dengan ukuran 12 x 10 inci
fig = plt.figure(figsize=(12, 10))

# Membuat grafik pertama (Baris 2, Kolom 1, Posisi Ke-1)
ax1 = plt.subplot(211)
ax1.plot(dataset_indonesia['year'], dataset_indonesia['realgdppercapita'], label='Indonesia')
ax1.plot(dataset_malaysia['year'], dataset_malaysia['realgdppercapita'], label='Malaysia')
ax1.plot(dataset_singapore['year'], dataset_singapore['realgdppercapita'], label='Singapore')
ax1.plot(dataset_thailand['year'], dataset_thailand['realgdppercapita'], label='Thailand')

# Konfigurasi elemen visual grafik pertama
ax1.legend()
ax1.grid(True)
ax1.set_xlabel('Tahun')
ax1.set_ylabel('GDP per Kapita')
ax1.set_title('GDP per Kapita untuk Empat Negara ASEAN', fontsize=14)


# --------------------------------------------------------------------
# STEP 3: Analisis Top 20 Negara dengan GDP Tertinggi Tahun 2015 (Bar Chart)
# --------------------------------------------------------------------
# Mengambil subset data tahun 2015 dan menyaring 20 negara teratas
dataset_2015 = dataset_worldbank[dataset_worldbank['year'] == 2015].nlargest(20, 'realgdppercapita')

# Membuat grafik kedua (Baris 2, Kolom 1, Posisi Ke-2)
ax2 = plt.subplot(212)
ax2.bar(dataset_2015['country'], dataset_2015['realgdppercapita'])

# Konfigurasi elemen visual grafik kedua
ax2.grid(axis='y')
ax2.set_xlabel('Negara')
ax2.set_ylabel('GDP per Kapita')
ax2.set_title('20 Negara dengan GDP per Kapita Tertinggi di 2015', fontsize=14)

# Memutar teks nama negara pada sumbu X sebesar 90 derajat agar terbaca rapi
plt.xticks(rotation=90)


# --------------------------------------------------------------------
# STEP 4: Render & Tampilkan Grafik
# --------------------------------------------------------------------
plt.tight_layout()
plt.show()
