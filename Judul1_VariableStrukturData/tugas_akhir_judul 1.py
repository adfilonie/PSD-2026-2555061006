class Node:
    def __init__(self, dokumen):
        self.data = dokumen
        self.next = None


class PrinterQueue:
    def __init__(self):
        self.start = None
        self.rear = None

    def create_new_node(self, nama_file):
        return Node(nama_file)

    def insert_at_end(self, new_node):
        if self.start is None:
            self.start = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def delete_node(self):
        if self.start is None:
            print("Tidak ada dokumen")
        else:
            print(f"Mencetak: {self.start.data}")
            self.start = self.start.next
            if self.start is None:
                self.rear = None

    def display(self):
        if self.start is None:
            print("(antrian kosong)")
            return
        current = self.start
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def main():
    pq = PrinterQueue()

    while True:
        print("\n=== MENU PRINTER ===")
        print("1. Tambah dokumen")
        print("2. Cetak dokumen")
        print("3. Lihat antrian")
        print("4. Keluar")

        try:
            choice = int(input("Pilih: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if choice == 1:
            nama = input("Nama dokumen: ")
            node = pq.create_new_node(nama)
            pq.insert_at_end(node)

        elif choice == 2:
            pq.delete_node()

        elif choice == 3:
            pq.display()

        elif choice == 4:
            print("Program selesai!")
            break

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()
