import os

URL = "https://github.com/dtekinoglu/Cracking-the-coding-interview-solutions/archive/refs/heads/main.tar.gz"

os.system("wget "+URL) # Fetch zip file from Github
os.system("tar xvf "+ URL[URL.rfind("/")+1:])