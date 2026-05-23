## Implementasi Binary Search Tree pada Sistem Data Nilai Mahasiswa

<p align="justify">
Program ini merupakan implementasi struktur data <b>Binary Search Tree (BST)</b> menggunakan bahasa Python dengan studi kasus pengelolaan data nilai mahasiswa. Program digunakan untuk menyimpan, mencari, dan menampilkan data nilai secara terstruktur.
</p>

<p align="justify">
BST bekerja dengan konsep node kiri memiliki nilai lebih kecil dan node kanan memiliki nilai lebih besar. Struktur ini memungkinkan proses pencarian data dilakukan lebih cepat dibanding pencarian linear biasa.
</p>

## Source Code

<img width="314" height="138" alt="Screenshot 2026-05-23 093228" src="https://github.com/user-attachments/assets/b3b6f7ee-e53c-4cd7-bd7f-ebced9c906db" />
<br></br>

<img width="606" height="940" alt="Screenshot 2026-05-23 093255" src="https://github.com/user-attachments/assets/935d53d2-0dae-4894-b950-07448a1b94d7" />
<br></br>

<img width="435" height="863" alt="Screenshot 2026-05-23 093308" src="https://github.com/user-attachments/assets/7e079563-1f5f-46f9-8d30-e45f6d7c527f" />
<br></br>

<img width="787" height="284" alt="Screenshot 2026-05-23 093318" src="https://github.com/user-attachments/assets/aab2e89d-2ca9-44ee-b946-312efbd248fa" />
<br></br>

<img width="625" height="790" alt="Screenshot 2026-05-23 093328" src="https://github.com/user-attachments/assets/255e7e2f-ced6-4192-905f-d3a606c78e16" />
<br></br>

<img width="668" height="841" alt="Screenshot 2026-05-23 093343" src="https://github.com/user-attachments/assets/6fea2bc5-1388-44af-91a7-b7b7baa79610" />
<br></br>

<img width="691" height="305" alt="Screenshot 2026-05-23 093906" src="https://github.com/user-attachments/assets/61f6015c-ee73-4f99-a5af-abbbf0f4bece" />





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

### 1. Output PIlihan 1
<img width="353" height="938" alt="Screenshot 2026-05-23 094058" src="https://github.com/user-attachments/assets/16818934-3f94-4586-9b24-c03d9fe4c415" />
<br></br>
<img width="348" height="629" alt="Screenshot 2026-05-23 094110" src="https://github.com/user-attachments/assets/cb789897-22c8-4999-abac-7887de6a7520" />
<br></br>

### 2. Output Pilihan 2
<img width="338" height="311" alt="Screenshot 2026-05-23 094345" src="https://github.com/user-attachments/assets/988aa4e4-b5de-49a2-833e-8d2b334970c7" />
<br></br>

### 3. Output Pilihan 3
<img width="339" height="289" alt="Screenshot 2026-05-23 094400" src="https://github.com/user-attachments/assets/0e2d877b-b5dd-4f56-af36-79c9ac48c5e3" />
<br></br>

### 4. Output Pilihan 4
<img width="338" height="281" alt="Screenshot 2026-05-23 094414" src="https://github.com/user-attachments/assets/45137e0b-214b-4c0f-bbf1-ac00ee17f102" />
<br></br>

### 5. Output Pilihan 5
<img width="334" height="292" alt="Screenshot 2026-05-23 094438" src="https://github.com/user-attachments/assets/2e091561-5cf1-45ac-a095-b3c469356173" />
<br></br>

### 6. Output Pilihan 6
<img width="347" height="285" alt="Screenshot 2026-05-23 094450" src="https://github.com/user-attachments/assets/9a41c8cf-140c-402f-8109-d6d9e62d56ad" />
<br></br>

### 7. Output Pilihan 7
<img width="338" height="282" alt="Screenshot 2026-05-23 094507" src="https://github.com/user-attachments/assets/ef6bae6d-ed11-4791-b8ce-b974d5124adc" />
<br></br>

### 8. Output Pilihan 8
<img width="345" height="278" alt="Screenshot 2026-05-23 094518" src="https://github.com/user-attachments/assets/1dabca79-37bc-4542-a52e-af6ee92fe6be" />
<br></br>

### 9. Output Pilihan 9
<img width="343" height="287" alt="Screenshot 2026-05-23 094526" src="https://github.com/user-attachments/assets/8dbd99d0-47c4-4643-a223-2745a47db37a" />
<br></br>

### 10. Output Pilihan 10
<img width="348" height="294" alt="Screenshot 2026-05-23 094536" src="https://github.com/user-attachments/assets/d4fb10a9-e964-4169-b9af-cdf2b8e46fd9" />

### Penjelasan Output

<p align="justify">
Program akan menampilkan menu interaktif untuk mengelola data nilai mahasiswa menggunakan Binary Search Tree. Pengguna dapat menambahkan nilai, mencari data, melihat traversal tree, serta mengetahui nilai minimum, maksimum, jumlah data, dan total nilai.
</p>

<p align="justify">
Data dalam BST akan tersusun otomatis berdasarkan aturan Binary Search Tree sehingga pencarian dan pengelolaan data menjadi lebih efisien.
</p>



## 📌 Link YouTube

🎥 Demo Program:  
https://youtube.com/ISI_LINK_VIDEO
