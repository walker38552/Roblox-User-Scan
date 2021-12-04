import requests as req

with open('last_scanned.txt','r')as file:
  x = int(file.read())+1

while True:
  html = req.get('https://www.roblox.com/users/'+str(x)+'/profile').text
  try:
    start = html.index('profileusername":"')+18
    end = html.index('","previoususer')
    print("User",html[start:end],"found.")
    with open('Users.txt','a')as file:
      ts = html[start:end],"ID:",str(x)
      ts = " ".join(ts)
      file.write(ts+'\n')
  except ValueError:
    print("User was terminated")
  x = x + 1
  with open('last_scanned.txt','w+')as file:
    file.write(str(x))
