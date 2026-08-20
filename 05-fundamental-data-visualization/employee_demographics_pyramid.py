# ====================================================================
# PROJECT: DEMOGRAFI KARYAWAN - POPULATION PYRAMID CHART
# MODUL: Fundamental Data Visualization with Python (Bab 5)
# Skenario kasus oleh: DQLab x Digitalent Komdigi
# ====================================================================

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Dataset Demografi & Mengurutkan Berdasarkan Kelompok Usia
url = "https://googleapis.com"
tabel = (pd.read_csv(url)
         .sort_values("Kelompok Usia", ascending=False)
         .set_index("Kelompok Usia")
        )

# 2. Trik Transformasi Nilai Negatif untuk Membuat Efek Sumbu Kiri Piramida
tabel["Laki-laki"] = -tabel["Laki-laki"]

# 3. Inisialisasi Subplots Dua Grafik yang Berdampingan (1 Baris, 2 Kolom)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Menambahkan Judul Utama Grafik (Super Title)
fig.suptitle("Perbandingan Jumlah Karyawan Laki-laki dan Perempuan\nBerdasarkan Kelompok Usia",
             x=0.0, y=1.0, fontsize=24, fontweight="bold", ha="left")

# 4. Merender Grafik Batang Horizontal Laki-laki (Sumbu Kiri)
tabel["Laki-laki"].plot(kind="barh", ax=axes[0], color="tab:blue", xlim=[-550, 0])
axes[0].set_ylabel("")
axes[0].tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
axes[0].legend(["Laki-laki"], fontsize=14, bbox_to_anchor=(0., 0., 1., .05))
axes[0].set_frame_on(False)

# 5. Merender Grafik Batang Horizontal Perempuan (Sumbu Kanan)
tabel["Perempuan"].plot(kind="barh", ax=axes[1], color="tab:orange", xlim=[0, 550])
axes[1].set_ylabel("")
axes[1].tick_params(left=False, bottom=False, labelbottom=False)
axes[1].legend(["Perempuan"], fontsize=14, bbox_to_anchor=(0., 0., 0.3, .05))
axes[1].set_frame_on(False)

# 6. Menambahkan Anotasi Teks Angka Mutlak (Data Labels) di Dalam Batang Grafik
for i, m, w in zip(range(tabel.shape[0]), list(tabel["Laki-laki"]), list(tabel["Perempuan"])):
    # Anotasi angka untuk data Laki-laki (Menggunakan nilai mutlak 'abs' agar tanda minus hilang)
    axes[0].annotate(str(abs(m)), (m+20, i), xytext=(m+20, i),
                     color="w", va="center", ha="center", fontsize=14)
    
    # Anotasi angka untuk data Perempuan
    axes[1].annotate(str(abs(w)), (w-20, i), xytext=(w-20, i),
                     color="w", va="center", ha="center", fontsize=14)

# 7. Render & Tampilkan Grafik Piramida
plt.tight_layout(rect=(0, 0, 1, 0.88))
plt.show()
