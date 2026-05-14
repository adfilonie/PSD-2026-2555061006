##  Implementasi Queue Linked List pada Sistem Antrian Printer

<p align="justify">
Program ini merupakan implementasi struktur data <b>Queue Linked List</b> menggunakan bahasa Python dengan studi kasus sistem antrian printer. Program digunakan untuk mengelola dokumen yang akan dicetak berdasarkan urutan kedatangan dokumen.
</p>

<p align="justify">
Konsep yang digunakan adalah <b>FIFO (First In First Out)</b>, yaitu dokumen yang pertama masuk ke dalam antrian akan dicetak terlebih dahulu. Struktur data Linked List digunakan agar proses penambahan dan penghapusan data dapat dilakukan secara dinamis.
</p>


## Source Code

> Tambahkan screenshot source code di sini


## Penjelasan Kode

### Class `Node`
- Merepresentasikan satu data dokumen
- `data` → menyimpan nama dokumen
- `next` → pointer ke node berikutnya


### Class `PrinterQueue`
- Mengelola seluruh antrian printer
- `front_ptr` → menunjuk dokumen paling depan
- `rear_ptr` → menunjuk dokumen paling belakang


### Fungsi `is_empty`
- Mengecek apakah antrian kosong atau tidak
- Mengembalikan nilai `True` atau `False`

---

### Fungsi `tambah_dokumen`
- Menambahkan dokumen ke belakang antrian
- Jika antrian kosong, dokumen menjadi elemen pertama


### Fungsi `cetak_dokumen`
- Menghapus dan mencetak dokumen paling depan
- Jika kosong, program menampilkan pesan antrian kosong


### Fungsi `lihat_dokumen_terdepan`
- Menampilkan dokumen yang berada di posisi paling depan


### Fungsi `tampilkan_antrian`
- Menampilkan seluruh isi antrian dari depan ke belakang


### Fungsi `main`
- Menjalankan menu interaktif program
- Menu:
  1. Tambah dokumen
  2. Cetak dokumen
  3. Lihat dokumen terdepan
  4. Tampilkan antrian
  5. Keluar program

## Output Program

> Tambahkan screenshot output program di sini

### Penjelasan Output

<p align="justify">
Program akan menampilkan menu interaktif untuk mengelola antrian printer. Pengguna dapat menambahkan dokumen ke dalam antrian, mencetak dokumen, melihat dokumen paling depan, dan menampilkan seluruh isi antrian.
</p>

<p align="justify">
Dokumen yang pertama masuk akan dicetak terlebih dahulu sesuai konsep FIFO (First In First Out). Jika antrian kosong, program akan menampilkan pesan bahwa tidak ada dokumen yang tersedia.
</p>

### Contoh Output

Input:
```text
1
Tugas_AI.pdf

1
Laporan_StrukturData.docx

4
```

Output:
```text
Daftar antrian dokumen:
Tugas_AI.pdf -> Laporan_StrukturData.docx -> None
```

---

## Link YouTube

Demo Program:  
[Klik disini utk melihat demo]()
