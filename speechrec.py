import speech_recognition as sr

r = sr.Recognizer()
'''
with sr.Microphone() as source:

    print('Speak Anything: ' )

    audio = r.listen(source)


    try:

        text = r.recognize_google(audio)
        print('You just said',text)

    except:

        print("I didint get you sorry")
'''

song = sr.AudioFile('/home/ram/right_now1.wav')
with song as source:

    print('Trying ... ' )
    audio = r.record(source)

    try:

        text = r.recognize_google(audio)
        print('Lyrics',text)

    except:

        print("I didint get you sorry")
