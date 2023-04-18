from functions import *
def hapusjin(active_users,list_jin, list_candi):
    username_jin = input("Masukkan username jin: ")
    list_jin_baru = []      # Buat list kosong untuk menampung list jin yang tidak dihapus
    list_candi_baru = []    # Buat list kosong untuk menampung list candi yang tidak dihapus saat jin terhapus
    checker = False         # Untuk mengecek apakah jin ditemukan atau tidak

    for i in range (arr_len(list_jin)):         # Cari jin dalam users
        if username_jin != list_jin[i][0]:      # Jika username jin berbeda, maka masukkan jin yang berbeda tersebut ke dalam list_jin_baru
            list_jin_baru = konso(list_jin_baru, list_jin[i])
        else:       # Jika username jin ditemukan, ubah checker ke True pertanda jin sudah ditemukan
            checker = True

    if checker == False:    # Jika jin tidak ditemukan, tampilkan pesan pada layar bahwa jin tidak ditemukan
        print("Tidak ada jin dengan username tersebut.")
        list_jin = list_jin
    else:           # Jika jin ditemukan
        for j in range(arr_len(list_candi)):    # cari candi yang pembuatnya adalah jin dengan username yang dihapus
            if username_jin != list_candi[j][1]:    # bila candi bukan buatan jin yang dihapus, maka masukkan candi ke list_candi__baru
                list_candi_baru = konso(list_candi_baru, list_candi[j])
                
        determine = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ") # Input konfirmasi penghapusan
        while True:
            if determine == "y" or determine == "Y":        # Jika pilihan y atau Y maka penghapusan terjadi, maka berikan output list_jin_baru dan list_candi_baru
                print("Jin telah berhasil dihapus dari alam gaib.")
                list_jin[:] = list_jin_baru
                list_candi[:] = list_candi_baru
                break
            elif determine == "n" or determine == "N":      # Jika pilihan n atau N maka penghapusan tidak terjadi, maka kembalikan list awal yang diinputkan user
                print("Jin tidak jadi dihapus dari alam gaib.")
                list_jin[:] = list_jin
                list_candi[:] = list_candi
                break
            else:       # Jika pilihan ngaco, maka suruh player untuk mengulang sampai input benar
                print(f"Hanya menerima input y/n. Silahkan ulangi.")
                determine = input(f"Apakah anda yakin ingin menghapus jin dengan username {username_jin} (Y/N)? ")