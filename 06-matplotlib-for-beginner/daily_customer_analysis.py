# ====================================================================
# PROJECT: E-COMMERCE DAILY CUSTOMER & GMV ANALYSIS (PART 1)
# MODUL: Data Visualization with Python Matplotlib for Beginner (Bab 6)
# Skenario kasus oleh: DQLab x Digitalent Komdigi
# ====================================================================

import datetime
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Dataset Transaksi Retail Terkompresi (Reduced Dataset)
url = 'https://googleapis.com'
dataset = pd.read_csv(url)

# 2. Feature Engineering: Ekstraksi Format Tahun-Bulan (order_month)
dataset['order_month'] = dataset['order_date'].apply(
    lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').strftime('%Y-%m')
)

# 3. Metrik Bisnis: Kalkulasi Gross Merchandise Volume (GMV) per Baris Transaksi
dataset['gmv'] = dataset['item_price'] * dataset['quantity']

# 4. Inisialisasi Kanvas Grafik & Agregasi Tren Pelanggan Harian Bulan Desember 2019
plt.figure(figsize=(10, 5))
dataset[dataset['order_month'] == '2019-12'].groupby(['order_date'])['customer_id'].nunique().plot(
    color='red', marker='.', linewidth=2
)

# 5. Konfigurasi Elemen Visual & Tipografi Grafik (Aesthetic Styling)
plt.title('Daily Number of Customers - December 2019', loc='left', pad=20, fontsize=20, color='orange')
plt.xlabel('Order Date', fontsize=15, color='blue')
plt.ylabel('Number of Customers', fontsize=15, color='blue')

# Menambahkan garis bantu kotak (Grid) dengan tipe putus-putus halus
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)

# Mengunci batas bawah sumbu Y agar dimulai tepat dari angka 0
plt.ylim(ymin=0)

# 6. Render & Tampilkan Grafik Line Chart
plt.show()
