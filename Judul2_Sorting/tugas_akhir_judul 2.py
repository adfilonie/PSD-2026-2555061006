def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                tukar(arr, j, j + 1)


def main():
    try:
        n = int(input("Jumlah siswa: "))
    except ValueError:
        print("Input harus angka")
        return

    nilai_siswa = []

    print("Masukkan nilai siswa:")
    for i in range(n):
        while True:
            try:
                nilai = int(input(f"Nilai siswa ke-{i+1}: "))
                nilai_siswa.append(nilai)
                break
            except ValueError:
                print("Masukkan angka yang valid!")

    print("\nNilai sebelum diurutkan:")
    print(nilai_siswa)

    bubble_sort(nilai_siswa, n)

    print("\nNilai setelah diurutkan (terendah ke tertinggi):")
    for nilai in nilai_siswa:
        print(nilai, end=" ")
    print()


if __name__ == "__main__":
    main()
