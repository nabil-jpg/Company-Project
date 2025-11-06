# company.py


class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur):
        # atribut dasar karyawan
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        # pendapatan_tambahan akan bertambah jika lembur atau proyek
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur

    def lembur(self):
        """
        Tambah pendapatan_tambahan sebesar insentif_lembur.
        Jika ingin menambah lebih dari 1 kali, panggil berkali-kali
        atau modifikasi metode untuk menerima argumen jumlah.
        """
        self.pendapatan_tambahan += self.insentif_lembur

    def tambahan_proyek(self, jumlah_tambahan):
        """
        Default: tambahkan jumlah_tambahan (nilai uang) ke pendapatan_tambahan.
        Untuk beberapa child class, metode ini akan di-override.
        """
        self.pendapatan_tambahan += jumlah_tambahan

    def total_pendapatan(self):
        """Kembalikan total (gaji + tambahan)."""
        return self.pendapatan + self.pendapatan_tambahan

    def __repr__(self):
        # memudahkan saat print(list_karyawan)
        return f"{self.__class__.__name__}({self.nama}, total={self.total_pendapatan()})"


class TenagaLepas(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        # freelance tidak punya insentif lembur tetap, jadi kasi 0
        super().__init__(nama, usia, pendapatan, 0)

    def tambahan_proyek(self, nilai_proyek):
        """
        Biasanya freelancer mendapat persentase yang lebih tinggi, misal 10% (0.1).
        Di sini saya pakai 0.1 (10%) supaya terlihat lebih masuk akal,
        """
        self.pendapatan_tambahan += nilai_proyek * 0.1


class AnalisData(Karyawan):
    def __init__(self, nama, usia=21, pendapatan=6500000, insentif_lembur=100000):
        super().__init__(nama, usia, pendapatan, insentif_lembur)


class IlmuwanData(Karyawan):
    def __init__(self, nama, usia=25, pendapatan=12000000, insentif_lembur=150000):
        super().__init__(nama, usia, pendapatan, insentif_lembur)

    def tambahan_proyek(self, nilai_proyek):
        # ilmuwan data dapat 10% dari nilai proyek (contoh)
        self.pendapatan_tambahan += 0.1 * nilai_proyek


class PembersihData(TenagaLepas):
    def __init__(self, nama, usia, pendapatan=4000000):
        super().__init__(nama, usia, pendapatan)


class DokumenterTeknis(TenagaLepas):
    def __init__(self, nama, usia, pendapatan=2500000):
        super().__init__(nama, usia, pendapatan)


class Perusahaan:
    def __init__(self, nama, alamat, nomor_telepon):
        self.nama = nama
        self.alamat = alamat
        self.nomor_telepon = nomor_telepon
        self.list_karyawan = []

    def aktifkan_karyawan(self, karyawan):
        """Tambahkan object karyawan ke perusahaan."""
        self.list_karyawan.append(karyawan)

    def nonaktifkan_karyawan(self, nama_karyawan):
        """Hapus karyawan berdasarkan nama (jika ditemukan)."""
        karyawan_nonaktif = None
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan:
                karyawan_nonaktif = karyawan
                break
        if karyawan_nonaktif is not None:
            self.list_karyawan.remove(karyawan_nonaktif)

    def total_pengeluaran(self):
        """Jumlahkan total_pendapatan semua karyawan aktif."""
        pengeluaran = 0
        for karyawan in self.list_karyawan:
            pengeluaran += karyawan.total_pendapatan()
        return pengeluaran

    def cari_karyawan(self, nama_karyawan):
        """Cari karyawan berdasarkan nama, kembalikan object atau None."""
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan:
                return karyawan
        return None
