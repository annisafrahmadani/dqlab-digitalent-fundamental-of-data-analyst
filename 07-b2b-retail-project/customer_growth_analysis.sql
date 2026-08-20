-- ====================================================================
-- PROJECT: B2B RETAIL CUSTOMER ANALYTICS - CUSTOMER GROWTH ANALYSIS
-- MODUL: Project Data Analysis for B2B Retail (Bab 7)
-- Skenario kasus oleh: DQLab x Digitalent Komdigi
-- ====================================================================

SELECT 
    quarter,
    COUNT(DISTINCT customerID) AS total_customers -- Menghitung total pelanggan unik yang mendaftar per kuartal
FROM (
    -- Langkah 1 & 2: Subquery untuk mengambil data profil customer baru
    SELECT 
        customerID,
        createDate,
        QUARTER(createDate) AS quarter -- Mengekstrak angka kuartal dari tanggal pembuatan akun
    FROM customer
    -- Filter rentang pendaftaran dari 1 Januari 2004 hingga 30 Juni 2004
    WHERE createDate BETWEEN '2004-01-01' AND '2004-06-30'
) AS tabel_b
-- Langkah 3: Mengelompokkan hasil agregat berdasarkan kolom "quarter"
GROUP BY quarter;
