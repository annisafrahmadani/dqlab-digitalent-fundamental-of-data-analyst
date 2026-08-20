# ====================================================================
# PROJECT: DATA WRANGLING & CLEANING DATASET WORLDBANK (PART 1)
# MODUL: Pengantar Storytelling dengan Visualisasi menggunakan Python
# Skenario kasus oleh: DQLab x Digitalent Komdigi
# ====================================================================

import pandas as pd

# 1. Konfigurasi Display Pandas DataFrame
pd.set_option('display.max_columns', 10)

# 2. Membaca dan Memuat Dataset Worldbank dari Source URL
# Menggunakan encoding 'cp1252' untuk menangani karakter khusus pada teks
url = 'https://googleapis.com'
dataset_worldbank = pd.read_csv(url, delimiter=',', encoding='cp1252')

# 3. Inspeksi Awal Struktur dan Tipe Data Dataset
print('\nInformasi dataset_worldbank:')
print('============================')
dataset_worldbank.info()

# 4. Data Cleansing: Mengisi Baris Data Kosong (Missing Values) dengan Angka 0
dataset_worldbank = dataset_worldbank.fillna(0)

# 5. Verifikasi Hasil Pembersihan Data
print('\nInformasi dataset_worldbank setelah .fillna(0):')
print('==============================================')
dataset_worldbank.info()

# 6. Eksplorasi Dimensi Waktu: Melihat Cakupan Tahun yang Tersedia
print('\nData worldbank dari tahun ... sampai tahun ...')
print('=============================================')
print(dataset_worldbank['year'].unique())
