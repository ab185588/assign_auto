from pytube import YouTube



def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path='downloads/')
    except:
        print("An error has occurred")
    print("Download is completed successfully")



links = ["https://www.youtube.com/watch?v=gH_RYRwVrVM"]
for i in range(len(links)):
  Download(links[i])