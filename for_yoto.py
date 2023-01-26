import os
from pytube import YouTube


FILE = input(
    "File path of text file with youtube URLS: (enter if /Desktop/in_yoto.txt)"
)

if FILE == "":
    to_get = open("/home/brad/Desktop/in_yoto.txt", "r")
else:
    to_get = open(FILE, "r")


def get_vid(URL):
    yt = YouTube(URL)

    yt.streams.filter()

    stream = yt.streams.get_by_itag("140")
    stream.download(output_path="/home/brad/Desktop/raw_downloads")


if __name__ == "__main__":
    list(map(get_vid, to_get))
    os.system(
        "audioconvert convert /home/brad/Desktop/raw_downloads /home/brad/Desktop/to_yoto"
    )
    os.system("rm -r /home/brad/Desktop/raw_downloads")
    print(
        """
    
          Now... open my.yotoplay.com and upload
          
          """
    )
