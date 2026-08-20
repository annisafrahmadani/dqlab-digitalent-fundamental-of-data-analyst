-- ====================================================================
-- PROJECT: B2B RETAIL CUSTOMER ANALYTICS - QUARTERLY PERFORMANCE ANALYSIS
-- MODUL: Project Data Analysis for B2B Retail (Bab 7)
-- Skenario kasus oleh: DQLab x Digitalent Komdigi
-- ====================================================================

SELECT 
    quarter,
    SUM(quantity) AS total_penjualan,
    SUM(quantity * priceEach) AS revenue -- Menghitung total omset pendapatan per kuartal
FROM (
    -- Langkah 1: Mengambil data orders_1 dan menandainya sebagai quarter = 1
    SELECT orderNumber, status, quantity, priceEach, 1 AS quarter
    FROM orders_1
    
    UNION ALL
    
    -- Langkah 2: Mengambil data orders_2 dan menandainya sebagai quarter = 2
    SELECT orderNumber, status, quantity, priceEach, 2 AS quarter
    FROM orders_2
) AS tabel_a
-- Langkah 3: Memfilter data hasil penggabungan agar hanya mengambil status "Shipped"
WHERE status = 'Shipped'
-- Langkah 4: Mengelompokkan hasil agregat berdasarkan kolom "quarter"
GROUP BY quarter;
