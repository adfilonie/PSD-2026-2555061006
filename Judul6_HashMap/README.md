## Implementasi HashMap Open Addressing pada Sistem Data Produk Minimarket

<p align="justify">
Program ini merupakan implementasi struktur data <b>HashMap Open Addressing</b> menggunakan metode <b>Linear Probing</b> dengan studi kasus sistem data produk minimarket. Program digunakan untuk menyimpan, mencari, dan menghapus data produk berdasarkan kode produk.
</p>

<p align="justify">
HashMap bekerja dengan menggunakan fungsi hash untuk menentukan posisi penyimpanan data pada tabel. Jika terjadi collision atau tabrakan data, maka program akan mencari slot kosong berikutnya menggunakan metode Linear Probing.
</p>


## Source Code

> Tambahkan screenshot source code di sini

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

> Tambahkan screenshot output program di sini

<br>

### Penjelasan Output

<p align="justify">
Program akan menampilkan data produk yang tersimpan di dalam hash table. Pengguna dapat melihat proses penambahan produk, pencarian produk berdasarkan kode, dan penghapusan data produk.
</p>

<p align="justify">
Jika terjadi collision, program akan mencari slot kosong berikutnya menggunakan metode Linear Probing sehingga data tetap dapat disimpan tanpa menimpa data lain.
</p>


### Contoh Output

Input:

```text
Tambah produk:
101 → 5000
111 → 12000
121 → 7000
```

Output:

```text
Data Produk Minimarket:
0: EMPTY
1: (Kode: 101, Harga: 5000)
2: (Kode: 111, Harga: 12000)
3: (Kode: 121, Harga: 7000)
```


## Link YouTube

Demo Program:
https://youtu.be/0vN7ALuF0rM?si=ykCIKE0q3_NcixUv
