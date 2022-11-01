import socket
import os
import subprocess
import ffmpeg

#FPS: "-r 30"

list_files = subprocess.run(["ffmpeg", "-f", "v4l2", "-i", "/dev/video0", "-f", "alsa", "-i", "hw:1", "-profile:v", "high", 
                            "-pix_fmt", "yuvj420p", "-level:v", "4.1", "-preset", "ultrafast", "-tune", "zerolatency", "-vcodec", 
                            "libx264", "-r", "30", "-b:v", "512k", "-s", "1920x1080", "-acodec", "aac", "-strict", "-2", "-ac",
                            "2", "-ab", "32k", "-ar", "44100", "-f", "mpegts", "-flush_packets", "0", "udp://162.250.138.11:9001"], 
                            stdout=subprocess.DEVNULL)


