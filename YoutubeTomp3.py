from pytube import YouTube
def download(url):
    try:
        video = YouTube(url)
        yt = video 
        stream = video.streams.filter(only_audio=True).first()
        stream.download(output_path="C:/Users/hilar/Music", filename=f"{video.title} - SnowMan.mp3")
        print("The video is downloaded in MP3")
    except KeyError:
        print("Unable to fetch video information. Please check the video URL or your network connection.")
    return 

def downloadABunch(urls):
    for url in urls:
        download(url)
    return 
