from pytube import YouTube
import subprocess
from sys import argv
import json
import os

class YouToU:
    savePath = os.getenv("APPDATA") + "\\YouToU"

    dstO = ""
    dstA = ""
    dstV = ""

    currentTitle = ""

    def init():
        try:
            configPath = YouToU.savePath + "\\config.json"

            with open(configPath) as save:
                data = json.load(save)
            savedPath = data["output"]

        except:
            print("Error occured when loading output path. Saving to current working directory.\nYou can fix you output location by using the -o flag followed by the path to the folder you want to use. Most likely C:Users\\'profile'\\")
            savedPath = ".\\"

        YouToU.dstO = savedPath + "\\output\\"
        YouToU.dstA = savedPath + "\\output\\audio\\"
        YouToU.dstV = savedPath + "\\output\\video\\"


    def createConfig(outputVal = ".\\"):
        if not os.path.exists(YouToU.savePath):
            os.mkdir(YouToU.savePath)

        outputVal = outputVal.replace('\\\\', '\\').replace('\\', '\\\\').replace('/', '\\\\')

        if outputVal[-2:] == '\\\\':
            outputVal = outputVal[-2:]

        with open(YouToU.savePath + "\\config.json", "w") as config: #Needs to open in the path the program is running from
            config.write('{"output": "'+ outputVal +'"} ')

        print("Updated Output Directory")


    def checkDirectories():
        if not os.path.exists(YouToU.dstO):
            os.mkdir(YouToU.dstO)
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


    def downloadAudio(yt: YouTube):
        print("\tDownloading Audio")

        try:
            video = yt.streams.get_audio_only()
            video.download(YouToU.dstA, YouToU.currentTitle + ".mp4")

            print("\t\tSuccess!")

        except:
            print("\t\tError Downloading Audio")
            return


        print("\tFixing Audio") #Issue fixing audio with a - or / in its name

        try:
            with open(YouToU.dstA + YouToU.currentTitle + ".mp3", "w"):
                pass

            mp4 = YouToU.dstA + YouToU.currentTitle + ".mp4"
            mp3 = YouToU.dstA + YouToU.currentTitle + ".mp3"

            os.remove(mp3)

            subprocess.call([
                'ffmpeg',
                '-i',
                mp4,
                '-c:v',
                'copy',
                '-c:a',
                'libmp3lame',
                '-q:a',
                '4', 
                mp3,
                '-loglevel', 'quiet'
            ])

            os.remove(mp4)

            print("\t\tAudio Fixed!")

        except Exception as e:
            print(e)
            print("\t\tError Fixing Audio")

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

        print(title)

        YouToU.currentTitle = title.replace('/', ' ')


        if (flag == "-a" or flag == "-audio"): ##Audio Only
            YouToU.downloadAudio(yt)

        elif (flag == "-v" or flag == "-video"): #Video and Audio one file
            YouToU.downloadVideo(yt)

        elif (flag == "-b" or flag == "-both"): ##Video and Audio Seperate
            YouToU.downloadBoth(yt)

        else:
            print("\tError unrecognized flag: " + flag)


def printHelpOption(helpType):

    if helpType == 'link':
        print(
            'Links must be entered in either of the following ways\n'
            + '\t["-l" or "link"] [link] [typeflag]\n'
            + '\t["-l" or "link"] [link]\n'
            + '\tThe second option will use the -video typeflag without it needing to be specified'
        )

    if helpType == 'file':
        print(
            'Files must be entered in this exact format\n'
            + '\t["-f" or "file"] [path (including extension)]\n'
            + '\tThe file being read from should preferably be a txt. The file should be formated in the following way.\n'
            + '\t[link] [typeflag]\n'
            + '\tThere should also be no blank lines.'
        )

    if helpType == 'output':
        print(
            'Output changes where your files will be outputed to. There are two options for usage.\n'
            + '\t["-o" or "-output"] [full path] \n'
            + '\t["-o" or "-output"] Sets the current working directory (cwd) of the command prompt to the output path'
        )

    if helpType == 'typeflag':
        print(
            'Type Flags are used to tell YouToU how you want your video to be downloaded. There are currently three options.\n'
            + '\t"-a" or "-audio" -> Downloads only the audio of the video in mp4 format.\n'
            + '\t"-v" or "-video" -> Downlaods the video in in mp4 format\n'
            + '\t"-b" or "-both"  -> Runs both the other two commands\n'
            + '\nThe Audio flags requires FFMPEG to be installed and added to path to properly fix the audio.'
        )

    if helpType == 'help':
        print(
            'Help\n'
            + '-h link     \n'
            + '-h video    \n'
            + '-h output   \n'
            + '-h typeflag \n'
            + '-h          \n'
        )

    if helpType == 'misc':
        print(
            'The entered command could not be properly identified. Try using the help flag (-h) by itself for help.\n'
            + '\tYouToU -h\n'
            + '\tYouToU.exe -h\n'
            + '\tpython YouToU.py -h\n'
            + 'The command entered will depend on how you installed and set up YouToU'
        )


if __name__ == "__main__":
    args = argv[1:]
    YouToU.init()

    argsLength = len(args)

    if argsLength == 0:
        printHelpOption('help')

    else:

        flag1 = args[0].lower()

        if flag1 == '-l' or flag1 == '-link':
            if argsLength == 3:
                YouToU.checkDirectories()
                YouToU.downloadWithLink(args[1], args[2].lower())
                print("Completed")

            elif argsLength == 2:
                YouToU.checkDirectories()
                YouToU.downloadWithLink(args[1], '-v')
                print("Completed")

            else:
                printHelpOption('link')


        elif flag1 == '-f' or flag1 == '-file':
            if argsLength >= 2:
                YouToU.checkDirectories()
                YouToU.downloadFromFile(args[1])

            else:
                printHelpOption('file')


        elif flag1 == '-o' or flag1 == '-output':
            if argsLength == 2:
                YouToU.createConfig(args[1])

            elif argsLength == 1:
                YouToU.createConfig(os.getcwd())

            else:
                printHelpOption('output')


        elif flag1 == '-h' or flag1 == '-help': #Can take second argument that will be used to find its help option
            if argsLength == 1:
                printHelpOption('help')

            elif argsLength == 2:
                arg = args[1].lower()              

                if arg == 'l' or arg == 'link':
                    printHelpOption('link')

                elif arg == 'f' or arg == 'file':
                    printHelpOption('file')

                elif arg == 'o' or arg == 'output':
                    printHelpOption('output')

                elif arg == 't' or arg == 'typeflag':
                    printHelpOption('typeflag')

                else:
                    printHelpOption('misc')

            else:
                printHelpOption('misc')

        else:
            printHelpOption('misc')