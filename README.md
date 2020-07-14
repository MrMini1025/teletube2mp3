youtube to mp3 telegram bot
For of 
https://github.com/thezawad/teletubemp3
____________________________________________________________________________________

#teletube2mp3
teletube2mp3 is a Telegram Bot which converts YouTube video(s) to mp3 and send directly to you
#screenshot
<img alt="yt" src="https://raw.githubusercontent.com/MrMini1025/teletube2mp3/master/Screenshot_20200714_131045.png" width="350">

### How does it work?

* It takes your command ( `yt videoname` )
* Uses `videoname` as a *keyword* to search in **YouTube**
* Takes the first link from YouTube
* Download that video using **youtube_dl** library
* Converts it into mp3 using **youtube_dl**
* Sends it to your chatbox

### Installation
```
git clone https://github.com/MrMini1025/teletube2mp3
cd teletube2mp3
pip install telepot
pip install urllib2
pip install requests
pip install bs4
pip install youtube_dl
apt-get install youtube-dl
apt-get install ffmpeg
```
Now create a file *api.txt* and put your **api-key**

### Run
While in the directly, run

`python ytgr.py`

You'll see 
```
[+] Server is Listenining [+]
[=] Type Command from Telegram [=]
```

### Usage
In your Telegram message box. Text

`yt URL

The Bot will find out the video from YouTube, converts it and send it to your Telegram.
