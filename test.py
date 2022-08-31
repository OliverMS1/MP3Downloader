#https://pypi.org/project/pytube/
from pytube import YouTube
from flask import render_template
import os

def lookup(input):
    try:
        yt = YouTube(input)

    except:
        return render_template("index.html")

    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download(output_path=".")

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 