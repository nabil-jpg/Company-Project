from company import Perusahaan, AnalisData, IlmuwanData, TenagaLepas
from db_connection import insert_karyawan, load_karyawan, update_pendapatan_tambahan

# ---------- 1. Buat perusahaan ----------
perusahaan1 = Perusahaan("TechCorp", "Jl. Sudirman 123", "08123456789")

# ---------- 2. Buat karyawan ----------
k1 = AnalisData("Azmi")
k2 = IlmuwanData("Budi")
k3 = TenagaLepas("Cici", 22, 4000000)

# ---------- 3. Aktifkan karyawan di Python ----------
perusahaan1.aktifkan_karyawan(k1)
perusahaan1.aktifkan_karyawan(k2)
perusahaan1.aktifkan_karyawan(k3)

# ---------- 4. Masukkan karyawan ke database ----------
insert_karyawan(k1)
insert_karyawan(k2)
insert_karyawan(k3)

# ---------- 5. Contoh update pendapatan tambahan ----------
# Misal Azmi lembur
update_pendapatan_tambahan(1, k1.insentif_lembur)  # id=1 sesuai di DB
# Misal Budi dapat tambahan proyek 1.000.000
update_pendapatan_tambahan(2, 1000000)

# ---------- 6. Ambil data dari DB ----------
all_karyawan = load_karyawan()
print("Data semua karyawan dari DB:")
for k in all_karyawan:
    print(k)

# ---------- 7. Hitung total pengeluaran di Python ----------
print("\nTotal pengeluaran perusahaan (Python object):", perusahaan1.total_pengeluaran())
