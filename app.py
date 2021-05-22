# -*- coding: utf-8 -*-
"""
Created on 

"""
from __future__ import unicode_literals 
import youtube_dl
import os
from flask import Flask
from flask import request,send_from_directory
import flask


def downloadMP3(youtubeLink):
    options = {
        'format': 'bestaudio/best', # choice of quality
        'extractaudio' : True,      # only keep the audio
        'audioformat' : "mp3",      # convert to mp3 
        'outtmpl': '%(id)s',        # name the file the ID of the video
        'noplaylist' : True,}       # only download single song, not playlist
    
    ydl = youtube_dl.YoutubeDL(options)
    
    result = ydl.extract_info(youtubeLink, download=True)
    
    if result == None:
        return ""
    newName = result["id"] + ".mp3"
    if "track" in result and "artist" in result:
        if result["artist"] != None and result["track"] != None:
            newName = result["artist"].replace(" ", "_") + "_" + result["track"].replace(" ", "_") + ".mp3"
    
    if not os.path.exists(newName):
        os.rename(result["id"], newName)
    
    return newName
    
   
def downloadMP4(youtubeLink):
    options = {
        'outtmpl': '%(id)s',        # name the file the ID of the video
        'noplaylist' : True
    }      
    
    ydl = youtube_dl.YoutubeDL(options)
    
    result = ydl.extract_info(youtubeLink, download=True)
    print(result)
    newName = result["id"] + ".mp4"
    if "track" in result and "artist" in result:
        newName = result["artist"].replace(" ", "_") + "_" + result["track"].replace(" ", "_") + ".mp4"
    
    if not os.path.exists(newName):
        os.rename(result["id"], newName)
    
    return newName
 
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        if request.form["YoutubeLink"] == "":
            return flask.render_template("example.html")
        if "MP3" in request.form:
            fileName = downloadMP3(request.form["YoutubeLink"])
        else:
            fileName = downloadMP4(request.form["YoutubeLink"])
        if fileName != "":  
            return flask.send_from_directory("", fileName, as_attachment=True)
    
    return flask.render_template("example.html")

if __name__ == '__main__':
    app.run(debug=True)