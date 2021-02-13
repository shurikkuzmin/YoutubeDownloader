# -*- coding: utf-8 -*-
"""
Created on 

"""

from __future__ import unicode_literals 
import youtube_dl
import os

options = {
    'format': 'bestaudio/best', # choice of quality
    'extractaudio' : True,      # only keep the audio
    'audioformat' : "mp3",      # convert to mp3 
    'outtmpl': '%(id)s',        # name the file the ID of the video
    'noplaylist' : True,}       # only download single song, not playlist

ydl = youtube_dl.YoutubeDL(options)

result = ydl.extract_info("https://www.youtube.com/watch?v=XXYlFuWEuKI", download=True)
os.rename(result['id'], result['id'] + ".mp3")

