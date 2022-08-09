# YouToU
  Read Me not Done
  
Installation
============
  To begin you will need to download FFMPEG and add it to your path. It can be download from their website [here](https://ffmpeg.org/download.html). To Ensure you've set everything up correctly watch [this](https://www.youtube.com/watch?v=IECI72XEox0) video on setting up FFMPEG for Windows.  
  Next download the latest release.  
  Once downloaded add the folder YouToU.exe is in to the system variables.
  
  If you wish to use the python script it is worth noting that pytube library will need to be installed. Run __`pip install pytube3`__ to install.
  
Usage
=====
Tell How to get to cmd properly  

 All commands entered are expected to entered in either of the two formats.  
 * __`[-link or -l] ['link'] [type flag]`__
 * __`[-file or -f] ['path']`__
  
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
__`["-o" or "-output"] [full path]__` Sets the output to the folder given as the path.  
__`["-o" or "-output"]__` Sets the output path to the current working directory (cwd) of the command prompt

Help
====

Type Flags
=====
 Type flags let the program know how you want your media to be downloaded. There are currently 3. Their names and usage are shown below.
 
 * __`-a`__ or __`-audio`__ -> Downloads only the audio of the video in mp3 format
 * __`-v`__ or __`-video`__ -> Downlaods the highest quality version of a video in in mp4 format
 * __`-b`__ or __`-both`__  -> Runs both the other two commands  
 The Audio flags requires FFMPEG to be installed and added to path to properly fix the audio. The audio will still be installed without FFMPEG, but some programs may not recognize it.
