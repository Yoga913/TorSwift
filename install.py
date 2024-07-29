import os
choice = input('[+] untuk menginstal tekan (Y) untuk uninstall tekan (T) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 torswift.py')
    run('mkdir /usr/share/aut')
    run('cp torswift.py /usr/share/aut/torswift.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/aut/torswift.py "$@"')
    with open('/usr/bin/aut','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/aut & chmod +x /usr/share/aut/torswift.py')
    print('''\n\nselamat auto Tor Ip Changer berhasil diinstal \nmulai sekarang hanya type \x1b[6;30;42maut\x1b[0m di terminal ''')
if str(choice)=='T' or str(choice)=='t':
    run('rm -r /usr/share/aut ')
    run('rm /usr/bin/aut ')
    print('[!] sekarang Auto Tor Ip changer telah berhasil dihapus')
