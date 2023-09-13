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

def main():
    way = input("Do you want to download a bunch or just 1? (1/Bunch) \n")
    if way == "1":
        url = input("Please copy your url: \n")
        download(url)
    if way == "Bunch":
        n = input("Enter the number of videos you want to download: \n")
        urls, i = [], 0
        while i < int(n):
            url = input("Please copy your url: \n")
            i += 1
            download(url)
        
    return 

main()