from flask import Flask, render_template, request
import os
import time
import json

song = ""
endtime = time.time()

app = Flask(__name__)
@app.route('/')
def index():
    """Renders the welcome page."""
    return render_template('index.html')

@app.route('/choice')
def choicessss():
    return render_template("choice.html")

@app.route('/main', methods=['POST','GET'])
def wowthisdefinitionisimportant():
    print("flask is running")
    global starttime, endtime, lyrics, song
    try:
        song = request.form['song']
    except:
        song = request.args.get('song')
    # Just try it for both POST and GET because we change it so often
    print(song)
    print("crash 1")
    song = song.lower()
    print(song)
    lyrics = []
    song_file = f"songs/{song}/song.mp3"
    print("crash 2")
    #starttime = time.time()
    print("variables are deifined")
    try:
        with open(f"static/songs/{song}/lyrics.csv", "r") as file:
            for row in file:
                lyrics.append(row)
            print("".join(lyrics))
    except:
        return render_template('choice.html', ERROR="Invalid song please try again")
    print("made it to end")
    print(f"SONG: {song} TYPE: {type(song)}")
    return render_template('main.html', LYRICS = json.dumps(lyrics), AUDIO_AS_CHOSEN = song_file)

@app.route("/About")
def About():
    """Renders the main application page."""
    return render_template("About.html")

@app.route('/results', methods =['GET'])
def buring_an_orphanage():
    errors = request.args.get('var1')
    wpm = request.args.get('var2')
    return render_template('results.html', ERROR=errors, WPM=wpm, SONG=song)

if __name__ == '__main__':
    app.run()