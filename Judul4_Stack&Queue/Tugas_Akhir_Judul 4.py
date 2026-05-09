class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class PrinterQueue:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None

    def is_empty(self):
        return self.front_ptr is None

    def tambah_dokumen(self, nama_file):
        new_node = Node(nama_file)

        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node

        print(f"Dokumen '{nama_file}' berhasil ditambahkan")

    def cetak_dokumen(self):
        if self.is_empty():
            print("Antrian printer kosong")
            return

        temp = self.front_ptr

        print(f"Mencetak dokumen: {temp.data}")

        self.front_ptr = self.front_ptr.next

        if self.front_ptr is None:
            self.rear_ptr = None

    def lihat_dokumen_terdepan(self):
        if self.is_empty():
            print("Antrian printer kosong")
            return

        print(f"Dokumen berikutnya: {self.front_ptr.data}")

    def tampilkan_antrian(self):
        if self.is_empty():
            print("Antrian printer kosong")
            return

        print("Daftar antrian dokumen:")

        current = self.front_ptr

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


def main():
    printer = PrinterQueue()

    pilih = 0

    while pilih != 5:
        print("\n=== SISTEM ANTRIAN PRINTER ===")
        print("1. Tambah dokumen")
        print("2. Cetak dokumen")
        print("3. Lihat dokumen terdepan")
        print("4. Tampilkan antrian")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if pilih == 1:
            nama = input("Masukkan nama dokumen: ")
            printer.tambah_dokumen(nama)

        elif pilih == 2:
            printer.cetak_dokumen()

        elif pilih == 3:
            printer.lihat_dokumen_terdepan()

        elif pilih == 4:
            printer.tampilkan_antrian()

        elif pilih == 5:
            while not printer.is_empty():
                printer.cetak_dokumen()

            print("Program selesai")

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()
