from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data
music_data = {
    "playlists": [
        {"id": 1, "name": "Top Hits", "songs": [1, 2, 3]},
        {"id": 2, "name": "Chill Vibes", "songs": [4, 5, 6]},
    ],
    "songs": [
        {"id": 1, "title": "Song One", "artist": "Artist One", "album": "Album One", "genre": "Pop"},
        {"id": 2, "title": "Song Two", "artist": "Artist Two", "album": "Album Two", "genre": "Rock"},
        {"id": 3, "title": "Song Three", "artist": "Artist Three", "album": "Album Three", "genre": "Jazz"},
        {"id": 4, "title": "Song Four", "artist": "Artist Four", "album": "Album Four", "genre": "Pop"},
        {"id": 5, "title": "Song Five", "artist": "Artist Five", "album": "Album Five", "genre": "Classical"},
        {"id": 6, "title": "Song Six", "artist": "Artist Six", "album": "Album Six", "genre": "Rock"},
    ]
}

@app.route('/')
def index():
    return render_template('index.html', playlists=music_data['playlists'], songs=music_data['songs'])

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    results = [song for song in music_data['songs'] if query.lower() in song['title'].lower() or query.lower() in song['artist'].lower()]
    return jsonify(results)

@app.route('/playlist/<int:playlist_id>')
def get_playlist(playlist_id):
    playlist = next((pl for pl in music_data['playlists'] if pl['id'] == playlist_id), None)
    if not playlist:
        return jsonify({"error": "Playlist not found"}), 404
    songs = [song for song in music_data['songs'] if song['id'] in playlist['songs']]
    return jsonify({"playlist": playlist, "songs": songs})

@app.route('/genres')
def get_genres():
    genres = list(set(song['genre'] for song in music_data['songs']))
    return jsonify(genres)

if __name__ == '__main__':
    app.run(debug=True)
