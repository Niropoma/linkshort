import os
import time
import pyshorteners
user = "niropoma"
password = "r2k"
logo = '''
 _______    ______   __    __ 
/       \  /      \ /  |  /  |
$$$$$$$  |/$$$$$$  |$$ | /$$/ 
$$ |__$$ |$$____$$ |$$ |/$$/  
$$    $$<  /    $$/ $$  $$<   
$$$$$$$  |/$$$$$$/  $$$$$  \  
$$ |  $$ |$$ |_____ $$ |$$  \ 
$$ |  $$ |$$       |$$ | $$  |
$$/   $$/ $$$$$$$$/ $$/   $$/ 
                              
                              
                              
'''

givenuser = input("Enter your user: ")
if givenuser == user:
  print("Correct user")
  givenpassword = input("Enter Your password: ")
  if givenpassword == password:
   print(" Wellcome to this tool")
   print(logo)
   
  else:
    print("incorrect password")
    time.sleep(2)
else:
  print("Wrong user")
  

link = input(" Enter your link :")
s = pyshorteners.Shortener()
provid = s.tinyurl.short(link)
print(f" Your short link is : {provid}")
  


