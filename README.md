# YouToU
  YouToU is a command line based program that allows the user to download youtube videos one at a time or in bulk. The videos can also be downloaded with just their audio. YouToU relies on some of the pytube3 python library to work. 
  
Installation
============
To start you will need to downlaod the YouToU.exe from the latest release. From there place the exe wherever you wish to save it on your computer. Make sure to copy the path to the folder you placed the exe in as you will need to add it to your path. To add the folder to the path follow these steps.  

__`Open Control Panel`__ --> __`System and Security`__ --> __`System`__ --> __`Advanced System Settings`__ --> __`Environment Variables`__  

Here you will have the option to modify the users variables and the systems variables. I suggest doing the following steps with the user variables and if that does not work follow them again but modify the system variables.  

__`Click on Path`__ --> __`Edit`__ --> __`New`__ --> __`Paste in the path to the folder`__ --> __`Press ok on each of the menus that popped up previously`__  


When downloading just audio it might be downloaded in a weird format that other programs will not recognize. If you wish for the audio to be in the best possible quality it is suggested that you download FFMPEG. FFMPEG can be download from their website [here](https://ffmpeg.org/download.html) just be sure to add it to your path. If you dont know how to do that watch [this](https://www.youtube.com/watch?v=IECI72XEox0) video on setting up FFMPEG for Windows.  

Using with Python
================
  If you wish to use the python script it is worth noting that pytube library will need to be installed. Run __`pip install pytube3`__ to install.  
  The .spec file created by pyinstaller will be provided in the most recent release to allow for easily building an exe of YouToU.
  
Usage
=====
YouToU operates in the command line and has no GUI at all. To use YouToU open up the command promp by searching for it in the windows search bar. If everything was set up correctly you should be able to pull up the help menu by typeing in "YouToU" and pressing enter. If the help menu was not pulled up redo the installation, but make sure you add the folder to the system variable's path.  

All commands will begin with __`YouToU `__. Read the bellow sections to see valid inputs. An example input is listed below.  

__`YouToU -l https://www.youtube.com/watch?v=dQw4w9WgXcQ -v`__
  
Link
====

Links must be entered in either of the following ways
* __`["-l" or "link"] [link] [typeflag]`__
* __`["-l" or "link"] [link]`__  
The second option will use the -video typeflag without it needing to be specified

File
====

Files must be entered in this exact format  
__`["-f" or "file"] [path (including extension)]`__  
The file being read from should preferably be a text file. The file should be formated in the following way with no blank lines between links.  

__`[link] [typeflag]`__  

An example file can be seen below.
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ -a
https://www.youtube.com/watch?v=jNQXAC9IVRw -v
https://www.youtube.com/watch?v=owBhCgqGrS0 -b
```

Output
======

Output changes where your files will be saved to. There are two options for usage.  
__`["-o" or "-output"] [full path]`__ Sets the output to the folder given as the path.  
__`["-o" or "-output"]`__ Sets the output path to the current working directory (cwd) of the command prompt


Type Flags
=====
 Type flags let the program know how you want your media to be downloaded. There are currently 3. Their names and usage are shown below.
 
 * __`-a`__ or __`-audio`__ -> Downloads only the audio of the video in mp3 format
 * __`-v`__ or __`-video`__ -> Downlaods the highest quality version of a video in in mp4 format
 * __`-b`__ or __`-both`__  -> Runs both the other two commands  
 The Audio flags requires FFMPEG to be installed and added to path to properly fix the audio. The audio will still be installed without FFMPEG, but some programs may not recognize it.

Help
====
Commands that can be entered to get help.  
-h `link`   
-h `video`    
-h `output`  
-h `typeflag`    
-h  
