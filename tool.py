

import os,time as t,getpass
#pkgs
#print('colorama \n --upgrade pip')
#import colorama
#from colorama import Fore
ceo = '''▐██░▐█▀▀▒█▀█▀█░▐█▀▀░▐█▀█░▐█░▐█░
░█▌░▐█▀▀░░▒█░░░▐█▀▀░▐█──░▐████─
▐██░▐█▄▄░▒▄█▄░░▐█▄▄░▐█▄█░▐█░▐█░ '''
def update:
    while True:
        os.system('rm -rf ie-tech')
        os.system('git clone https://github.com/isaac-easie/ie-tech') 
        print('tool is successfully updated!')
        print ('wait a moment.....')
        t.sleep(2)
        os.system('clear')
def available_tools():
    while True:
        available_op = int(input('choose options \n1.>>phishing tool \n2.>>brute force tool \n3.>>home'))
        if available_op == 1:
            os.system('rm -rf zphisher')
            os.system('git clone https://github.com/htr-tech/zphisher') 
            os.system('cd zphisher') 
            #code
        elif available_op == 2:
            os.system('git clone https://github.com/htr-tech/zphisher')
                    
            
            #code
        elif available_op == 3:
            home()
            
            #code
        else:
            print ('invalid option!!')
            t.sleep(1)
            continue 
def contact():
	while True:
		os.system('clear')
		print(tn)
		media = int(input('  choose media to contact  IE-tech \n  1.>>Whatsapp \n  2.>>E-mail \n  3.>>Telegram \n  4.>>Facebook \n  5.>>Home \n  >>>'))
		#whatsapp
		if media == 1:
			print('it may take some time for a reply to your issues...')
			print('contacting IE-tech on +256776515577 in a few seconds....##')
			t.sleep(1)
			
			#os.system('xdg-open https://wa.me/+256776515577')
			break
		#e-mail
		elif media == 2:
			print('contacting IE-tech on ietech256.co@gmail.com in a few seconds....##')
			t.sleep(1)
			#os.system('xdg-open ietech256.co@gmail.com')
			break
		#telegram
		elif media == 3:
			print('contacting IE-tech on +256776515577 in a few seconds....##')
			t.sleep(1)
			#os.system('xdg-open https://t.me/+256776515577')
			break
		#facebook
		elif media == 5:
		    home()
		elif media  == 4:
			print('contacting IE-tech on facebook in a few seconds....##')
			t.sleep(1)
			#os.system('xdg-open https://www.facebook.com/isaac.easie')
			break
		#if invalid
		else:
			print('invalid option!!!')
			t.sleep(2)
			continue

#DEF HOME
def home():
        while True:
            print(ceo)
            #os.system('date')
            home_op = input('\n  1.>>show tools \n  2.>>tool information \n  3.>>contact IE-TECH \n  4.>>update tool \n  5.>>quite \n  >>>')
            if home_op == 1:
                print('the program is still being coded!!')
            
            elif home_op == 2:
                print (ceo)
                print ('version 0.1')
                t. sleep(0.5)
                #os.system('date')
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
                #code
             elif home_op == 5:
                print ('thanks for your time... ')
                break
                #code                   
             else:
                print ('invalid entry!!')
                t. sleep(1)
                continue 
                #code   
home()  
#DEF CONTACT

		
   
	
