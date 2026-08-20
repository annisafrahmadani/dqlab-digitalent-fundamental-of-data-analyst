-- ====================================================================
-- PROJECT: RETAIL SALES PERFORMANCE REPORT - PERFORMANCE BY PRODUCT SUB CATEGORY
-- MODUL: Project Data Analysis for Retail (Bab 8)
-- Skenario kasus oleh: DQLab x Digitalent Komdigi
-- ====================================================================

SELECT 
    YEAR(order_date) AS years,
    product_sub_category,
    SUM(sales) AS sales
FROM dqlab_sales_store
WHERE order_status = 'Order Finished'
  AND YEAR(order_date) BETWEEN 2011 AND 2012 -- Membatasi analisis perbandingan hanya pada rentang tahun 2011 dan 2012
GROUP BY 
    YEAR(order_date),
    product_sub_category
ORDER BY 
    years ASC,
    sales DESC; -- Mengurutkan dari omset penjualan terbesar ke terkecil per tahunnya
