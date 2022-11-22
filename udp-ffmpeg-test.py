import socket
import os
import subprocess
import platform
# import ffmpeg
#FPS: "-r 30"

OS = platform.system()

videodrivers = ""
audiodrivers = ""
ip = ""
if OS == "Linux":
    videodrivers = "v4l2"
    audiodrivers = "alsa"
    ip = "udp://162.250.138.11:9001"    
# subprocess.run(["arecord", "-l", "-D", "hw:1,0"])
#Linux

list_files = subprocess.run(["ffmpeg", "-f", videodrivers, "-i", "/dev/video0", "-f", audiodrivers, "-i", "hw:1", "-profile:v", "high", 
                            "-pix_fmt", "yuvj420p", "-level:v", "4.1", "-preset", "medium", "-tune", "zerolatency", "-vcodec", 
                            "libx264", "-r", "60", "-b:v", "8M", "-s", "1280x720", "-acodec", "aac", "-strict", "experimental", "-ac",
                            "2", "-ab", "64k", "-ar", "44100", "-f", "mpegts", "-flush_packets", "0", ip,
                            "-loglevel", "quiet"])
                            # stdout=subprocess.DEVNULL)

#"-loglevel error" is used to suppress debug logs (speed?)
#maybe increase buffer size                            "-fflags", "nobuffer"
 