import instaloader
import os, sys
BANNER = """\033[1;33m

 ___   __    _  _______  _______  _______  ___   __    _  _______  _______ 
|   | |  |  | ||       ||       ||   _   ||   | |  |  | ||       ||       |
|   | |   |_| ||  _____||_     _||  |_|  ||   | |   |_| ||    ___||   _   |
|   | |       || |_____   |   |  |       ||   | |       ||   |___ |  | |  |
|   | |  _    ||_____  |  |   |  |       ||   | |  _    ||    ___||  |_|  |
|   | | | |   | _____| |  |   |  |   _   ||   | | | |   ||   |    |       |
|___| |_|  |__||_______|  |___|  |__| |__||___| |_|  |__||___|    |_______|


\033[1;94m"""
E = "\033[1;92m"
H = "\033[1;93m"  
M = '\033[2;36m'
bot = instaloader.Instaloader()
print(BANNER)
os.system("termux-open-url https://t.me/termux_community_uz")
usertop=input(' FOYDALANUVCHI NOMINI KIRITING:   ')
profile = instaloader.Profile.from_username(bot.context, usertop)
print(type(profile))

print(E+"Foydalanuvchi nomi: ", profile.username)
print(M+"User ID: ", profile.userid)
print(E+"Postlarining soni: ", profile.mediacount)
print(M+"Podpischiklari: ", profile.followers)
print(E+"Podpisatsia tashaganlar soni: ", profile.followees)
print(M+"Biosi: ", profile.biography,profile.external_url)

posts = profile.get_posts(
