# ====================================================================
# PROJECT: EXPLORATORY DATA ANALYSIS (EDA) ORDER DATASET
# MODUL: Exploratory Data Analysis with Python for Beginner
# Skenario kasus oleh: DQLab x Digitalent Komdigi
# ====================================================================

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Dataset dari URL Source
order_df = pd.read_csv("https://googleapis.com")

# 2. Analisis Median Harga Berdasarkan Metode Pembayaran (payment_type)
median_price = order_df["price"].groupby(order_df["payment_type"]).median()
print("[INFO] Median harga per metode pembayaran:")
print(median_price)
print("-" * 50)

# 3. Data Cleansing: Mengubah Nama Kolom & Analisis Biaya Pengiriman Termahal
order_df.rename(columns={"freight_value": "shipping_cost"}, inplace=True)
sort_value = order_df.sort_values(by="shipping_cost", ascending=False)
print("[INFO] Data penjualan diurutkan berdasarkan biaya pengiriman termahal:")
print(sort_value.head())
print("-" * 50)

# 4. Analisis Rataan dan Standar Deviasi Berat Produk (product_weight_gram) Per Kategori
mean_value = order_df["product_weight_gram"].groupby(order_df["product_category_name"]).mean()
print("[INFO] Rata-rata berat produk per kategori:")
print(mean_value)
print("-" * 50)

std_value = order_df["product_weight_gram"].groupby(order_df["product_category_name"]).std()
print("[INFO] Standar deviasi berat produk per kategori (diurutkan terkecil):")
print(std_value.sort_values())
print("-" * 50)

# 5. Visualisasi Data: Distribusi Kuantitas Penjualan (Histogram)
print("[INFO] Menampilkan grafik histogram persebaran quantity...")
order_df[["quantity"]].hist(figsize=(4, 5), bins=5)
plt.title("Distribusi Kuantitas Penjualan")
plt.xlabel("Quantity")
plt.ylabel("Frekuensi")
plt.tight_layout()
plt.show()
