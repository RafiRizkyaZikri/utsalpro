# Deklarasi Variabel dan Tipe Data
nama_lengkap: str = "Rafi Rizkya Zikri"                      # Tipe data String (Teks)
tempat_tanggal_lahir: str = "Bogor, 20 September 2008"        # Tipe data String (Teks)
jenis_kelamin: str = "Laki - laki"                           # Tipe data String (Teks)
alamat_lengkap: str = "Cikereteg, RT 01 RW 04 Desa Ciderum Kec. Caringin Kab. Bogor"  # Tipe data String (Teks)
no_hp: str = "081281160411"                                  # Tipe data String (Nomor HP menggunakan string agar angka '0' di depan tidak hilang)
penghasilan_sebulan: int = 6500000                           # Tipe data Integer (Angka bulat, cocok untuk nilai uang)

# Menampilkan Data ke Layar
print("=" * 37)
print("         DATA INFORMASI PRIBADI")
print("=" * 37)
print(f"Nama Lengkap         : {nama_lengkap}")
print(f"Tempat & Tanggal Lahir : {tempat_tanggal_lahir}")
print(f"Jenis Kelamin        : {jenis_kelamin}")
print(f"Alamat Lengkap       : {alamat_lengkap}")
print(f"No Hp                : {no_hp}")

# Memformat penghasilan agar menggunakan titik sebagai pemisah ribuan
format_penghasilan = f"Rp {penghasilan_sebulan:,}".replace(",", ".")
print(f"Penghasilan Sebulan  : {format_penghasilan}")
print("=" * 37)