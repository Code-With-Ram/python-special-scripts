
#importing the module 
from pytube import YouTube 
import sys  
  
#link of the video to be downloaded 
link=""
  
try: 
    #object creation using YouTube which was imported in the beginning 
    yt = YouTube(link) 
except: 
    print("Connection Error") #to handle exception 
    sys.exit(0)
stream = yt.streams.first()
stream.download()
try: 
    #downloading the video 
    d_video.download(SAVE_PATH) 
except: 
    print("Some Error!") 
print('Task Completed!') 
