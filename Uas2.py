from collections import deque

dq = deque()

while True:
    print("\n===== MENU DEQUE =====")
    print("a) Append (kanan)")
    print("b) AppendLeft (kiri)")
    print("c) Pop (kanan)")
    print("d) PopLeft (kiri)")
    print("e) Clear")
    print("f) Keluar")

    menu = input("Pilih menu: ").lower()

    if menu == 'a':
        val = input("Masukkan data: ")
        dq.append(val)
        print("-> Data ditambahkan di kanan:", val)

    elif menu == 'b':
        val = input("Masukkan data: ")
        dq.appendleft(val)
        print("-> Data ditambahkan di kiri:", val)

    elif menu == 'c':
        if len(dq) == 0:
            print("Deque kosong!")
        else:
            print("-> Data dihapus dari kanan:", dq.pop())

    elif menu == 'd':
        if len(dq) == 0:
            print("Deque kosong!")
        else:
            print("-> Data dihapus dari kiri:", dq.popleft())

    elif menu == 'e':
        dq.clear()
        print("-> Semua data berhasil dihapus.")

    elif menu == 'f':
        print("Keluar program...")
        break

    else:
        print("Pilihan tidak valid!")

    print("Isi deque sekarang:", list(dq))
