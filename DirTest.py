import re,requests
requests.packages.urllib3.disable_warnings()

print("""
	_________________________________________| \033[94mBeta\033[0m |____

	██████╗ ██╗██████╗ ████████╗███████╗███████╗████████╗
	██╔══██╗██║██╔══██╗╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
	██║  ██║██║██████╔╝   ██║   █████╗  ███████╗   ██║   
	██║  ██║██║██╔══██╗   ██║   ██╔══╝  ╚════██║   ██║   
	██████╔╝██║██║  ██║   ██║   ███████╗███████║   ██║ 
	╚═════╝ ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝   ╚═╝ 

	\033[1mFrom\033[0m: 	CryptoGen Nepal \033[94m\033[1m(@CryptoGenNepal)\033[0m
		https://CryptoGenNepal.com

	\033[1mAuthor\033[0m: #Nittam \033[94m\033[1m(@TheNittam)\033[0m
		https://nirmaldahal.com.np
	_____________________________________________________
""")
regex='<a href=\\"(.*?)\\">'
def link(url):
	I='\x1b[0m';E=False;D='/';C=url;F=requests.get(C,verify=E);A=re.findall(regex,F.text)
	for B in range(1,len(A)):
		if'.'in A[B]:
			G=requests.get(C+D+A[B],verify=E)
			if G.status_code==200:print('File\t: \x1b[94m'+C+D+A[B]+I)
		elif A[B]==D:print(end='')
		elif D in A[B]:
			H=requests.get(C+D+A[B],verify=E)
			if H.status_code==200:print('Folder\t: \x1b[93m'+C+D+A[B]+I);link(C+D+A[B])
			else:print(end='')
print('\x1b[4mDirTest\x1b[0m > set \x1b[1mDirectory Listing Path\x1b[0m')
url=input('\x1b[4mDirTest\x1b[0m Scanner(\x1b[1m\x1b[91mDirectory Listing Path\x1b[0m) > set HOST ')
print(end='\n')
link(url)
