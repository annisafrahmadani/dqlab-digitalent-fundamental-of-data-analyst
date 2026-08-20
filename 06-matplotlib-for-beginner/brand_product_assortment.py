# ====================================================================
# CASE 3: ANALISIS RAGAM PRODUK (PRODUCT ASSORTMENT) PER BRAND
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

# 3. Merender Grafik Batang Ragam Produk (Bar Chart - Case 3)
plt.clf()
dataset_top5brand_dec.groupby('brand')['product_id'].nunique().sort_values(ascending=False).plot(
    kind='bar', color='green'
)

# 4. Konfigurasi Elemen Visual & Label Sumbu
plt.title('Number of Sold Products per Brand, December 2019', loc='center', pad=30, fontsize=15, color='blue')
plt.xlabel('Brand', fontsize=15)
plt.ylabel('Number of Products', fontsize=15)
plt.ylim(ymin=0)
plt.xticks(rotation=0)

# 5. Tampilkan Grafik
plt.show()
