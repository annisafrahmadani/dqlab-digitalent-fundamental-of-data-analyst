# ====================================================================
# CASE 4: ANALISIS SEGMENTASI PRODUK BERDASARKAN KUANTITAS TERJUAL
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

# 3. Membuat Agregasi Kuantitas Penjualan per Product ID dan Brand
dataset_top5brand_dec_per_product = (dataset_top5brand_dec
                                     .groupby(['product_id', 'brand'])['quantity']
                                     .sum()
                                     .reset_index()
                                    )

# 4. Feature Engineering: Membuat Kolom Klasifikasi Penjualan (>= 100 dan < 100)
dataset_top5brand_dec_per_product['quantity_group'] = dataset_top5brand_dec_per_product['quantity'].apply(
    lambda x: '>= 100' if x >= 100 else '< 100'
)
dataset_top5brand_dec_per_product.sort_values('quantity', ascending=False, inplace=True)

# 5. Membuat Referensi Pengurutan Brand Berdasarkan Ragam Produk Terbanyak
s_sort = dataset_top5brand_dec_per_product.groupby('brand')['product_id'].nunique().sort_values(ascending=False)

# 6. Merender Grafik Batang Bertumpuk (Stacked Bar Chart - Case 4)
(dataset_top5brand_dec_per_product
 .groupby(['brand', 'quantity_group'])['product_id']
 .nunique()
 .reindex(index=s_sort.index, level='brand')
 .unstack()
 .plot(kind='bar', stacked=True)
)

# 7. Konfigurasi Elemen Visual Grafik
plt.title('Number of Sold Products per Brand, December 2019', loc='center', pad=30, fontsize=15, color='blue')
plt.xlabel('Brand', fontsize=15)
plt.ylabel('Number of Products', fontsize=15)
plt.ylim(ymin=0)
plt.xticks(rotation=0)

# 8. Tampilkan Grafik
plt.show()
