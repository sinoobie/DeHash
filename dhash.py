import requests, os

os.system('clear')
w='\033[1;37m'
r='\033[1;31m'
g='\033[1;32m'
y='\033[1;33m'
print('''%s
  【D】【E】【C】【R】【Y】【P】【T】
 ('-. .-.   ('-.      .-')    ('-. .-. 
( OO )  /  ( OO ).-. ( OO ). ( OO )  / 
,--. ,--.  / . --. /(_)---\_),--. ,--. 
|  | |  |  | \-.  \ /    _ | |  | |  | 
|   .|  |.-'-'  |  |\  :` `. |   .|  | 
|       | \| |_.'  | '..`''.)|       | 
|  .-.  |  |  .-.  |.-._)   \|  .-.  | 
|  | |  |  |  | |  |\       /|  | |  | 
`--' `--'  `--' `--' `-----' `--' `--' 
%s  Author:KANG-NEWBIE (https://t.me/kang_nuubi)%s
 saya tidak menjamin semua hash ada di database
server karena yang punya server bukan saya XD %s
'''%(g,w,y,w))
type=input("Input Hash Type: ").lower()
hash=input("Input Hash: ")
email='nnb85353@zwoho.com'
code='9c512744205f079c'

req=requests.get('https://md5decrypt.net/Api/api.php?hash='+hash+'&hash_type='+type+'&email='+email+'&code='+code)
out=(req.content).decode("utf-8", "ignore")
print("\nResults:",out)
if 'CODE ERREUR : 001' in str(out):
	print("%sSudah mencapai limit harian"%(r))
elif 'CODE ERREUR : 002' in str(out):
	print("%sAda kesalahan di alamat email/code, mohon hubungi saya"%(r))
elif 'CODE ERREUR : 003' in str(out):
	print("%sPanjang Hash melebihin 400 karakter"%(r))
elif 'CODE ERREUR : 005' in str(out):
	print("%sHash yang di input tidak cocok dengan Type Hash yang di pilih"%(r))
elif 'CODE ERREUR : 006' in str(out):
	print("%sKesalahan Penulisan, priksa kembali"%(r))
