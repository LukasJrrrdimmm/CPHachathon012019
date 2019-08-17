import os
import shutil
from pydub import AudioSegment

def convertByFolder():
    pathFolder = "Audios/obrigacao/"
    files = []

    try:
        os.mkdir("{}dist".format(pathFolder))
    except:
        shutil.rmtree("{}dist".format(pathFolder))
        os.mkdir("{}dist".format(pathFolder))

    for r, d, f in os.walk(pathFolder):
        for mp3 in f:
            pathFile = "{}{}".format(pathFolder, mp3)
            print(pathFile)
            sound = AudioSegment.from_mp3(pathFile)
            sound.export("{}dist/{}.wav".format(pathFolder, mp3.strip(".mp3")), format="wav")

convertByFolder()