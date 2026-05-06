# Sistem Cek Kehadiran Mahasiswa (Sequential Search)

Program ini digunakan untuk mengecek apakah nama mahasiswa terdapat dalam daftar absensi. Pencarian dilakukan menggunakan algoritma **Sequential Search**, yaitu metode pencarian yang memeriksa data satu per satu dari awal hingga akhir.

Algoritma ini cocok digunakan untuk data yang tidak terlalu besar dan tidak harus dalam kondisi terurut. Program juga menangani perbedaan huruf besar/kecil dan spasi agar pencarian lebih fleksibel.


## Source Code
> Tambahkan screenshot kode di sini


## Penjelasan Kode

### Fungsi `sequential_search`
- Melakukan pencarian nama dalam list absensi
- Mengecek setiap elemen satu per satu
- Menggunakan:
  - `strip()` → menghapus spasi berlebih
  - `casefold()` → menyamakan huruf (biar tidak case-sensitive)
- Jika ditemukan → return `True`
- Jika tidak → return `False`

### Fungsi `main`
- Menyimpan data absensi dalam list
- Menampilkan daftar nama
- Menerima input nama dari user
- Memanggil fungsi pencarian
- Menampilkan hasil (hadir / tidak hadir)


## Output Program
> Tambahkan screenshot output di sini

### Contoh
Input:
```text
dave
