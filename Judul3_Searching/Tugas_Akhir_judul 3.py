def sequential_search(absensi, nama):
    for data in absensi:
        if data.lower() == nama.lower():
            return True
    return False


def main():
    absensi = ["Naufal", "Dave", "Azka", "Ridho", "Arif"]

    print("=== Sistem Cek Kehadiran ===")
    print("Data absensi:", absensi)

    nama = input("Masukkan nama mahasiswa: ")

    ditemukan = sequential_search(absensi, nama)

    if ditemukan:
        print(f"Mahasiswa {nama} hadir.")
    else:
        print(f"Mahasiswa {nama} tidak hadir.")


if __name__ == "__main__":
    main()
