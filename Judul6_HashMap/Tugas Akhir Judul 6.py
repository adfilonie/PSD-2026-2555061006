class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.kode_produk = None
        self.harga = None
        self.state = SlotState.EMPTY


class HashMapProduk:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, kode_produk):
        return (kode_produk % self.SIZE + self.SIZE) % self.SIZE

    def tambah_produk(self, kode_produk, harga):
        idx = self.hash_function(kode_produk)

        first_deleted = -1

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.OCCUPIED:

                if self.table[i].kode_produk == kode_produk:
                    self.table[i].harga = harga
                    return True

            elif self.table[i].state == SlotState.DELETED:

                if first_deleted == -1:
                    first_deleted = i

            else:
                if first_deleted != -1:
                    i = first_deleted

                self.table[i].kode_produk = kode_produk
                self.table[i].harga = harga
                self.table[i].state = SlotState.OCCUPIED

                return True

        if first_deleted != -1:
            self.table[first_deleted].kode_produk = kode_produk
            self.table[first_deleted].harga = harga
            self.table[first_deleted].state = SlotState.OCCUPIED

            return True

        return False

    def cari_produk(self, kode_produk):
        idx = self.hash_function(kode_produk)

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.EMPTY:
                return None

            if (
                self.table[i].state == SlotState.OCCUPIED
                and self.table[i].kode_produk == kode_produk
            ):
                return self.table[i]

        return None

    def hapus_produk(self, kode_produk):
        entry = self.cari_produk(kode_produk)

        if entry is None:
            return False

        entry.state = SlotState.DELETED

        return True

    def tampilkan_produk(self):
        print("\nData Produk Minimarket:")

        for i in range(self.SIZE):

            print(f"{i}: ", end="")

            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")

            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")

            else:
                print(
                    f"(Kode: {self.table[i].kode_produk}, Harga: {self.table[i].harga})"
                )


def main():
    produk = HashMapProduk()

    produk.tambah_produk(101, 5000)
    produk.tambah_produk(111, 12000)
    produk.tambah_produk(121, 7000)
    produk.tambah_produk(102, 15000)

    produk.tampilkan_produk()

    hasil = produk.cari_produk(111)

    if hasil is not None:
        print(f"\nProduk ditemukan, harga = {hasil.harga}")

    else:
        print("\nProduk tidak ditemukan")

    produk.hapus_produk(111)

    print("\nSetelah menghapus produk 111:")

    produk.tampilkan_produk()

    hasil = produk.cari_produk(121)

    if hasil is not None:
        print(f"\nProduk 121 masih ditemukan, harga = {hasil.harga}")

    else:
        print("\nProduk tidak ditemukan")


if __name__ == "__main__":
    main()
