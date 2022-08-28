

import os,time as t,getpass
t1 = t.sleep(1)
t2 = t.sleep(2)
t0 = t.sleep(0.5)
#COLORING
import colorama
from colorama import Fore
r ,w,g= Fore.RED,Fore.WHITE,Fore.GREEN
ceo =g+ '''▐██░▐█▀▀▒█▀█▀█░▐█▀▀░▐█▀█░▐█░▐█░
░█▌░▐█▀▀░░▒█░░░▐█▀▀░▐█──░▐████─
▐██░▐█▄▄░▒▄█▄░░▐█▄▄░▐█▄█░▐█░▐█░ '''+w
#COUNTDOWN
def count_down():
        time = 5
        while time <=0:
            time = time+1
            print(time)
            os.system('clear')
            print(ceo)
            os.system('time')
            if time == 5:
                break
                print('reached!!')
                
        
#TO CONTINUE
def con():
    a1 = getpass.getpass('\n \nenter any key to continue \n')

#UPDATE
def update():
    while True:
        os.system('rm -rf ie-tech')
        os.system('git clone https://github.com/isaac-easie/ie-tech') 
        print(g+'tool is successfully updated!')
        print (r+'wait a moment!.....'+w)
        t.sleep(2)
        print(g+'done!')
        con()
        os.system('clear')
        home()
        
#SHOW TOOLS
def available_tools():
    while True:
        os.system('clear')
        print (ceo)
        available_op = int(input('choose options \n1.>>phishing tool \n2.>>brute force tool \n3.>>home \n>>>'))
        if available_op == 1:
            os.system('rm -rf zphisher')
            os.system('git clone https://github.com/htr-tech/zphisher') 
            os.system('cd')
            os.system('cd zphisher')
            os.system('cd zphisher') 
            os.system('bash setup')
            os.system('bash nexphisher')
            break
        elif available_op == 2:
            os.system('rm -rf zphisher')
            os.system('git clone https://github.com/jaykali/maskphish')
            break
        elif available_op == 3:
            home()
        else:
            print ('invalid option!!')
            t.sleep(1)
            continue 
            
 #CONTACT
def contact():
	while True:
		os.system('clear')
		print(ceo)
		os.system('date')
		media = int(input('  choose media to contact  IE-tech \n  1.>>Whatsapp \n  2.>>E-mail \n  3.>>Telegram \n  4.>>Facebook \n  5.>>Home \n  >>>'))
		#whatsapp
		if media == 1:
			print('it may take some time for a reply to your issues...')
			print('contacting IE-tech on +256776515577 in a few seconds....##')
			t.sleep(1)
			count_down()
			
			os.system('xdg-open https://wa.me/+256776515577')
			break
		#e-mail
		elif media == 2:
			print('contacting IE-tech on ietech256.co@gmail.com in a few seconds....##')
			t.sleep(1)
			count_down()
			os.system('xdg-open ietech256.co@gmail.com')
			break
		#telegram
		elif media == 3:
			print('contacting IE-tech on +256776515577 in a few seconds....##')
			t.sleep(1)
			count_down()
			os.system('xdg-open https://t.me/+256776515577')
			break
		#facebook
		elif media == 5:
		    home()
		elif media  == 4:
			print('contacting IE-tech on facebook in a few seconds....##')
			t.sleep(1)
			count_down()
			os.system('xdg-open https://www.facebook.com/isaac.easie')
			break
		#if invalid
		else:
			print('invalid option!!!')
			t.sleep(2)
			continue

#DEF HOME
def home():
        while True:
            os.system('clear')
            print(ceo)
            os.system('date')
            home_op = int(input('\n  1.>>show tools \n  2.>>tool information \n  3.>>contact IE-TECH \n  4.>>update tool \n  5.>>quite \n  >>>'))
            if home_op == 1:
                available_tools()
            
            elif home_op == 2:
                print (ceo)
                print ('version 0.1')
                t. sleep(0.5)
                os.system('date')
                print ('\n \n \nthis tool was  programmed by isaac easie')
                t. sleep(0.5)
                print ('aimed at helping and guiding newbies to termux and kali linux to use some mostly used tools without any hard ways......')
                t. sleep(0.5)
                print ('this tool brings together other tools just to this one tool and solves the budded of running commands timely.')
                t. sleep(0.5)
                print ('\n \nthe tool may not yet be 100% good but with your participation,it can be improved')
                t. sleep(0.5)
                print ('make reports to us (IE-tech) incase of any issues  \n \nThanks very much for all your time.')
             
            elif home_op == 3:
                contact ()
                #code            
            elif home_op == 4:
                 update ()
             
            elif home_op == 5:
                print ('thanks for your time... ')
                break
                #code   
            else:
                print ('invalid entry!!')
                t. sleep(1)
                continue 
                #code

                #code   
home()  


		
   
	
