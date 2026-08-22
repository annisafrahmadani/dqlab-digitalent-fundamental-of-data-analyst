-- ====================================================================
-- PROJECT: RETAIL SALES PERFORMANCE REPORT - OVERALL PERFORMANCE BY YEAR
-- MODUL: Project Data Analysis for Retail (Bab 8)
-- Skenario kasus oleh: DQLab x Digitalent Komdigi
-- ====================================================================

SELECT 
    YEAR(order_date) AS years,               -- Mengekstrak tahun dari kolom tanggal transaksi
    SUM(sales) AS sales,                     -- Menjumlahkan seluruh nominal penjualan (omset tahunan)
    COUNT(order_id) AS number_of_order       -- Menghitung total banyaknya nota order yang masuk
FROM dqlab_sales_store
WHERE order_status = 'Order Finished'        -- KUNCI UTAMA: Filter hanya transaksi yang selesai/sukses
GROUP BY YEAR(order_date)                    -- Mengelompokkan data berdasarkan tahun
ORDER BY years ASC;                          -- Mengurutkan dari tahun tertua ke terbaru
