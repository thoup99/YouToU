from pytube import YouTube
from moviepy.editor import *
import os
from sys import argv

class YouToU:
    dstA = "./output/audio/"
    dstV = "./output/video/"

    currentTitle = ""
    currentLink = ""

    def checkDirectories():
        if not os.path.exists("./output/"):
            os.mkdir("./output/")
            print("Creating Output Directory")

        if not os.path.exists(YouToU.dstA):
            os.mkdir(YouToU.dstA)
            print("Creating Audio Output Directory")

        if not os.path.exists(YouToU.dstV):
            os.mkdir(YouToU.dstV)
            print("Creating Video Output Directory")

    def downloadVideo(yt: YouTube):
        print("\tDownloading Video")

        try:
            video = yt.streams.get_highest_resolution()
            video.download(YouToU.dstV)

            print("\t\tSuccess!")

        except:
            print("\t\tError Downloading Video")
            return


    def downloadAudio(yt: YouTube):
        print("\tDownloading Audio")

        try:
            video = yt.streams.get_audio_only()
            video.download(YouToU.dstA)

            print("\t\tSuccess!")

        except:
            print("\t\tError Downloading Audio")
            return


        print("\tFixing File")

        try:
            with open("./output/audio/" + YouToU.currentTitle + ".mp3", "w"):
                pass

            mp4 = "./output/audio/" + YouToU.currentTitle + ".mp4"
            mp3 = "./output/audio/" + YouToU.currentTitle + ".mp3"

            os.remove(mp3)

            video = AudioFileClip(mp4)
            video.write_audiofile(mp3, verbose=False, logger= None)

            os.remove(mp4)

            print("\t\tFile Fixed")

        except:
            print("\t\tError Fixing File. Remnence of the Process may still be found in the output folder.")

    def downloadBoth(yt):
        YouToU.downloadVideo(yt)
        YouToU.downloadAudio(yt)


    def downloadFromFile(fileName):
        if not os.path.exists(fileName):
            print("Error: Files does not exist.")
            return

        with open(fileName, "r") as file:
            links = file.read().splitlines()
        
        for link in links:

            flag = link[-2:].lower()
            link = link[:-2]

            YouToU.downloadWithLink(link, flag)            

        print("Completed")

    def downloadWithLink(link, flag):
        yt = YouTube(link)
        title = yt.title

        YouToU.currentTitle = title
        YouToU.currentLink = link

        print(title)

        if (flag == "-a" or flag == "-audio"): ##Audio Only
            YouToU.downloadAudio(yt)

        elif (flag == "-v" or flag == "-video"): #Video and Audio one file
            YouToU.downloadVideo(yt)

        elif (flag == "-b" or flag == "-both"): ##Video and Audio Seperate
            YouToU.downloadBoth(yt)

        else:
            print("\tError unrecognized flag: " + flag)

def printArgumentError():
    print("Enter arguments in either format:\n\t[-link or -l] [link] [type flag]\n\t[-file or -f] [path]")

if __name__ == "__main__":
    args = argv[1:]
    #Format [-link or -l] [link] [type flag]
    #Format [-file or -f] [path]

    #Type Flags
        # -a or -audio -> Downloads only the audio of the video in mp4 format
        # -v or -video -> Downlaods the video in in mp4 format
        # -b or -both  -> Runs both the other two commands

    if len(args) <= 1:
        printArgumentError()

    else:
        flag1 = args[0].lower()

        if flag1 == '-l' or flag1 == '-link':
            if len(args) >= 3:
                YouToU.checkDirectories()
                YouToU.downloadWithLink(args[1], args[2].lower())

            else:
                printArgumentError()

        elif flag1 == '-f' or flag1 == '-file':
            if len(args) >= 2:
                YouToU.checkDirectories()
                YouToU.downloadFromFile(args[1])

            else:
                printArgumentError()

        else:
            print("Flag " + flag1 + " not recoognized.")