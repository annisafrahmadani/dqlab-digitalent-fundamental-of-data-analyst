-- ====================================================================
-- PROJECT: DATA RELATION & COMBINATION (INNER JOIN & UNION)
-- SUB-MODUL: Fundamental SQL using INNER JOIN & UNION
-- ====================================================================

-- 1. PROJECT INNER JOIN: Menghubungkan tabel master pelanggan dan transaksi
-- Menyaring pelanggan unik yang membeli produk spesifik (Kotak Pensil, Flashdisk, & Sticky Notes)
SELECT DISTINCT 
    ms_pelanggan.kode_pelanggan, 
    ms_pelanggan.nama_customer, 
    ms_pelanggan.alamat
FROM ms_pelanggan
INNER JOIN tr_penjualan 
    ON ms_pelanggan.kode_pelanggan = tr_penjualan.kode_pelanggan
WHERE tr_penjualan.nama_produk IN (
    'Kotak Pensil DQLab', 
    'Flashdisk DQLab 32 GB', 
    'Sticky Notes DQLab 500 sheets'
);


-- 2. PROJECT UNION: Menggabungkan dua tabel produk dari cabang berbeda
-- Menampilkan produk dari ms_produk_1 dan ms_produk_2 yang memiliki harga di bawah 100.000
SELECT nama_produk, kode_produk, harga 
FROM ms_produk_1
WHERE harga < 100000

UNION

SELECT nama_produk, kode_produk, harga 
FROM ms_produk_2
WHERE harga < 100000;
