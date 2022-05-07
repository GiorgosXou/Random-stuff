# Playing live audio with python [7-5-2022]
[live_audio_player.py](https://github.com/GiorgosXou/Random-stuff/blob/main/Programming/Python/live_audio_player.py) | An *(semi\kind-of working)* attempt of streaming audio in a pythonic(?) way and without the use of vlc module [...]
```python
import requests, pyaudio, io
from pydub import AudioSegment

stream_url = "http://realfm.live24.gr:80/realfm"
r = requests.get(stream_url, stream=True)
p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                channels=2,
                rate=44100,
                output=True)

for block in r.iter_content(1024 * 150):
    stream.write(AudioSegment.from_file(io.BytesIO(block), format="mp3")._data, exception_on_underflow=False) # m4a for YT?

stream.stop_stream()
stream.close()
```


# Resources
References\Releated Topics\Searches across the internet about the subject of Audio and Streaming.

* ***Python Projects related to Audio:***
* * [spotui](https://github.com/ceuk/spotui)
* * [spotipy](https://github.com/plamere/spotipy)
* * [just_playback](https://github.com/cheofusi/just_playback)
* * [pafy](https://github.com/mps-youtube/pafy)
* * [twitch-realtime-handler](https://github.com/adrz/twitch-realtime-handler)
* * [pithos](https://github.com/pithos/pithos)
* * [Pydub](https://github.com/jiaaro/pydub)
* ***StackOverflow:***
* * ***Releated Issues (?):***
* * * [Playing live audio from a website using PyAudio](https://stackoverflow.com/questions/45129089/playing-live-audio-from-a-website-using-pyaudio)
* * * [Opening wav from URL in Python](https://stackoverflow.com/questions/70872076/opening-wav-from-url-in-python)
* * * [Pydub playback from queue](https://stackoverflow.com/questions/65568510/pydub-playback-from-queue)
* * * [Read audio stream from an Icecast2 URL and re-stream it using Flask](https://stackoverflow.com/questions/60149615/read-audio-stream-from-an-icecast2-url-and-re-stream-it-using-flask)
* * * [How to play mp3 from bytes?](https://stackoverflow.com/questions/43941716/how-to-play-mp3-from-bytes)
* * * [Python stream audio from YouTube livestream](https://stackoverflow.com/questions/68522350/python-stream-audio-from-youtube-livestream)
* * * [Is there a way to directly stream audio from a youtube video using youtube-dl or pafy library in python 3.7?](https://stackoverflow.com/questions/60745020/is-there-a-way-to-directly-stream-audio-from-a-youtube-video-using-youtube-dl-or)
* * ***"Random":***
* * * [FileNotFoundError: Could not find module 'libvlc.dll'](https://stackoverflow.com/questions/59014318/filenotfounderror-could-not-find-module-libvlc-dll)
* * * [ImportError: No module named youtube_dl](https://stackoverflow.com/questions/44348032/importerror-no-module-named-youtube-dl)
* ***Other Related (?):***
* * [Streaming MP3's from the internet.](https://www.reddit.com/r/learnpython/comments/3xxx86/streaming_mp3s_from_the_internet/)
* * [How can I play audio stream without saving it into the file with pyglet?](https://tousu.in/qa/?qa=1137598/)
* * [decode mp3 stream with python streamp3](https://serveanswer.com/questions/decode-mp3-stream-with-python-streamp3)
* * [stream - Record streaming and saving internet radio in python](https://qa.wujigu.com/qa/?qa=959418/)
* * [Playing MP3 Files in Python with Pydub and Pyaudio](https://dev.to/mathewthe2/playing-mp3-files-in-python-with-pydub-and-pyaudio-579i)
* * [???](https://gist.github.com/kanhavishva/38416f4bdd1382ad15ccc40eb7a39429)