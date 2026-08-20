# ====================================================================
# CASE 6b: ANALISIS KORELASI ANTARA MEDIAN HARGA VS QUANTITY (SCATTER PLOT)
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

# Kalkulasi metrik bisnis Gross Merchandise Volume (GMV)
dataset['gmv'] = dataset['item_price'] * dataset['quantity']

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

# 3. Agregasi Data Finansial Tingkat Lanjut per Product ID
data_per_product_top5brand_dec = (dataset_top5brand_dec
                                  .groupby('product_id')
                                  .agg({'quantity': 'sum', 'gmv': 'sum', 'item_price': 'median'})
                                  .reset_index()
                                 )

# 4. Inisialisasi Ukuran Kanvas Grafik Scatter Plot
plt.clf()
plt.figure(figsize=(10, 8))

# 5. Merender Grafik Diagram Sebar (Scatter Plot - Case 6b)
plt.scatter(data_per_product_top5brand_dec['item_price'], 
            data_per_product_top5brand_dec['quantity'], 
            marker='o', color='green')

# 6. Konfigurasi Elemen Visual & Pembatasan Skala Grafik
plt.title('Correlation of Quantity and GMV per Product\nTop 5 Brands in December 2019', loc='center', fontsize=15, color='blue')
plt.xlabel('Price Median', fontsize=12)
plt.ylabel('Quantity', fontsize=12)

# Mengunci batas tampilan sumbu X dan Y agar fokus pada kluster utama
plt.xlim(xmin=0, xmax=2000000)
plt.ylim(ymin=0, ymax=250)

# 7. Tampilkan Grafik
plt.show()
