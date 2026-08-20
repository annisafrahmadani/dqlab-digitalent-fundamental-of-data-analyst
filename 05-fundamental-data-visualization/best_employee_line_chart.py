# ====================================================================
# PROJECT: ANALISIS PRODUKTIVITAS - BEST EMPLOYEE HIGHLIGHT CHART
# MODUL: Fundamental Data Visualization with Python (Bab 5)
# Skenario kasus oleh: DQLab x Digitalent Komdigi
# ====================================================================

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Dataset Produktivitas Karyawan & Skala Ribuan
url = "https://googleapis.com"
tabel = pd.read_csv(url, index_col="Bulan") / 1000

# 2. Inisialisasi Kanvas Grafik (1 Baris, 1 Kolom)
fig, ax = plt.subplots(1, 1, figsize=(12, 6))

# Menambahkan Judul Utama (Super Title) dan Sub-Judul Grafik
fig.suptitle("Best Employee 2019", x=0.01, y=0.95, fontsize=24, fontweight="bold", ha="left")
ax.set_title("Lima karyawan dengan produktivitas tertinggi\n", fontsize=18, ha="right")

# 3. Kustomisasi Warna & Ketebalan Garis Spesifik (Highlight Karyawan E / Karyawan ke-5)
colors = ["tab:gray", "tab:gray", "tab:gray", "tab:gray", "darkblue"]
line_widths = [1.5, 2, 1, 2.5, 3.]

# Merender Line Chart
lp = tabel.plot(kind="line", ax=ax, xlim=[0, 11], ylim=[10, 40], color=colors,
                xticks=range(tabel.shape[0]), yticks=[10, 20, 30, 40])

# 4. Iterasi Dinamis untuk Mengatur Ketebalan & Anotasi Label Garis di Bulan Desember
add_lbl_pos = [0.3, 0.5, 1.2, -1.0, 0.5]
add_avg_pos = [-0.7, -0.5, 0.2, -2.0, -0.5]

for i, item in enumerate(lp.get_lines()):
    item.set_linewidth(line_widths[i])
    lbl = item.get_label()
    
    # Anotasi Nama Karyawan di Ujung Garis (Bulan Desember / Indeks ke-11)
    ax.annotate(lbl, (11, tabel.loc["Desember", lbl]),
                (11.2, tabel.loc["Desember", lbl] + add_lbl_pos[i]),
                fontweight="bold", fontsize=12, color=colors[i], va="center",
                arrowprops={"arrowstyle": "-", "color": colors[i]})
    
    # Anotasi Nilai Rata-rata Karyawan di Ujung Garis
    ax.annotate("(avg: %.4f)" % tabel[lbl].mean(), (11, tabel.loc["Desember", lbl]),
                (11.2, tabel.loc["Desember", lbl] + add_avg_pos[i]),
                fontsize=11, color=colors[i], va="center")

# 5. Menambahkan Anotasi Puncak Produktivitas Tertinggi (Karyawan E)
highest_prod = tabel["Karyawan E"].max()
ax.annotate("Produktivitas\ntertinggi\n%.4f" % highest_prod,
            (8, highest_prod), (7.75, highest_prod + 1.5),
            ha="left", color=colors[-1], arrowprops={"arrowstyle": "-", "color": colors[-1]})

# 6. Formatting Sumbu X, Sumbu Y, dan Label
ax.set_xticklabels([item[:3] for item in tabel.index], fontsize=12)
ax.set_yticklabels([str(i) for i in [10, 20, 30, 40]], fontsize=12)
ax.set_xlabel("")
ax.set_ylabel("Jumlah produk (ribuan)\n", fontsize=14)

# 7. Chart Junk Removal: Membuang Bingkai Atas, Kanan, dan Bawah Grafik
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_color("none")

# Menghapus legenda bawaan karena sudah digantikan oleh anotasi langsung
ax.get_legend().remove()

# 8. Render & Tampilkan Grafik Bersih
plt.tight_layout(rect=(0, 0, 1, 0.90))
plt.show()
