# YouToU
  project yada yada
  
Installation
============
  To begin you will need to download FFMPEG and add it to your path. It can be download from their website [here](https://ffmpeg.org/download.html). To Ensure you've set everything up correctly watch [this](https://www.youtube.com/watch?v=IECI72XEox0) video on setting up FFMPEG for Windows.  
  Next download the latest release.  
  Once downloaded add the folder YouToU.exe is in to the system variables.
  
  If you wish to use the python script it is worth noting that pytube library will need to be installed. Run __`pip install pytube3`__ to install.
  
Usage
=====
 All commands entered are expected to entered in either of the two formats.
 __`[-link or -l] ['link'] [type flag]`__
 __`[-file or -f] ['path']`__
  
Type Flags
=====
 Type flags let the program know how you want your media to be downloaded. There are currently 3. Their names and usage are shown below.
 
 * __`-a`__ or __`-audio`__ -> Downloads only the audio of the video in mp3 format
 * __`-v`__ or __`-video`__ -> Downlaods the highest quality version of a video in in mp4 format
 * __`-b`__ or __`-both`__  -> Runs both the other two commands
