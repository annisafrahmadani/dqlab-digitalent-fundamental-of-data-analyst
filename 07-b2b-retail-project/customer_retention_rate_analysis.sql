-- ====================================================================
-- PROJECT: B2B RETAIL CUSTOMER ANALYTICS - CUSTOMER RETENTION RATE ANALYSIS
-- MODUL: Project Data Analysis for B2B Retail (Bab 7)
-- Skenario kasus oleh: DQLab x Digitalent Komdigi
-- ====================================================================

-- #Menghitung total unik customers yang transaksi di quarter_1
SELECT COUNT(DISTINCT customerID) as total_customers FROM orders_1;


-- Langkah 4: Menghitung persentase retensi pembeli dan memberi nama "Q2"
SELECT 
    "1" AS quarter,
    (COUNT(DISTINCT customerID) / 25) * 100 AS Q2 -- Menghitung rasio pelanggan yang melakukan pembelian berulang (repeat order)
FROM orders_1
-- Langkah 3: Filter menggunakan operator IN() dari subquery Langkah 2
WHERE customerID IN (
    -- Langkah 2: Mengambil customerID unik (DISTINCT) dari tabel orders_2 untuk validasi keaktifan
    SELECT DISTINCT customerID 
    FROM orders_2
);
