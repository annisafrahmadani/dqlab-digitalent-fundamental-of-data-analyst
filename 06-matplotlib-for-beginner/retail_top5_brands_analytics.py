# ====================================================================
# PROJECT: 7 CASE STUDI KASUS BISNIS - RETAIL TOP 5 BRANDS ANALYTICS
# MODUL: Data Visualization with Python Matplotlib for Beginner (Bab 6)
# Skenario kasus oleh: DQLab x Digitalent Komdigi
# ====================================================================

import datetime
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------------------------
# PREPARATION: Data Loading & Base Feature Engineering
# --------------------------------------------------------------------
url = 'https://googleapis.com'
dataset = pd.read_csv(url)

# Ekstraksi kolom format tahun-bulan (order_month)
dataset['order_month'] = dataset['order_date'].apply(
    lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').strftime('%Y-%m')
)

# Kalkulasi metrik bisnis Gross Merchandise Volume (GMV)
dataset['gmv'] = dataset['item_price'] * dataset['quantity']


# --------------------------------------------------------------------
# CASE 1: Menentukan Top 5 Brands Berdasarkan Volume Penjualan (Quantity)
# --------------------------------------------------------------------
# Mengambil informasi top 5 brands berdasarkan total quantity di bulan Desember 2019
top_brands = (dataset[dataset['order_month'] == '2019-12']
              .groupby('brand')['quantity']
              .sum()
              .reset_index()
              .sort_values(by='quantity', ascending=False)
              .head(5)
             )

# Membuat DataFrame baru yang mengisolasi transaksi bulan Desember 2019 HANYA untuk top 5 brands di atas
dataset_top5brand_dec = dataset[
    (dataset['order_month'] == '2019-12') & 
    (dataset['brand'].isin(top_brands['brand'].to_list()))
]

# Output verifikasi ke konsol untuk memastikan data top 5 brands terekstrak sempurna
print("[INFO] Top 5 Brands di Bulan Desember 2019:")
print(top_brands)
