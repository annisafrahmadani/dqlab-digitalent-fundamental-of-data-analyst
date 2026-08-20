# ====================================================================
# PROJECT: KALKULASI PENGELUARAN EKSPEDISI (GANJIL-GENAP)
# MODUL: Python for Professional Data Beginner - Part 1
# Skenario kasus oleh: DQLab x Digitalent Komdigi
# ====================================================================

# 1. Inisialisasi Data Dasar Finansial & Operasional
uang_jalan = 1500000
jumlah_hari = 31
list_plat_nomor = [8993, 2198, 2501, 2735, 3772, 4837, 9152]

# 2. Kategorisasi Kendaraan Berdasarkan Pelat Ganjil / Genap
kendaraan_genap = 0
kendaraan_ganjil = 0

for plat_nomor in list_plat_nomor:
    if plat_nomor % 2 == 0:
        kendaraan_genap += 1
    else:
        kendaraan_ganjil += 1

# 3. Simulasi Kalkulasi Total Pengeluaran Berdasarkan Hari Kalender
i = 1
total_pengeluaran = 0

while i <= jumlah_hari:
    # Jika hari genap, kendaraan berpelat genap yang beroperasi
    if i % 2 == 0:
        total_pengeluaran += (kendaraan_genap * uang_jalan)
    # Jika hari ganjil, kendaraan berpelat ganjil yang beroperasi
    else:
        total_pengeluaran += (kendaraan_ganjil * uang_jalan)
    i += 1

# 4. Output Hasil Analisis Pengeluaran
print(f"Total pengeluaran operasional ekspedisi selama {jumlah_hari} hari: IDR {total_pengeluaran:,}")
# Output Konsol: 163,500,000
