# ====================================================================
# CASE 5: ANALISIS DISTRIBUSI HARGA PRODUK (PRICING STRATEGY)
# MODUL: Data Visualization with Python Matplotlib for Beginner (Bab 6)
# Skenario kasus oleh: DQLab x Digitalent Komdigi
# ====================================================================

import datetime
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Dataset & Base Feature Engineering
url = 'https://googleapis.com'
dataset = pd.read_csv(url)

dataset['order_month'] = dataset['order_date'].apply(
    lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').strftime('%Y-%m')
)

# 2. Filter Top 5 Brands Berdasarkan Volume Penjualan Desember 2019
top_brands = (dataset[dataset['order_month'] == '2019-12']
              .groupby('brand')['quantity']
              .sum()
              .reset_index()
              .sort_values(by='quantity', ascending=False)
              .head(5)
             )

dataset_top5brand_dec = dataset[
    (dataset['order_month'] == '2019-12') & 
    (dataset['brand'].isin(top_brands['brand'].to_list()))
]

# 3. Inisialisasi Ukuran Kanvas Grafik
plt.figure(figsize=(10, 5))

# 4. Merender Grafik Histogram Sebaran Nilai Tengah Harga Produk (Case 5)
plt.hist(dataset_top5brand_dec.groupby('product_id')['item_price'].median(), 
         bins=10, stacked=True, range=(1, 2000000), color='green')

# 5. Konfigurasi Elemen Visual & Label Grafik
plt.title('Distribution of Price Median per Product\nTop 5 Brands in Dec 2019', loc='center', pad=15, fontsize=15, color='blue')
plt.xlabel('Price Median', fontsize=12)
plt.ylabel('Number of Products', fontsize=12)

# Mengunci batas sumbu X dari angka 0 hingga maksimal 2.000.000
plt.xlim(xmin=0, xmax=2000000)

# 6. Tampilkan Grafik
plt.show()
