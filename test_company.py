# test/test_company.py

from company import Perusahaan, Karyawan, AnalisData, IlmuwanData, PembersihData, DokumenterTeknis

def test_total_pengeluaran():
    ani = PembersihData('Ani', 25)
    budi = DokumenterTeknis('Budi', 18)
    cici = IlmuwanData('Cici')
    efi = AnalisData('Efi')

    perusahaan = Perusahaan('ABC', 'Jl. Jendral Sudirman', '(021) 95812XX')

    perusahaan.aktifkan_karyawan(ani)
    perusahaan.aktifkan_karyawan(budi)
    perusahaan.aktifkan_karyawan(cici)
    perusahaan.aktifkan_karyawan(efi)

    total = perusahaan.total_pengeluaran()
    print("Total pengeluaran perusahaan:", total)

if __name__ == "__main__":
    test_total_pengeluaran()

    test_total_pengeluaran()
