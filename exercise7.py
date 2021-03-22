#Christina Andrea Putri - Universitas Kristen Duta Wacana

# Perpustakaan komunitas meminjamkan buku dengan cara anggota perpustakaan harus menginput buku pinjaman 
# serta keterangan lainnya di sebuah program. Buku hanya bisa dipinjam max. 6 hari dan hanya bisa menginput
# 1 kali. Jika meminjam selama 4 hari, pada tanggal berapa buku harus dikembalikan ? 

#input : judul, jumlah, tanggal peminjaman, lama peminjaman
#proses : menghitung lama peminjaman dan menentukan tanggal pengembalian
#output : tanggal pengembalian

memb = input("Apakah Anda anggota perpustakaan? ")

while memb=="Ya" or memb=="ya":
    id_mem = input("ID anggota : ")
    judul = input("Judul buku :")
    jml = int(input("Jumlah buku: "))
    tgl_p = input("Tanggal peminjaman (DD/MM/YYYY): ")
    day = int(input("Lama peminjaman (hari): "))

    tgl_sp = tgl_p.split(" ")
    for i in tgl_sp:
        if day<7 and i[0].isdigit() and len(id_mem)==5:
            tgl = i.split("/")
            
            date = tgl[0]
            
            ft = int(date) + day
            
            ft = str(ft)
            print("Mohon dikembalikan pada tanggal ", ft+"/"+tgl[1]+"/"+tgl[2])
        elif day>=7 : 
            print("Peminjaman max. hanya 6 hari.")
        elif len(id_mem)!=5:
            print("Terdapat kesalahan dalam penulisan ID Anda. Silahkan coba lagi.")
        elif i[0]!=i[0].isdigit():
            print("Error")
    break
else : 
    print("Silahkan membuat ID perpusatakaan terlebih dahulu.")
