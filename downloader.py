# -*- coding: utf-8 -*-
"""
Created on 

"""
from __future__ import unicode_literals 
import youtube_dl
import os
from flask import Flask
import flask


def downloadMP3():
    options = {
        'format': 'bestaudio/best', # choice of quality
        'extractaudio' : True,      # only keep the audio
        'audioformat' : "mp3",      # convert to mp3 
        'outtmpl': '%(id)s',        # name the file the ID of the video
        'noplaylist' : True,}       # only download single song, not playlist
    
    ydl = youtube_dl.YoutubeDL(options)
    
    result = ydl.extract_info("https://www.youtube.com/watch?v=6A2mcpjq6F4&ab_channel=jouhari", download=True)
    
    newName = result["id"] + ".mp3"
    if "track" in result and "artist" in result:
        newName = result["artist"].replace(" ", "_") + "_" + result["track"].replace(" ", "_") + ".mp3"
        
    os.rename(result["id"], newName)
    
app = Flask(__name__)

@app.route("/")
def hello_world():
    return flask.render_template("example.html")

if __name__ == '__main__':
    app.run(debug=True)