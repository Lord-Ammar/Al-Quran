import os,sys,time,requests
ip = requests.get('https://api.ipify.org').text
print ("   \033[1;95m[\033[1;90m•\033[1;95m]\033[1;96m Your Ip\033[1;93m: \033[1;92m"+ip)
