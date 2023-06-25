import os
from pytube import YouTube
from pytube import Playlist
from alive_progress import alive_it, alive_bar

FILE = input(
    "File path of text file with youtube URLS: (ENTER if /Desktop/in_yoto.txt) "
)

DIR_NAME = input(
    "Directory name for ~/Music/yoto_downloads: "
)

if FILE == "":
    to_get = open("/home/brad/Desktop/in_yoto.txt", "r")
else:
    to_get = open(FILE, "r")

# Convert playlists to indiv URLS

urls = to_get.readlines()


final_urls = []
for i in urls:
    # print(i)
    

    if 'playlist' in i:
        playlist_urls = Playlist(i)
        for i in playlist_urls:
            final_urls.append(i)
    else:
        final_urls.append(i)


# delete playlist urls

def get_vid(URL):
    yt = YouTube(URL,use_oauth=True)

    yt.streams.filter()

    stream = yt.streams.get_by_itag("140")
    stream.download(output_path="/home/brad/Desktop/raw_downloads")


if __name__ == "__main__":
        with alive_bar(len(final_urls), spinner="waves", bar="bubbles", title="Converting youtube vids to audio!") as bar:
            for i in final_urls:
                try:
                    get_vid(i)
                except:
                    print(f"URL: { i } bad ...")
                    pass
                bar()

        os.system(
            "audioconvert convert /home/brad/Desktop/raw_downloads /home/brad/Desktop/to_yoto"
        )
        os.system(f"cp -R /home/brad/Desktop/to_yoto/. /home/brad/Music/yoto_downloads/{ DIR_NAME }")
        os.system("rm -r /home/brad/Desktop/raw_downloads")
        print(
            """
            Copied files to ~/Music/yoto_downloads ...
            Now... opening my.yotoplay.com in brave ...
            
            """
        )
        os.system("brave-browser https://my.yotoplay.com")
