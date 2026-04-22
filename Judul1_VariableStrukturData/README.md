## Implementasi Linked List pada Sistem Antrian Printer

Program ini merupakan implementasi struktur data Linked List menggunakan bahasa Python yang diterapkan pada studi kasus antrian printer. Dalam program ini, setiap dokumen direpresentasikan sebagai sebuah node yang saling terhubung melalui pointer next. Sistem antrian mengikuti konsep FIFO (First In First Out), di mana dokumen yang pertama masuk akan diproses lebih dahulu.

Algoritma yang digunakan adalah Single Linked List, dengan dua pointer utama yaitu start sebagai penunjuk elemen pertama dan rear sebagai penunjuk elemen terakhir. Operasi utama dalam program ini meliputi penambahan dokumen ke dalam antrian (enqueue), penghapusan dokumen dari antrian (dequeue), serta penampilan isi antrian secara berurutan.

## Source Code
<img width="607" height="910" alt="Screenshot 2026-04-22 230257" src="https://github.com/user-attachments/assets/450c36cf-5328-4733-a624-60c298cfe173" />
<br><br>
<img width="534" height="883" alt="Screenshot 2026-04-22 230307" src="https://github.com/user-attachments/assets/38eaa921-1e12-4766-b504-75db3ca4b90f" />
<br><br>

## Penjelasan Kode

### Class Node
Class `Node` digunakan untuk merepresentasikan satu data dalam antrian.  
Setiap node memiliki atribut:
- `data` → menyimpan nama dokumen  
- `next` → pointer ke node berikutnya  



### Class PrinterQueue
Class ini berfungsi untuk mengelola antrian printer menggunakan Linked List.

Memiliki dua atribut utama:
- `start` → menunjuk ke dokumen paling depan  
- `rear` → menunjuk ke dokumen paling belakang  



### Fungsi create_new_node
Fungsi ini digunakan untuk membuat node baru berdasarkan input pengguna, yaitu nama dokumen yang akan dimasukkan ke dalam antrian.



### Fungsi insert_at_end
Fungsi ini digunakan untuk menambahkan dokumen ke dalam antrian.  
Jika antrian kosong, maka node menjadi elemen pertama. Jika tidak, maka node akan ditambahkan di bagian belakang.


### Fungsi delete_node
Fungsi ini digunakan untuk mencetak dokumen, yaitu dengan menghapus node dari bagian depan antrian.  
Jika antrian kosong, maka akan ditampilkan pesan bahwa tidak ada dokumen.



### Fungsi display
Fungsi ini digunakan untuk menampilkan seluruh isi antrian dari depan ke belakang dalam bentuk berurutan.



### Fungsi main
Fungsi utama yang menjalankan program dengan menu interaktif:

1. Tambah dokumen  
2. Cetak dokumen  
3. Lihat antrian  
4. Keluar program

## Output Program
1. Tambah dokumen  
<img width="276" height="663" alt="Screenshot 2026-04-22 231405" src="https://github.com/user-attachments/assets/50dc8302-bd7a-4712-8ed9-d496a9566113" />
<br><br>

2. Cetak dokumen  
<img width="221" height="179" alt="Screenshot 2026-04-22 231423" src="https://github.com/user-attachments/assets/256eb76a-5b6c-4ea0-99ea-7dfb2765bbf0" />
<br><br>

3. Lihat antrian  
<img width="239" height="162" alt="Screenshot 2026-04-22 231435" src="https://github.com/user-attachments/assets/258fc040-7bdd-42df-a8a7-ec7d9dca5dcd" />
<br><br>

4. Keluar program
<img width="217" height="171" alt="Screenshot 2026-04-22 231442" src="https://github.com/user-attachments/assets/e9ddc29a-b285-4af2-b24c-20fcbc5a1831" />
<br><br>

## Penjelasan Ouput
Output program menampilkan menu interaktif yang memungkinkan pengguna untuk menambahkan dokumen ke dalam antrian, mencetak dokumen, dan melihat isi antrian.
Ketika dokumen ditambahkan, data akan masuk ke bagian belakang antrian. Saat dokumen dicetak, data akan keluar dari bagian depan sesuai konsep FIFO.

## Link YouTube
[Klik di sini untuk melihat video demo](https://youtu.be/0vN7ALuF0rM?si=ykCIKE0q3_NcixUv)
