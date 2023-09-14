from pytube import YouTube
import threading

def download_video(url, output_path):
    try:
        video = YouTube(url)
        stream = video.streams.filter(only_audio=True).first()
        stream.download(output_path=output_path, filename=f"{video.title} - SnowMan.mp3")
        print(f"The video {video.title} is downloaded in MP3")
    except Exception as e:
        print(f"Error downloading video from {url}: {e}")

def download_videos(urls, output_path):
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_video, args=(url, output_path))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

def main():
    way = input("Do you want to download a bunch or just 1? (1/Bunch) \n")
    output_path = "C:/Users/hilar/Music"
    
    if way == "1":
        url = input("Please copy your url: \n")
        download_video(url, output_path)
    
    elif way == "Bunch":
        n = int(input("Enter the number of videos you want to download: \n"))
        urls = [input("Please copy your url: \n") for _ in range(n)]
        download_videos(urls, output_path)
if __name__ == "__main__":
    main()
