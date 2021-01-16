import random, string
import datetime       
def transfer():
    print("* Transfer *")
    data = []
    saldo_sumber = 0
    saldo_tujuan = 0
    file = open("nasabah.txt", "r")
    for x in file:
        data.append(x.split(","))

    #mengecek rekening sumber
    while True:  
        rek_sumber = input("Masukkan nomor rekening sumber: ")
        cek_sumber = False
        for y in range(len(data)):
            if(data[y][0] == rek_sumber.upper()):
                print("--Nomor rekening sumber ditemukan atas nama " + data[y][1] + "--")
                saldo_sumber = data[y][2]
                cek_sumber = True
        if(cek_sumber == True):
            print()
            break #menghentikan while dan melanjutkan ke proses selanjutnya
        print("--Nomor rekening sumber tidak ditemukan--")

    #mengecek rekening tujuan
    while True:
        cek_tujuan = 0
        rek_tujuan = input("Masukkan nomor rekening tujuan: ")
        for z in range(len(data)):
            if(rek_sumber == rek_tujuan):
                cek_tujuan = 1
            elif(rek_sumber != rek_tujuan):
                if(data[z][0] == rek_tujuan.upper()):
                    print("--Nomor rekening tujuan ditemukan atas nama " + data[z][1] + "--")
                    saldo_tujuan = data[z][2]
                    cek_sumber = False
            elif(data[z][0] != rek_tujuan.upper()):
                    cek_sumber = True
        if(cek_sumber == False):
            print()
            break
        elif(cek_tujuan == 1):
            print("--Nomor rekening sumber tak boleh sama dengan nomor rekening tujuan")
        elif(cek_sumber == True):
            print("--Nomor rekening sumber tidak ditemukan--")
    
    #mengecek saldo transfer
    while True:
        saldo_transfer = int(input("Masukkan nominal yang akan ditransfer: "))
        if(int(saldo_sumber) >= int(saldo_transfer)):
            time = datetime.datetime.now() # waktu saat mentransfer
            print("--Transfer sebesar " + str(saldo_transfer) + " dari rekening " + rek_sumber.upper() + " ke rekening " + rek_tujuan.upper() + " berhasil--")
            break
        print("--Saldo tidak mencukupi. Transfer gagal--")
    file.close()
    file = open("nasabah.txt", "w+")
    for i in range(len(data)):
        if(data[i][0] == rek_sumber.upper()):
            saldo_awal = data[i][2]
            data[i][2] = int(saldo_awal) - saldo_transfer
    for j in range(len(data)):
        if(data[j][0] == rek_tujuan.upper()):
            saldo_awal = data[j][2]
            data[j][2] = int(saldo_awal) + saldo_transfer

    #menulis ulang pada file nasabah
    for e in range(len(data)):
        data_akhir = [data[e][0], data[e][1], data[e][2]]
        for element in data_akhir:
            file.writelines(str(element) + ",")
        file.write("\n")
    file.close()

    #menulis di file transfer
    no_transfer = "TRF" + ''.join(random.choice(string.digits) for _ in range(3))
    file = open("transfer.txt", 'a+')
    struk = [time.strftime("%x"), time.strftime("%X"), no_transfer, rek_sumber.upper(), rek_tujuan.upper(), saldo_transfer]
    for element in struk:
        file.writelines(str(element) + " ")
    file.write("\n")
    file.close()
    print()
transfer()