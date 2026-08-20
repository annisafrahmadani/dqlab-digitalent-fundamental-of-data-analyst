# ====================================================================
# CASE 6a: ANALISIS KORELASI ANTARA QUANTITY VS GMV (SCATTER PLOT)
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
dataset_top5brand_dec_per_product = (dataset_top5brand_dec
                                     .groupby('product_id')
                                     .agg({'quantity': 'sum', 'gmv': 'sum', 'item_price': 'median'})
                                     .reset_index()
                                    )

# 4. Inisialisasi Ukuran Kanvas Grafik Scatter Plot
plt.figure(figsize=(10, 8))

# 5. Merender Grafik Diagram Sebar (Scatter Plot - Case 6a)
plt.scatter(dataset_top5brand_dec_per_product['quantity'], 
            dataset_top5brand_dec_per_product['gmv'], 
            marker='+', color='red')

# 6. Konfigurasi Elemen Visual & Pembatasan Skala Grafik
plt.title('Correlation of Quantity vs GMV per Product\nTop 5 Brands in Dec 2019', loc='center', pad=20, fontsize=15, color='blue')
plt.xlabel('Quantity', fontsize=12)
plt.ylabel('GMV (in Millions)', fontsize=12)

# Mengunci batas tampilan sumbu X dan Y agar fokus pada data cluster utama
plt.xlim(xmin=0, xmax=300)
plt.ylim(ymin=0, ymax=200000000)

# 7. Tampilkan Grafik
plt.show()
