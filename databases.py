import mysql.connector

# Membuat koneksi ke database
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="fuzzy_db"
)

# Membuat kursor untuk melakukan eksekusi perintah SQL
mycursor = mydb.cursor()

# Membuat database fuzzy_db jika belum ada
mycursor.execute("CREATE DATABASE IF NOT EXISTS fuzzy_db")

# Menggunakan database fuzzy_db
mycursor.execute("USE fuzzy_db")

# Membuat tabel tb_emp beserta kolom-kolomnya
mycursor.execute("DROP TABLE IF EXISTS tb_emp")
mycursor.execute("CREATE TABLE tb_emp (id INT AUTO_INCREMENT PRIMARY KEY, nama VARCHAR(50), usia TINYINT(2), masakerja TINYINT(2), gaji INT)")
mycursor.execute("ALTER TABLE tb_emp AUTO_INCREMENT=11")

# Menambahkan data ke dalam tabel tb_emp
sql = "INSERT INTO tb_emp (id, nama, usia, masakerja, gaji) VALUES (%s, %s, %s, %s, %s)"
val = [
  (1, 'Anik', 30, 6, 750000),
  (2, 'Yudi', 48, 17, 1255000),
  (3, 'Inawati', 36, 14, 1500000),
  (4, 'Rudi', 37, 4, 1040000),
  (5, 'Riska', 42, 12, 950000),
  (6, 'Aman', 39, 13, 1600000),
  (7, 'Dudi', 37, 5, 1250000),
  (8, 'Rini', 32, 1, 550000),
  (9, 'Ratih', 35, 3, 735000),
  (10, 'Panjul', 25, 2, 860000)
]
mycursor.executemany(sql, val)

# Membuat tabel tb_kelompok beserta kolom-kolomnya
mycursor.execute("DROP TABLE IF EXISTS tb_kelompok")
mycursor.execute("CREATE TABLE tb_kelompok (id INT AUTO_INCREMENT PRIMARY KEY, nama_kelompok VARCHAR(25), field_akses VARCHAR(25))")
mycursor.execute("ALTER TABLE tb_kelompok AUTO_INCREMENT=4")

# Menambahkan data ke dalam tabel tb_kelompok
sql = "INSERT INTO tb_kelompok (id, nama_kelompok, field_akses) VALUES (%s, %s, %s)"
val = [
  (1, 'Umur', 'usia'),
  (2, 'Masa Kerja', 'masakerja'),
  (3, 'Gaji', 'gaji')
]
mycursor.executemany(sql, val)

# Membuat tabel tb_kriteria beserta kolom-kolomnya
mycursor.execute("DROP TABLE IF EXISTS tb_kriteria")
mycursor.execute("CREATE TABLE tb_kriteria (id INT AUTO_INCREMENT PRIMARY KEY, nama_kriteria VARCHAR(30), bawah FLOAT(10,2), tengah FLOAT(10,2), atas FLOAT(10,2), kelompok TINYINT(2), keterangan VARCHAR(100))")
mycursor.execute("ALTER TABLE tb_kriteria AUTO_INCREMENT=9")



mycursor.execute("DROP TABLE IF EXISTS tb_kriteria")
mycursor.execute("""
    CREATE TABLE tb_kriteria (
        id INT(10) NOT NULL AUTO_INCREMENT,
        nama_kriteria VARCHAR(30) DEFAULT NULL,
        bawah FLOAT(10,2) DEFAULT NULL,
        tengah FLOAT(10,2) DEFAULT NULL,
        atas FLOAT(10,2) DEFAULT NULL,
        kelompok TINYINT(2) DEFAULT NULL,
        keterangan VARCHAR(100) DEFAULT NULL,
        PRIMARY KEY(id)
    ) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1
""")