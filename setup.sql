-- Tabel perusahaan
CREATE TABLE perusahaan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    alamat VARCHAR(255) NOT NULL,
    nomor_telepon VARCHAR(20) NOT NULL
);

-- Tabel karyawan
CREATE TABLE karyawan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    usia INT NOT NULL,
    pendapatan BIGINT NOT NULL,
    pendapatan_tambahan BIGINT DEFAULT 0,
    insentif_lembur BIGINT NOT NULL,
    tipe_karyawan VARCHAR(50) NOT NULL
);

-- Tabel karyawan_perusahaan
CREATE TABLE karyawan_perusahaan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_perusahaan INT NOT NULL,
    id_karyawan INT NOT NULL,
    status_aktif TINYINT DEFAULT 1,
    FOREIGN KEY (id_perusahaan) REFERENCES perusahaan(id),
    FOREIGN KEY (id_karyawan) REFERENCES karyawan(id)
);

-- Tabel proyek
CREATE TABLE proyek (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    nilai BIGINT NOT NULL,
    id_karyawan INT NOT NULL,
    FOREIGN KEY (id_karyawan) REFERENCES karyawan(id)
);

-- Contoh data karyawan
INSERT INTO karyawan (nama, usia, pendapatan, pendapatan_tambahan, insentif_lembur, tipe_karyawan)
VALUES ('Azmi', 21, 6500000, 0, 100000, 'AnalisData');
