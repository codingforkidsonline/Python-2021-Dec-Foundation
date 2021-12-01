from gtts import gTTS   
import os 
  
mytext = 'Welcome to One Target December Python holiday bootcamp. Hope you enjoy this camp and learn some interesting coding skill in Python.'
language = 'en'

#mytext = '欢迎参加One Target的12月假期Python编程集训班。希望你喜欢这个课程，学到有趣的Python编程技巧。'
#language = 'zh-cn'
  
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
myobj.save("welcome.mp3") 
  
os.system("open welcome.mp3")


