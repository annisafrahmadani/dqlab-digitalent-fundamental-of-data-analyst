-- ====================================================================
-- PROJECT: ANALISIS DATA TRANSAKSI - PROYEK DARI CABANG A
-- MODUL: Fundamental SQL using SELECT Statement
-- ====================================================================

-- Mengambil data pelanggan dan melakukan kalkulasi total revenue
SELECT 
    kode_pelanggan, 
    nama_produk, 
    qty, 
    harga, 
    (qty * harga) AS total -- Kalkulasi aritmatika untuk mendapatkan total pendapatan per baris transaksi
FROM tr_penjualan
-- Menyaring hasil kalkulasi alias menggunakan HAVING untuk performa transaksi >= IDR 100.000
HAVING total >= 100000
-- Mengurutkan hasil analisis secara menurun (descending) dari nilai transaksi terbesar
ORDER BY total DESC;
