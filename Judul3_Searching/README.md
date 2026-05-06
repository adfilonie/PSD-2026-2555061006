# Sistem Cek Kehadiran Mahasiswa (Sequential Search)

Program ini digunakan untuk mengecek apakah nama mahasiswa terdapat dalam daftar absensi. Pencarian dilakukan menggunakan algoritma **Sequential Search**, yaitu metode pencarian yang memeriksa data satu per satu dari awal hingga akhir.

Algoritma ini cocok digunakan untuk data yang tidak terlalu besar dan tidak harus dalam kondisi terurut. Program juga menangani perbedaan huruf besar/kecil dan spasi agar pencarian lebih fleksibel.


## Source Code
<img width="596" height="667" alt="Screenshot 2026-05-06 212459" src="https://github.com/user-attachments/assets/a50d0f28-98a5-4f5e-b4a6-2c6409635a35" />
<br></br>


## Penjelasan Kode

### Fungsi `sequential_search`
- Melakukan pencarian nama dalam list absensi
- Mengecek setiap elemen satu per satu
- Menggunakan `lower()` untuk menyamakan huruf agar tidak sensitif terhadap huruf besar/kecil
- Jika ditemukan → return `True`
- Jika tidak → return `False`

### Fungsi `main`
- Menyimpan data absensi dalam list
- Menampilkan daftar nama
- Menerima input nama dari user
- Memanggil fungsi pencarian
- Menampilkan hasil (hadir / tidak hadir)


## Output Program
### Output Jika Mahasiswa Hadir (Nama ada pada Array)
<img width="598" height="142" alt="Screenshot 2026-05-06 212040" src="https://github.com/user-attachments/assets/a3eb876e-a9ab-4ee5-961a-d59b711cd820" />

### Output Jika Mahasiswa Tidak Hadir (Nama tidak ada pada array)
<img width="610" height="145" alt="Screenshot 2026-05-06 212047" src="https://github.com/user-attachments/assets/1e661e55-893f-403b-8104-195d68ce1343" />


### Penjelasan Output
<p align="justify">
Program akan menampilkan daftar absensi yang sudah tersedia, kemudian pengguna diminta memasukkan nama mahasiswa. Jika nama yang dimasukkan terdapat dalam daftar, maka program akan menampilkan pesan bahwa mahasiswa tersebut hadir. Sebaliknya, jika nama tidak ditemukan, maka akan ditampilkan bahwa mahasiswa tidak hadir. Program juga menggunakan <code>lower()</code> sehingga perbedaan huruf besar dan kecil tidak mempengaruhi hasil pencarian.
</p>
