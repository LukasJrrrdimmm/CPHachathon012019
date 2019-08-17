
import speech_recognition as sr
import os

rec = sr.Recognizer()

pathFolders = ["Audios/capex/dist/", "Audios/gog/dist/", "Audios/marcos_criticos/dist/", "Audios/obrigacao/dist/"]

for folder in pathFolders:
    transcript = open('{}transcript.txt'.format(folder), 'w')
    for r, d, f in os.walk(folder):
        idx = 0
        for file in f:
            
            try:
                with sr.AudioFile("{}{}".format(folder, file)) as source:
                    audio = rec.record(source)
            except:
                print("ERROR: {}".format(file))

            try:
                text = rec.recognize_google(audio, language="pt-BR")
                transcript.write('{}\n'.format(text))
                idx += 1
                print("{}/{}".format(idx, len(f)))
                
            except Exception as e:
                print(e)

    transcript.close()