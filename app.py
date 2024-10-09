from flask import Flask, request, jsonify, render_template
from music_player import play_song, pause_song, stop_song, next_song, prev_song, recommend_song, load_songs

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to load songs
@app.route('/load_songs', methods=['POST'])
def load_songs_route():
    files = request.form.getlist('songs')  # Receive songs as list of file paths
    playlist = load_songs(files)
    return jsonify({"playlist": playlist})

# Route to play a song
@app.route('/play', methods=['GET'])
def play_route():
    song = play_song()
    return jsonify({"current_song": song})

# Route to pause a song
@app.route('/pause', methods=['GET'])
def pause_route():
    is_paused = pause_song()
    return jsonify({"paused": is_paused})

# Route to stop the song
@app.route('/stop', methods=['GET'])
def stop_route():
    stop_song()
    return jsonify({"message": "Stopped playing."})

# Route to go to the next song
@app.route('/next', methods=['GET'])
def next_route():
    song = next_song()
    return jsonify({"current_song": song})

# Route to go to the previous song
@app.route('/prev', methods=['GET'])
def prev_route():
    song = prev_song()
    return jsonify({"current_song": song})

# Route to get a recommendation
@app.route('/recommend', methods=['GET'])
def recommend_route():
    song = recommend_song()
    return jsonify({"recommended_song": song})

if __name__ == '__main__':
    app.run(debug=True)
