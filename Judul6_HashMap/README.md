## Implementasi HashMap Open Addressing pada Sistem Data Produk Minimarket

<p align="justify">
Program ini merupakan implementasi struktur data <b>HashMap Open Addressing</b> menggunakan metode <b>Linear Probing</b> dengan studi kasus sistem data produk minimarket. Program digunakan untuk menyimpan, mencari, dan menghapus data produk berdasarkan kode produk.
</p>

<p align="justify">
HashMap bekerja dengan menggunakan fungsi hash untuk menentukan posisi penyimpanan data pada tabel. Jika terjadi collision atau tabrakan data, maka program akan mencari slot kosong berikutnya menggunakan metode Linear Probing.
</p>


## Source Code

<img width="640" height="477" alt="Screenshot 2026-06-08 231757" src="https://github.com/user-attachments/assets/5a819851-83ff-417c-a8ec-5acf7c13e5fe" />
<br>
<img width="574" height="869" alt="Screenshot 2026-06-08 231742" src="https://github.com/user-attachments/assets/95cea171-329e-4cfd-9984-cca0530b06bf" />
<br>
<img width="558" height="385" alt="Screenshot 2026-06-08 231731" src="https://github.com/user-attachments/assets/03a7b1a6-e0c7-4e2c-8eb9-35fe46535115" />
<br>
<img width="806" height="661" alt="Screenshot 2026-06-08 231718" src="https://github.com/user-attachments/assets/21984338-ede5-470b-8673-ef848389d761" />
<br>
<img width="687" height="827" alt="Screenshot 2026-06-08 231700" src="https://github.com/user-attachments/assets/986aef24-7642-4ad1-9f55-0f3ec12d7a8a" />
<br>

## Penjelasan Kode

### Class `SlotState`

* Digunakan untuk menentukan status slot pada hash table
* `EMPTY` → slot kosong
* `OCCUPIED` → slot terisi data
* `DELETED` → slot pernah dihapus


### Class `Entry`

* Merepresentasikan satu data produk
* `kode_produk` → key data
* `harga` → value data
* `state` → status slot


### Class `HashMapProduk`

* Mengelola seluruh data hash table
* `table` → array penyimpanan data produk


### Fungsi `hash_function`

* Menghasilkan indeks penyimpanan berdasarkan kode produk


### Fungsi `tambah_produk`

* Menambahkan produk ke hash table
* Menggunakan Linear Probing jika terjadi collision


### Fungsi `cari_produk`

* Digunakan untuk mencari data produk berdasarkan kode produk


### Fungsi `hapus_produk`

* Menghapus data produk dari hash table


### Fungsi `tampilkan_produk`

* Menampilkan seluruh isi hash table


### Fungsi `main`

* Menjalankan simulasi program
* Menambahkan data produk
* Mencari produk
* Menghapus produk
* Menampilkan isi hash table


## Output Program

<img width="403" height="643" alt="Screenshot 2026-06-08 231647" src="https://github.com/user-attachments/assets/840710b0-4d6b-4735-a710-99726f4b019d" />


<br>

### Penjelasan Output

<p align="justify">
Program akan menampilkan data produk yang tersimpan di dalam hash table. Pengguna dapat melihat proses penambahan produk, pencarian produk berdasarkan kode, dan penghapusan data produk.
</p>

<p align="justify">
Jika terjadi collision, program akan mencari slot kosong berikutnya menggunakan metode Linear Probing sehingga data tetap dapat disimpan tanpa menimpa data lain.
</p>


## Link YouTube

Demo Program:
https://youtu.be/0vN7ALuF0rM?si=ykCIKE0q3_NcixUv
