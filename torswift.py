# -*- coding: utf-8 -*-
# Program Python ini dirancang untuk mengotomatisasi proses pergantian alamat IP menggunakan Tor. 

import time
import os
import subprocess

# # 1. **Pernyataan Impor**:
#   - Modul `time`, `os`, dan `subprocess` diimpor untuk menangani operasi terkait waktu, perintah sistem, dan manajemen subprocess, secara berturut-turut.
#   - Modul `requests` diimpor untuk melakukan permintaan HTTP.

try:
    check_pip3 = subprocess.check_output('dpkg -s python3-pip', shell=True)
    if str('install ok installed') in str(check_pip3):
        pass
except subprocess.CalledProcessError:
    print('[+] pip3 tidak diinstal')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install python3-pip -y', shell=True)
    print('[!] pip3 berhasil diinstal')
try:

    import requests
except Exception:
    print('[+] permintaan python3 tidak diinstal')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] permintaan python3 diinstal ')
try:

    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:

    print('[+] tor tidak diinstal !')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print('[!] tor berhasil diinstal ')
# 2. **Pengecekan Ketergantungan**:
#   - Skrip pertama-tama mencoba memeriksa apakah `python3-pip` terpasang dengan menjalankan `dpkg -s python3-pip` menggunakan subprocess. Jika tidak, dipasang.
#   - Selanjutnya, mencoba untuk mengimpor `requests`. Jika tidak berhasil, memasang `requests` dan `requests[socks]` menggunakan `pip3`.  
#   - Kemudian, memeriksa apakah Tor terpasang dengan memeriksa keberadaan perintah `tor`. Jika tidak, dipasang Tor.

os.system("clear")
def ma_ip():
    url='https://www.myexternalip.com/raw'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
    return get_ip.text
# 3. **Hapus Layar Konsol**:
#   - Membersihkan layar konsol menggunakan `os.system("clear")`.

def change():
    os.system("service tor reload")
    print ('[+] IP Anda telah diubah menjadi : '+str(ma_ip()))
# 4. **Definisikan Fungsi**:
#   - `ma_ip()`: Mengambil alamat IP eksternal menggunakan layanan `myexternalip.com` melalui permintaan HTTP melalui Tor.
#   - `change()`: Memuat ulang layanan Tor untuk mengubah alamat IP dan mencetak alamat IP baru yang diperoleh menggunakan `ma_ip()`.

print('''\033[1;32;40m \n

████████  ██████  ██████      ███████ ██     ██ ██ ███████ ████████ 
   ██    ██    ██ ██   ██     ██      ██     ██ ██ ██         ██    
   ██    ██    ██ ██████      ███████ ██  █  ██ ██ █████      ██    
   ██    ██    ██ ██   ██          ██ ██ ███ ██ ██ ██         ██    
   ██     ██████  ██   ██     ███████  ███ ███  ██ ██         ██    
''')
print("\033[1;40;31m Dibuat Oleh:[Yoga913](https://github.com/Yoga913)/\n")
# 5. **Tampilkan Pesan Selamat Datang**:
#   - Mencetak pesan selamat datang dengan informasi versi skrip dan kredit.

os.system("service tor start")

# 6. **Mulai Layanan Tor**:
#   - Memulai layanan Tor menggunakan `os.system("service tor start")`.


time.sleep(3)
print("\033[1;32;40m Ubah SOCKES Anda menjadi 127.0.0.1:9050\n")
os.system("service tor start")
x = input("[+] waktu untuk mengubah Ip dalam Detik [type=60] >> ")
lin = input("[+] berapa kali Anda ingin mengubah ip Anda [type=1000] untuk jenis perubahan ip tak terbatas [0] >>")
          # 7. **Interaksi Pengguna**:
          #   - Meminta pengguna untuk mengatur proksi SOCKS mereka menjadi `127.0.0.1:9050`.
          #   - Meminta masukan pada interval waktu (`x`) antara perubahan IP dan jumlah kali perubahan IP (`lin`).
if int(lin) ==int(0):

	while True:
		try:
			time.sleep(int(x))
			change()
		except KeyboardInterrupt:
		print('\ntor otomatis ditutup ')
        quit()

else:
	for i in range(int(lin)):
		    time.sleep(int(x))
            change()

# 8. **Loop Pergantian IP**:
#   - Jika jumlah pergantian IP diatur ke tak terbatas (yaitu, `lin == 0`), masuk ke loop tak terbatas di mana ia menunggu waktu yang ditentukan (`x`) dan kemudian memanggil fungsi `change()` untuk mengubah IP.
#   - Jika jumlah pergantian IP tertentu disebutkan, akan melakukan iterasi sebanyak `lin` kali, menunggu `x` detik antara setiap perubahan, dan memanggil `change()`.

# Fungsi `change()` bertanggung jawab atas mengubah alamat IP dengan memuat ulang layanan Tor dan menampilkan alamat IP baru. Loop utama mengontrol frekuensi dan jumlah perubahan IP berdasarkan masukan pengguna.

