import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="py_user",
    passwd="secret",
    database="db_python"
)

# if conn.is_connected():
# print("Koneksi berhasil dibuat")


def add_siswa(nis, nama, alamat):
    sql = "INSERT INTO siswa (nama, alamat, nis) VALUES (%s, %s, %s)"
    val = (nama, alamat, nis)

    cursor = conn.cursor()
    cursor.execute(sql, val)
    conn.commit()


def get_by_nis(nis):
    sql = "SELECT * FROM siswa WHERE nis = '" + nis + "'"
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()

    for data in results:
        print("ID:", data[0], "Nama:", data[1],
              "Alamat:", data[2], "NIS:", data[3])


def get_all():
    sql = "SELECT * FROM siswa WHERE terhapus is null"
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()

    for data in results:
        print("ID:", data[0], "Nama:", data[1],
              "Alamat:", data[2], "NIS:", data[3])


def update_data(id, nama, alamat):
    sql = """
        UPDATE siswa
        SET nama = %s, alamat = %s
        WHERE id = %s
    """
    val = (nama, alamat, id)
    cursor = conn.cursor()
    cursor.execute(sql, val)
    conn.commit()


def soft_delete_data(id):
    sql = "UPDATE siswa SET terhapus = 1 WHERE id = " + str(id)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()


def hapus_data(id):
    sql = "DELETE FROM siswa WHERE id = " + str(id)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()


#add_siswa("000000003", "Muflih", "Yogyakarta")
#add_siswa("000000004", "Firman", "Lamongan")
#add_siswa("000000005", "Budi", "Jombang")
# get_by_nis("000000002")
# get_all()
#update_data(4, "Akhdan", "Nganjuk")
# soft_delete_data(5)
# get_all()
hapus_data(7)
