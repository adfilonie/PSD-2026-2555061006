class Node:
    def __init__(self, nilai):
        self.key = nilai
        self.left = None
        self.right = None


class BSTNilaiMahasiswa:
    def __init__(self):
        self.root = None

    def insert_node(self, root, nilai):
        if root is None:
            return Node(nilai)

        if nilai < root.key:
            root.left = self.insert_node(root.left, nilai)

        elif nilai > root.key:
            root.right = self.insert_node(root.right, nilai)

        return root

    def tambah_nilai(self, nilai):
        self.root = self.insert_node(self.root, nilai)

    def search_node(self, root, nilai):
        if root is None:
            return False

        if root.key == nilai:
            return True

        if nilai < root.key:
            return self.search_node(root.left, nilai)

        return self.search_node(root.right, nilai)

    def cari_nilai(self, nilai):
        return self.search_node(self.root, nilai)

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        print(root.key, end=" ")
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return

        print(root.key, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.key, end=" ")

    def nilai_terendah(self, root):
        if root is None:
            return -1

        current = root

        while current.left is not None:
            current = current.left

        return current.key

    def nilai_tertinggi(self, root):
        if root is None:
            return -1

        current = root

        while current.right is not None:
            current = current.right

        return current.key

    def jumlah_data(self, root):
        if root is None:
            return 0

        return 1 + self.jumlah_data(root.left) + self.jumlah_data(root.right)

    def total_nilai(self, root):
        if root is None:
            return 0

        return root.key + self.total_nilai(root.left) + self.total_nilai(root.right)


def main():
    bst = BSTNilaiMahasiswa()

    pilih = 0

    while pilih != 10:
        print("\n=== SISTEM DATA NILAI MAHASISWA ===")
        print("1. Tambah nilai")
        print("2. Cari nilai")
        print("3. Tampilkan inorder")
        print("4. Tampilkan preorder")
        print("5. Tampilkan postorder")
        print("6. Nilai terendah")
        print("7. Nilai tertinggi")
        print("8. Jumlah data")
        print("9. Total nilai")
        print("10. Keluar")

        try:
            pilih = int(input("Pilih menu: "))

        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                nilai = int(input("Masukkan nilai mahasiswa: "))
                bst.tambah_nilai(nilai)

                print(f"Nilai {nilai} berhasil ditambahkan")

            except ValueError:
                print("Input harus angka!")

        elif pilih == 2:
            try:
                nilai = int(input("Cari nilai: "))

                if bst.cari_nilai(nilai):
                    print("Nilai ditemukan")

                else:
                    print("Nilai tidak ditemukan")

            except ValueError:
                print("Input harus angka!")

        elif pilih == 3:
            print("Inorder: ", end="")
            bst.inorder(bst.root)
            print()

        elif pilih == 4:
            print("Preorder: ", end="")
            bst.preorder(bst.root)
            print()

        elif pilih == 5:
            print("Postorder: ", end="")
            bst.postorder(bst.root)
            print()

        elif pilih == 6:
            print(f"Nilai terendah: {bst.nilai_terendah(bst.root)}")

        elif pilih == 7:
            print(f"Nilai tertinggi: {bst.nilai_tertinggi(bst.root)}")

        elif pilih == 8:
            print(f"Jumlah data: {bst.jumlah_data(bst.root)}")

        elif pilih == 9:
            print(f"Total seluruh nilai: {bst.total_nilai(bst.root)}")

        elif pilih == 10:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
