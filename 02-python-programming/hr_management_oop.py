# ====================================================================
# PROJECT: SISTEM MANAJEMEN SDM & HR PERUSAHAAN (OOP-BASED)
# MODUL: Python for Professional Data Beginner - Part 3
# Skenario kasus oleh: DQLab x Digitalent Komdigi
# ====================================================================

# --------------------------------------------------------------------
# A. STRUKTUR HIERARKI KELAS KARYAWAN (INHERITANCE & POLYMORPHISM)
# --------------------------------------------------------------------

# 1. Definisikan kelas Karyawan sebagai Parent Class
class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.self_pendapatan_tambahan = 0
        self.self_insentif_lembur = insentif_lembur
        
    def lembur(self):
        self.self_pendapatan_tambahan += self.self_insentif_lembur
        
    def tambahan_proyek(self, jumlah_tambahan):
        self.self_pendapatan_tambahan += jumlah_tambahan
        
    def total_pendapatan(self):
        return self.pendapatan + self.self_pendapatan_tambahan


# 2. Definisikan kelas TenagaLepas sebagai Child Class dari Karyawan
class TenagaLepas(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan, 0)
        
    def tambahan_proyek(self, nilai_proyek):
        self.self_pendapatan_tambahan += nilai_proyek * 0.01


# 3. Definisikan kelas AnalisData sebagai Child Class dari Karyawan
class AnalisData(Karyawan):
    def __init__(self, nama, usia=21, pendapatan=6500000, insentif_lembur=100000):
        super().__init__(nama, usia, pendapatan, insentif_lembur)


# 4. Definisikan kelas IlmuwanData sebagai Child Class dari Karyawan
class IlmuwanData(Karyawan):
    def __init__(self, nama, usia=25, pendapatan=12000000, insentif_lembur=150000):
        super().__init__(nama, usia, pendapatan, insentif_lembur)
        
    def tambahan_proyek(self, nilai_proyek):
        self.self_pendapatan_tambahan += 0.1 * nilai_proyek


# 5. Definisikan kelas PembersihData sebagai Child Class dari TenagaLepas
class PembersihData(TenagaLepas):
    def __init__(self, nama, usia, pendapatan=4000000):
        super().__init__(nama, usia, pendapatan)


# 6. Definisikan kelas DokumenterTeknis sebagai Child Class dari TenagaLepas
class DokumenterTeknis(TenagaLepas):
    def __init__(self, nama, usia, pendapatan=2500000):
        super().__init__(nama, usia, pendapatan)


# --------------------------------------------------------------------
# B. STRUKTUR KELAS UTAMA PERUSAHAAN (SISTEM MANAJEMEN AKUN)
# --------------------------------------------------------------------

class Perusahaan:
    def __init__(self, nama, alamat, nomor_telepon):
        self.nama = nama
        self.alamat = alamat
        self.nomor_telepon = nomor_telepon
        self.list_karyawan = []
        
    def aktifkan_karyawan(self, karyawan):
        self.list_karyawan.append(karyawan)
        
    def nonaktifkan_karyawan(self, nama_karyawan):
        karyawan_nonaktif = None
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan:
                karyawan_nonaktif = karyawan
                break
        if karyawan_nonaktif is not None:
            self.list_karyawan.remove(karyawan_nonaktif)
            
    def total_pengeluaran(self):
        pengeluaran = 0
        for karyawan in self.list_karyawan:
            pengeluaran += karyawan.total_pendapatan()
        return pengeluaran
        
    def cari_karyawan(self, nama_karyawan):
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan:
                return karyawan
        return None


# --------------------------------------------------------------------
# C. EKSEKUSI PIPELINE & INSTANSIASI OBJEK DATA
# --------------------------------------------------------------------

# Create object Karyawan sesuai dengan tugasnya masing-masing
ani = PembersihData('Ani', 25)
budi = DokumenterTeknis('Budi', 18)
cici = IlmuwanData('Cici')
didi = IlmuwanData('Didi', 32, 20000000)
efi = AnalisData('Efi')
febi = AnalisData('Febi', 28, 12000000)

# Create object perusahaan
perusahaan = Perusahaan('ABC', 'Jl. Jendral Sudirman, Blok 11', '(021) 95812XX')

# Aktifkan setiap karyawan yang telah di-inisialisasi
perusahaan.aktifkan_karyawan(ani)
perusahaan.aktifkan_karyawan(budi)
perusahaan.aktifkan_karyawan(cici)
perusahaan.aktifkan_karyawan(didi)
perusahaan.aktifkan_karyawan(efi)
perusahaan.aktifkan_karyawan(febi)

# Cetak keseluruhan total pengeluaran perusahaan
print(f"Total pengeluaran payroll bulanan perusahaan: IDR {perusahaan.total_pengeluaran():,}")
