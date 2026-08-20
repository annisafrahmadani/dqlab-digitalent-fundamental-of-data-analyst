-- ====================================================================
-- PROJECT: B2B RETAIL CUSTOMER ANALYTICS - SALES & REVENUE COMPARISON
-- MODUL: Project Data Analysis for B2B Retail (Bab 7)
-- Skenario kasus oleh: DQLab x Digitalent Komdigi
-- ====================================================================

-- 1. ANALISIS PERIODE 1: Menghitung total volume penjualan & revenue dari tabel orders_1
SELECT 
    SUM(quantity) AS total_penjualan,
    SUM(quantity * priceEach) AS revenue -- Operasi kalkulasi nilai total transaksi finansial bersih
FROM orders_1
WHERE status = 'shipped'; -- Menyaring data pesanan yang sukses terkirim saja


-- 2. ANALISIS PERIODE 2: Menghitung total volume penjualan & revenue dari tabel orders_2
SELECT 
    SUM(quantity) AS total_penjualan,
    SUM(quantity * priceEach) AS revenue -- Operasi kalkulasi nilai total transaksi finansial bersih
FROM orders_2
WHERE status = 'shipped'; -- Menyaring data pesanan yang sukses terkirim saja
