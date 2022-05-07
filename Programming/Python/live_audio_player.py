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