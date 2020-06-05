#!/usr/bin/python2
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
#LO MAU RIKOD? BIAR KEREN GITU?
G0 = "\033[0;32m"
G1 = "\033[1;32m"
C0 = "\033[0;36m"
C1 = "\033[1;36m"
P0 = "\033[0;35m"
P1 = "\033[1;35m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
B0 = "\033[0;34m"
B1 = "\033[1;34m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"
Y1 = "\033[1;33m"
Y0 = "\033[0;33m"
import requests
import os
import time

def h1():
	cari=raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[1;37mMasukkan IP target: ')
	a=requests.get('https://api.hackertarget.com/aslookup/?q='+cari)
	print '%s[%s>%s] %sResult: \n%s'%(G1,Y1,G1,W1,a.text)
	print
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] Klik enter untuk back')
	main()
def h2():
	cari=raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[1;37mMasukkan IP target: ')
	a=requests.get('https://api.hackertarget.com/nping/?q='+cari)
	print '%s[%s>%s] %sResult: \n%s'%(G1,Y1,G1,W1,a.text)
	print
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] Klik enter untuk back')
	main()
def h3():
	cari=raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[1;37mMasukkan Web target: ')
	a=requests.get('https://api.hackertarget.com/dnslookup/?q='+cari)
	print '%s[%s>%s] %sResult: \n%s'%(G1,Y1,G1,W1,a.text)
	print
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] Klik enter untuk back')
	main()
def h4():
	cari=raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[1;37mMasukkan IP target: ')
	a=requests.get('https://api.hackertarget.com/reversedns/?q='+cari)
	print '%s[%s>%s] %sResult: \n%s'%(G1,Y1,G1,W1,a.text)
	print
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] Klik enter untuk back')
	main()
def h5():
	cari=raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[1;37mMasukkan IP target: ')
	a=requests.get('https://api.hackertarget.com/whois/?q='+cari)
	print '%s[%s>%s] %sResult: \n%s'%(G1,Y1,G1,W1,a.text)
	print
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] Klik enter untuk back')
	main()
def h6():
	cari=raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[1;37mMasukkan IP target: ')
	a=requests.get('https://api.hackertarget.com/geoip/?q='+cari)
	print '%s[%s>%s] %sResult: \n%s'%(G1,Y1,G1,W1,a.text)
	print
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] Klik enter untuk back')
	main()
def h7():
	cari=raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[1;37mMasukkan IP target: ')
	a=requests.get('https://api.hackertarget.com/reverseiplookup/?q='+cari)
	print '%s[%s>%s] %sResult: \n%s'%(G1,Y1,G1,W1,a.text)
	print
	y=raw_input('\033[1;37m[\033[1;31m?\033[1;37m] Save resultnya? y/n: ')
	if y == 'Y' or y == 'y':
		file=raw_input('\033[1;37m[\033[1;31m?\033[1;37m] Simpan: ')
		open(file,"a+").write(a.text+"\n")
	elif y == 'N' or y == 'n':
		main()
	else:
		main()
def h8():
	cari=raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[1;37mMasukkan Web target: ')
	a=requests.get('https://api.hackertarget.com/httpheaders/?q='+cari)
	print '%s[%s>%s] %sResult: \n%s'%(G1,Y1,G1,W1,a.text)
	print
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] Klik enter untuk back')
	main()
def h9():
	cari=raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[1;37mMasukkan Web target: ')
	a=requests.get('https://api.hackertarget.com/pagelinks/?q='+cari)
	print '%s[%s>%s] %sResult: \n%s'%(G1,Y1,G1,W1,a.text)
	print
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] Klik enter untuk back')
	main()

def logo():
	os.system('clear')
	print '''%s
._____________  ___________           .__          
|   \______   \ \__    ___/___   ____ |  |   ______
|   ||     ___/   |    | /  _ \ /  _ \|  |  /  ___/
|   ||    |       |    |(  <_> |  <_> )  |__\___ \ 
|___||____|       |____| \____/ \____/|____/____  >
                                                \/
[%s>%s] %sAnon Roz Team
'''%(G1,Y1,G1,W0)

def menu():
	print '''   %s[%s1%s] %sAS Lookup
   %s[%s2%s] %sTes ping
   %s[%s3%s] %sDNS Lookup
   %s[%s4%s] %sReverse DNS Lookup
   %s[%s5%s] %sWhois Lookup
   %s[%s6%s] %sGeoIP Lookup
   %s[%s7%s] %sReverse IP Lookup
   %s[%s8%s] %sHTTP Headers
   %s[%s9%s] %sPage Links
   %s[%s0%s] %sExit
'''%(W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,R1,W1,W0)
def main():
	try:
		logo()
		menu()
		pilih=raw_input("\033[1;32m[\033[1;33m?\033[1;32m] \033[0;37m@ImamSy > ")
		no=["1","2","3","4","5","6","7","8","9","0"]
		while pilih not in no:
			logo()
			menu()
			print "%s[%sx%s] %sPilihan Anda salah"%(W0,R1,W0,R0)
			pilih=raw_input("\033[1;32m[\033[1;33m?\033[1;32m] \033[0;37m@ImamSy > ")
		if pilih == '1' :
			logo()
			h1()
		elif pilih == '2' :
			logo()
			h2()
		elif pilih == '3' :
			logo()
			h3()
		elif pilih == '4' :
			logo()
			h4()
		elif pilih == '5' :
			logo()
			h5()
		elif pilih == '6' :
			logo()
			h6()
		elif pilih == '7' :
			logo()
			h7()
		elif pilih == '8' :
			logo()
			h8()
		elif pilih == '9' :
			logo()
			h9()
	except requests.exceptions.ConnectionError:
		exit("%s[%sx%s] %sTidak ada koneksi"%(W1,R1,W1,W0))

if __name__=='__main__':
	main()


