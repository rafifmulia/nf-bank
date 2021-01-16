import random, string
import datetime

print('***** SELAMAT DATANG DI NF BANK *****')

run = True
menu = ['Buka Rekening', 'Setoran Tunai', 'Tarik Tunai', 'Transfer', 'Lihat Daftar Transfer', 'Keluar']
dbNasabah = 'nasabah.txt'

def printMenu ():
  print('\nMenu')
  for key,val in enumerate(menu):
    print('[{}] {}'.format(key+1,val))

def listNasabah ():
  f = open(dbNasabah, 'r')
  val = f.readlines()
  f.close()
  return val

def getNasabah (norek=None):
  f = open(dbNasabah, 'r')
  val = None

  for readLine in f:
    dataNasabah = readLine.split(',') # [0]==norek, [1]==nama, [2]=saldo
    if (norek.upper() == dataNasabah[0]):
      dataNasabah[2] = dataNasabah[2].strip('\n')
      val = dataNasabah

  f.close()
  return val

def storeNasabah (norek, nama, saldo):
  nasabah = getNasabah(norek)
  f = open(dbNasabah, 'a')
  val = False
  saldo = int(saldo)

  if (nasabah == None):
    f.write(f'{norek},{nama},{saldo}\n')
    val = True

  f.close()
  return val

def addSaldoNasabah (norek, saldo):
  nasabahs = listNasabah()
  f = open(dbNasabah, 'w')
  val = False
  saldo = int(saldo)

  for nasabah in nasabahs:
    nasabah = nasabah.strip('\n').split(',') # [0]==norek, [1]==nama, [2]=saldo
    if (norek.upper() == nasabah[0]):
      f.write(f'{nasabah[0]},{nasabah[1]},{int(nasabah[2])+saldo}\n')
      val = True
    else:
      f.write(f'{nasabah[0]},{nasabah[1]},{nasabah[2]}\n')

  f.close()
  return val

def chooseMenu (inputMenu):
  if (inputMenu == '1'):
    bukaRekening()
    return 'match'
  elif (inputMenu == '2'):
    setoranTunai()
    return 'match'
  elif (inputMenu == '3'):
    tarik()
    return 'match'
  elif (inputMenu == '4'):
    transfer()
    return 'match'
  elif (inputMenu == '5'):
    cekTransaksi()
    return 'match'
  elif (inputMenu == '6'):
    return 'exit'
  else:
    return 'try'

def bukaRekening ():
  print('\n*** BUKA REKENING ***')
  nama = input('Masukkan nama Anda: ')
  saldo = input('Masukkan setoran awal: ')
  norek = "REK" + ''.join(random.choice(string.digits) for _ in range(3))

  if (storeNasabah(norek, nama, saldo)):
    print('Pembukaan rekening dengan nomor {} atas nama {} berhasil.'.format(norek,nama))
  else:
    print('Mohon maaf pembukaan rekening dengan nomor {} atas nama {} gagal. Silahkan coba lagi.'.format(norek,nama))

def setoranTunai ():
  print('\n*** SETORAN TUNAI ***')
  norek = input('Masukkan nomor rekening: ')
  saldo = input('Masukkan nominal yang akan disetor: ')

  if (addSaldoNasabah(norek, saldo)):
    print('Setoran tunai sebesar {} ke rekening {} berhasil.'.format(saldo,norek))
  else:
    print('Nomor rekening tidak terdaftar. Setoran tunai gagal.')

def tarik():
    print("*** TARIK TUNAI ***")
    norek = input('Masukkan nomor rekening: ')
    saldo = input('Masukkan nominal yang akan ditarik: ')

    result = tarikTunai(norek, saldo)
    if (result == '200'):
      print('Tarik tunai sebesar {} dari rekening {} berhasil.'.format(saldo, norek.upper()))
    elif (result == '400'):
      print('Saldo tidak mencukupi. Tarik tunai gagal.')
    else:
      print('Nomor rekening tidak terdaftar. Tarik tunai gagal.')

def tarikTunai(norek, saldo):
    nasabahs = listNasabah()
    f = open(dbNasabah, 'w')
    val = '500'
    saldo = int(saldo)
    for nasabah in nasabahs:
      nasabah = nasabah.strip('\n').split(',') # [0]==norek, [1]==nama, [2]=saldo
      if (norek.upper() == nasabah[0]):
        if (int(nasabah[2]) < saldo):
          f.write(f'{nasabah[0]},{nasabah[1]},{nasabah[2]}\n')
          val = '400'
        else:
          f.write(f'{nasabah[0]},{nasabah[1]},{int(nasabah[2])-saldo}\n')
          val = '200'
      else:
        f.write(f'{nasabah[0]},{nasabah[1]},{nasabah[2]}\n')
    f.close()
    return val

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
                print("Nomor rekening sumber ditemukan atas nama " + data[y][1])
                saldo_sumber = data[y][2]
                cek_sumber = True
        if(cek_sumber == True):
            print()
            break #menghentikan while dan melanjutkan ke proses selanjutnya
        print("Nomor rekening sumber tidak terdaftar")

    #mengecek rekening tujuan
    while True:
        cek_tujuan = 0
        rek_tujuan = input("Masukkan nomor rekening tujuan: ")
        for z in range(len(data)):
            if(rek_sumber == rek_tujuan):
                cek_tujuan = 1
            elif(rek_sumber != rek_tujuan):
                if(data[z][0] == rek_tujuan.upper()):
                    print("Nomor rekening tujuan ditemukan atas nama " + data[z][1])
                    saldo_tujuan = data[z][2]
                    cek_sumber = False
            elif(data[z][0] != rek_tujuan.upper()):
                    cek_sumber = True
        if(cek_sumber == False):
            print()
            break
        elif(cek_tujuan == 1):
            print("Nomor rekening sumber tak boleh sama dengan nomor rekening tujuan")
        elif(cek_sumber == True):
            print("Nomor rekening sumber tidak ditemukan")
    
    #mengecek saldo transfer
    while True:
        saldo_transfer = int(input("Masukkan nominal yang akan ditransfer: "))
        if(int(saldo_sumber) >= int(saldo_transfer)):
            time = datetime.datetime.now() # waktu saat mentransfer
            print("Transfer sebesar " + str(saldo_transfer) + " dari rekening " + rek_sumber.upper() + " ke rekening " + rek_tujuan.upper() + " berhasil")
            break
        print("Saldo tidak mencukupi. Transfer gagal")
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
          file.writelines(str(element).strip('\n') + ",")
        file.write("\n")
    file.close()

    #menulis di file transfer
    no_transfer = "TRF" + ''.join(random.choice(string.digits) for _ in range(3))
    file = open("transfer.txt", 'a+')
    struk = [no_transfer, rek_sumber.upper(), rek_tujuan.upper(), saldo_transfer]
    for element in struk:
        file.writelines(str(element) + ",")
    file.write("\n")
    file.close()
    print()
    
def cekTransaksi():
  print('** LIHAT DATA TRANSFER **')
  norek = input('Masukkan nomor rekening: ')
  nb = open("nasabah.txt", 'r')
  b = False
  for a in nb:
      z = a.strip('\n').split(',')
      if (norek.upper() == z[0]):
          b = True
  if b == False:
      print('No rekening tidak ditemukan')
      return False

  tf = open("transfer.txt", 'r')
  val = []

  for transaksi in tf:
      # [0]==Kode Transfer, [1]==Rekening Sumber, [2]=Rekening Tujuan, [3]=Nominal Transfer
      log = transaksi.strip('\n').split(',')
      if (norek.upper() == log[1]):
          val.append(log)
  if (len(val) > 0):
      for x in val:
          print(x[0], x[1], x[2], x[3])
  else:
      print('Tidak ada data yang ditampilkan')
  tf.close()
  return val

# try:
while run:
  printMenu()
  
  runInput = True
  while runInput:
    inputMenu = input('Masukkan menu pilihan Anda: ')
    if (chooseMenu(inputMenu) == 'match'):
      runInput = False
    elif (chooseMenu(inputMenu) == 'exit'):
      runInput = False
      run = False
    else: # == 'try'
      print('Pilihan Anda salah. Ulangi.')

  if (run == False):
    print('Terima kasih atas kunjungan Anda...')
# except:
#   print('Program error')