## Implementasi Binary Search Tree pada Sistem Data Nilai Mahasiswa

<p align="justify">
Program ini merupakan implementasi struktur data <b>Binary Search Tree (BST)</b> menggunakan bahasa Python dengan studi kasus pengelolaan data nilai mahasiswa. Program digunakan untuk menyimpan, mencari, dan menampilkan data nilai secara terstruktur.
</p>

<p align="justify">
BST bekerja dengan konsep node kiri memiliki nilai lebih kecil dan node kanan memiliki nilai lebih besar. Struktur ini memungkinkan proses pencarian data dilakukan lebih cepat dibanding pencarian linear biasa.
</p>

## Source Code

> Tambahkan screenshot source code di sini


## Penjelasan Kode

### Class `Node`
- Merepresentasikan satu data nilai mahasiswa
- `key` → menyimpan nilai
- `left` → node kiri
- `right` → node kanan


### Class `BSTNilaiMahasiswa`
- Mengelola seluruh data BST
- `root` → node utama/pusat tree

### Fungsi `insert_node`
- Menambahkan data ke BST
- Nilai kecil masuk ke kiri
- Nilai besar masuk ke kanan

### Fungsi `tambah_nilai`
- Memanggil proses insert data

### Fungsi `search_node`
- Mencari nilai dalam BST
- Menggunakan konsep perbandingan kiri dan kanan

### Fungsi `cari_nilai`
- Memanggil proses pencarian data

### Fungsi `inorder`
- Menampilkan data secara urut dari kecil ke besar

### Fungsi `preorder`
- Menampilkan root terlebih dahulu


### Fungsi `postorder`
- Menampilkan root paling akhir


### Fungsi `nilai_terendah`
- Mencari nilai paling kecil pada BST

### Fungsi `nilai_tertinggi`
- Mencari nilai paling besar pada BST

### Fungsi `jumlah_data`
- Menghitung jumlah seluruh node

### Fungsi `total_nilai`
- Menghitung total seluruh nilai mahasiswa

### Fungsi `main`
- Menjalankan menu interaktif program

Menu:
1. Tambah nilai
2. Cari nilai
3. Inorder
4. Preorder
5. Postorder
6. Nilai terendah
7. Nilai tertinggi
8. Jumlah data
9. Total nilai
10. Keluar


## Output Program

> Tambahkan screenshot output program di sini

### Penjelasan Output

<p align="justify">
Program akan menampilkan menu interaktif untuk mengelola data nilai mahasiswa menggunakan Binary Search Tree. Pengguna dapat menambahkan nilai, mencari data, melihat traversal tree, serta mengetahui nilai minimum, maksimum, jumlah data, dan total nilai.
</p>

<p align="justify">
Data dalam BST akan tersusun otomatis berdasarkan aturan Binary Search Tree sehingga pencarian dan pengelolaan data menjadi lebih efisien.
</p>


### Contoh Output

Input:
```text
70
85
60
90
75
```

Output inorder:
```text
60 70 75 85 90
```

---

## 📌 Link YouTube

🎥 Demo Program:  
https://youtube.com/ISI_LINK_VIDEO
