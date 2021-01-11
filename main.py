import random, string

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