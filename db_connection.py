import os
from dotenv import load_dotenv
import mysql.connector


# load .env dari root project
load_dotenv()


def get_connection():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "companydb")
    )
    return conn

# ---------- 2. Fungsi CRUD ----------

# Tambah karyawan baru
def insert_karyawan(karyawan):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO karyawan (nama, usia, pendapatan, pendapatan_tambahan, insentif_lembur, tipe_karyawan)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (karyawan.nama, karyawan.usia, karyawan.pendapatan, karyawan.pendapatan_tambahan, karyawan.insentif_lembur, karyawan.__class__.__name__))
    conn.commit()
    cursor.close()
    conn.close()

# Ambil semua karyawan
def load_karyawan():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM karyawan")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# Cari karyawan berdasarkan id
def get_karyawan_by_id(karyawan_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM karyawan WHERE id = %s", (karyawan_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

# Update pendapatan_tambahan
def update_pendapatan_tambahan(karyawan_id, jumlah_tambahan):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE karyawan
        SET pendapatan_tambahan = pendapatan_tambahan + %s
        WHERE id = %s
    """, (jumlah_tambahan, karyawan_id))
    conn.commit()
    cursor.close()
    conn.close()

# Hapus karyawan
def delete_karyawan(karyawan_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM karyawan WHERE id = %s", (karyawan_id,))
    conn.commit()
    cursor.close()
    conn.close()
