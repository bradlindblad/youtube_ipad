

from pytube import YouTube

daniel = 'https://www.youtube.com/watch?v=MqJl0dzYYuA'
baby_moses = 'https://www.youtube.com/watch?v=qn8gmYOmk7s'
joseph = 'https://www.youtube.com/watch?v=oosM99f5KeQ'
goliath = 'https://www.youtube.com/watch?v=O7phn_d0Cok'
other = 'https://www.youtube.com/watch?v=02-ZpAX3JGQ'
summer_bible_songs = 'https://www.youtube.com/watch?v=yBYTqO9myMI'

to_get = [daniel, baby_moses, joseph, goliath, other, summer_bible_songs]

def get_vid(URL):
    yt = YouTube(URL)

    yt.streams.filter()

    stream = yt.streams.get_by_itag('18')
    stream.download(output_path="/home/brad/Desktop")


if __name__ == '__main__':
    list(map(get_vid, to_get))

