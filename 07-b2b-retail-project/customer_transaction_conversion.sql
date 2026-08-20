-- ====================================================================
-- PROJECT: B2B RETAIL CUSTOMER ANALYTICS - CUSTOMER TRANSACTION CONVERSION
-- MODUL: Project Data Analysis for B2B Retail (Bab 7)
-- Skenario kasus oleh: DQLab x Digitalent Komdigi
-- ====================================================================

SELECT 
    quarter,
    COUNT(DISTINCT customerID) AS total_customers -- Menghitung pelanggan baru yang terkonversi menjadi pembeli aktif
FROM (
    -- Langkah A, B, & 3: Ambil kolom & buat subquery tabel_b untuk profil pendaftaran
    SELECT 
        customerID,
        createDate,
        QUARTER(createDate) AS quarter
    FROM customer
    WHERE createDate BETWEEN '2004-01-01' AND '2004-06-30'
) AS tabel_b
-- Langkah 5: Filter menggunakan operator IN() untuk memvalidasi riwayat transaksi
WHERE customerID IN (
    -- Langkah 4: Gabungkan customerID dari orders_1 dan orders_2 pakai UNION untuk daftar pembeli unik
    SELECT DISTINCT customerID FROM orders_1
    UNION
    SELECT DISTINCT customerID FROM orders_2
)
-- Langkah 7: Kelompokkan hasil agregat berdasarkan kolom quarter
GROUP BY quarter;
