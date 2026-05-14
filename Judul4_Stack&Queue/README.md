##  Implementasi Queue Linked List pada Sistem Antrian Printer

<p align="justify">
Program ini merupakan implementasi struktur data <b>Queue Linked List</b> menggunakan bahasa Python dengan studi kasus sistem antrian printer. Program digunakan untuk mengelola dokumen yang akan dicetak berdasarkan urutan kedatangan dokumen.
</p>

<p align="justify">
Konsep yang digunakan adalah <b>FIFO (First In First Out)</b>, yaitu dokumen yang pertama masuk ke dalam antrian akan dicetak terlebih dahulu. Struktur data Linked List digunakan agar proses penambahan dan penghapusan data dapat dilakukan secara dinamis.
</p>


## Source Code

<img width="353" height="128" alt="Screenshot 2026-05-14 222105" src="https://github.com/user-attachments/assets/bb8d8057-4eea-43f8-ad46-ffd3e4794c88" />

<br><br>

<img width="594" height="783" alt="Screenshot 2026-05-14 222117" src="https://github.com/user-attachments/assets/967301a0-b73e-4266-a70e-19cbc7024f2a" />

<br><br>

<img width="561" height="507" alt="Screenshot 2026-05-14 222129" src="https://github.com/user-attachments/assets/67aa7b9f-ab78-4476-8000-d7f2546a5bba" />

<br><br>

<img width="478" height="859" alt="Screenshot 2026-05-14 222145" src="https://github.com/user-attachments/assets/e361e74b-5bdc-447e-b2bc-b0076e4dcaea" />

<br><br>

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

<img width="317" height="504" alt="Screenshot 2026-05-14 222247" src="https://github.com/user-attachments/assets/b354c822-8a27-4e19-a82a-29964a4b6a08" />

<br><br>

<img width="293" height="155" alt="Screenshot 2026-05-14 222303" src="https://github.com/user-attachments/assets/efba7187-aef4-4074-b2aa-4b4d9d489c41" />

<br><br>

<img width="247" height="150" alt="Screenshot 2026-05-14 222319" src="https://github.com/user-attachments/assets/dcfbaceb-8494-476f-9f1d-f668551019bc" />

<br><br>

<img width="276" height="153" alt="Screenshot 2026-05-14 222334" src="https://github.com/user-attachments/assets/4f2b4b49-71e0-47fb-b511-75273491ceaf" />

<br><br>

<img width="314" height="174" alt="Screenshot 2026-05-14 222345" src="https://github.com/user-attachments/assets/8ef1c6f6-4b4d-459a-b421-32142f3970c6" />


### Penjelasan Output

<p align="justify">
Program akan menampilkan menu interaktif untuk mengelola antrian printer. Pengguna dapat menambahkan dokumen ke dalam antrian, mencetak dokumen, melihat dokumen paling depan, dan menampilkan seluruh isi antrian.
</p>

<p align="justify">
Dokumen yang pertama masuk akan dicetak terlebih dahulu sesuai konsep FIFO (First In First Out). Jika antrian kosong, program akan menampilkan pesan bahwa tidak ada dokumen yang tersedia.
</p>

## Link YouTube

Demo Program:  
[Klik disini utk melihat demo](https://youtu.be/m9CzbpjTdpI?si=R1_D8Ej0wtCpvH3j)
