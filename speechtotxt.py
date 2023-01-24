import speech_recognition as sr
from pydub import AudioSegment
import os
os.chdir(r'C:\Users\Abdulrahman\Desktop\app\python')
# files                                                                         
src = "hello.mp3"
dst = "hello.wav"
# convert mp3 file to wav  
src=("hello.mp3")
sound = AudioSegment.from_mp3(src)
sound.export("hello.wav", format="wav", parameters=["-ac","2","-ar","8000"])

file_audio = sr.AudioFile("hello.wav")
                                  
r = sr.Recognizer()
with file_audio as source:
   audio_text = r.record(source)

print(type(audio_text))
print(r.recognize_google(audio_text))