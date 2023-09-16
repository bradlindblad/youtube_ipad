
from alive_progress import alive_bar
import os
from pytube import YouTube

# Get inputs ------------------------------------

FILE = input(
    "File path of text file with youtube URLS: (ENTER if /Desktop/in_yoto.txt) "
)

d = input("Directory name for ~/Music/yoto_downloads: ")
DIR_NAME = f"/home/brad/Music/yoto_downloads/{ d }"

if FILE == "":
    to_get = open("/home/brad/Desktop/in_yoto.txt", "r")
else:
    to_get = open(FILE, "r")

# Convert playlists to indiv URLS

urls = to_get.readlines()

# Define functions ------------------------------

def get_vid(url):
        # Create a YouTube object by passing the URL of the video
        yt = YouTube(url)

        # Filter the available video streams to select only the audio stream
        video = yt.streams.filter(only_audio=True).first()

        # Download the selected audio stream and save it to a specified directory
        out_file = video.download(output_path=DIR_NAME)

        # Split the downloaded file path into the base name and extension
        base, ext = os.path.splitext(out_file)

        # Create a new file name with the '.mp3' extension
        new_file = base + '.mp3'

        # Rename the downloaded audio file to have the '.mp3' extension
        os.rename(out_file, new_file)
 
 
if __name__ == "__main__":
    # Iterate through a list of input video URLs or file paths
    with alive_bar(
        len(urls),
        spinner="waves",
        bar="bubbles",
        title="Converting youtube vids to audio!",
    ) as bar:
    
        for i in urls:
            try:
                get_vid(i)
            except:
                print(f"Bad url: {i}")
                pass
            bar()
        
    

    print(
        f"""
            Copied files to ~/Music/yoto_downloads{ d } ...
            Now... opening my.yotoplay.com in brave ...
            
            """
    )

    os.system("brave-browser https://my.yotoplay.com")

    os.system(f'xdg-open "{ DIR_NAME }"')

        
