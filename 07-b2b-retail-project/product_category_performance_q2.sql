-- ====================================================================
-- PROJECT: B2B RETAIL CUSTOMER ANALYTICS - PRODUCT CATEGORY PERFORMANCE (Q2)
-- MODUL: Project Data Analysis for B2B Retail (Bab 7)
-- Skenario kasus oleh: DQLab x Digitalent Komdigi
-- ====================================================================

-- 5. Menggunakan SELECT * di bagian paling luar untuk mengambil kolom dari subquery di bawahnya
SELECT * FROM (
    SELECT 
        categoryID,
        COUNT(DISTINCT orderNumber) AS total_order,
        SUM(quantity) AS total_penjualan
    FROM (
        -- 2. LEFT() diletakkan di dalam subquery ini bersama kolom productCode, orderNumber, dll.
        SELECT 
            productCode,
            orderNumber,
            quantity,
            status,
            LEFT(productCode, 3) AS categoryID -- Mengambil 3 karakter pertama dari kode produk sebagai ID Kategori
        FROM orders_2
        -- 3. Menggunakan tanda petik ganda ("Shipped") sesuai kode jawaban
        WHERE status = "Shipped"
    ) AS tabel_c
    GROUP BY categoryID
) AS tabel_b
-- 4. Mengurutkan berdasarkan total_order DAN total_penjualan dari terbesar ke terkecil (DESC)
ORDER BY total_order DESC, total_penjualan DESC;
