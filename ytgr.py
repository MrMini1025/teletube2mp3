#!/usr/bin/python
import time
import subprocess
import telepot
import os
import urllib3
import re
import json
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import youtube_dl

def handle(msg):
        chat_id = msg['chat']['id']
        command = msg['text']

        print("Command from client : %s " %command)

    #youtube search
        if command.startswith('yt'):
            param = command[3:]
            response = urlopen(param)
            data = response.read()
            response.close()
            soup = BeautifulSoup(data,"html.parser")
            metas = soup.find_all('meta')
            vid = [ meta.attrs['content'] for meta in metas if 'itemprop' in meta.attrs and meta.attrs['itemprop'] == 'name' ]
            link = str(param)
            print(link)
            watchid = param[32:]
            titlen = str(vid)
            title = titlen[2:-2]
            print(title)
            print(watchid)
            bot.sendMessage(chat_id,title+"\n"+"Downloading...")
            print(param)
            options = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320'
                }]
            }
            filename = title+"-"+watchid+".mp3"
            #filename = filename.replace(" ","_")
            #filename = filename.replace("'","")
            #filename = filename.replace("&","")
            #filename = filename.replace("__","_")
            #filename = filename.replace(",","")
            #filename = filename.replace("(","")
            #filename = filename.replace(")","")
           # filename = filename.replace("[","")
            #filename = filename.replace("]","")
           # filename = filename.replace("{","")
          #  filename = filename.replace("}","")
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([link])
                newfilename = title+".mp3"
                os.rename(filename, newfilename)
                bot.sendAudio(chat_id,audio=open(newfilename,'rb'))
                print("Sent!"+"\n"+title)
                os.remove(newfilename)
    #end youtube search



#api credentials
api = open('api.txt','r')
api_cont = api.read().strip()
bot = telepot.Bot(api_cont)
bot.message_loop(handle)
print('[+] Server is Listenining [+]')
print('[=] Type Command from Telegram [=]')

while 1:
        time.sleep(10)
