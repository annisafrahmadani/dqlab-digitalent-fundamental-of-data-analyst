-- ====================================================================
-- PROJECT: ANALISIS PENJUALAN (PART 1 & PART 2)
-- SUB-MODUL: SQL Function, CASE WHEN, & GROUP BY
-- ====================================================================

-- 1. Menghitung total jumlah seluruh penjualan (total/revenue)
SELECT SUM(total) AS total 
FROM tr_penjualan;

-- 2. Menghitung total quantity seluruh produk yang terjual
SELECT SUM(qty) AS qty 
FROM tr_penjualan;

-- 3. Menghitung total quantity dan total revenue untuk setiap kode produk
SELECT kode_produk, SUM(qty) AS qty, SUM(total) AS total 
FROM tr_penjualan
GROUP BY kode_produk;

-- 4. Menghitung rata-rata total belanja per kode pelanggan
SELECT kode_pelanggan, AVG(total) AS avg_total 
FROM tr_penjualan
GROUP BY kode_pelanggan;

-- 5. Klasifikasi tingkat transaksi ke dalam 3 kategori: High, Medium, Low
SELECT 
    kode_transaksi, 
    kode_pelanggan, 
    no_urut, 
    kode_produk, 
    nama_produk, 
    qty, 
    total,
    CASE 
        WHEN total > 300000 THEN 'High'
        WHEN total < 100000 THEN 'Low'
        ELSE 'Medium'
    END AS kategori
FROM tr_penjualan;
