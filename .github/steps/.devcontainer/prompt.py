#Create an API endpoint that returns a JSON object with the following keys:
# "name", "age", "hobbies", "wakeup_time", "sleep_time", "favorite_food", "favorite_drink", 
#"favorite_operating_system", "favorite_computer_brand", "favorite_programming_language", "favorite_browser", 
#"favorite_video_game_console", "favorite_video_game", "favorite_board_game"

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')

def index():

    return jsonify({
        "name": "Aidan",
        "age": 18,
        "hobbies": ["video games", "programming", "reading", "listening to music", "watching movies"],
        "wakeup_time": "7:00 AM",
        "sleep_time": "11:00 PM",
        "favorite_food": "pizza",
        "favorite_drink": "water",
        "favorite_operating_system": "Windows 10",
        "favorite_computer_brand": "Dell",
        "favorite_programming_language": "Python",
        "favorite_browser": "Google Chrome",
        "favorite_video_game_console": "PlayStation 4",
        "favorite_video_game": "The Last of Us",
        "favorite_board_game": "Monopoly"
    })

if __name__ == '__main__': 
    app.run(debug=True)

# Path: .github/steps/.devcontainer/Dockerfile
