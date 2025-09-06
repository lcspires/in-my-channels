from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# --- MOCK DATA ---
MOCK_SUBSCRIPTIONS = [
    {"id": "UC_x5XG1OV2P6uZZ5FSM9Ttw", "title": "Google Developers"},
    {"id": "UCVHFbqXqoYvEWM1Ddxl0QDg", "title": "Python"},
    {"id": "UC8butISFwT-Wl7EV0hUK0BQ", "title": "freeCodeCamp.org"}
]

MOCK_VIDEOS = [
    {
        "id": "vid001",
        "title": "Flask Tutorial for Beginners",
        "channel": "Python"
    },
    {
        "id": "vid002",
        "title": "Advanced Python Programming Tips",
        "channel": "Python"
    },
    {
        "id": "vid003",
        "title": "JavaScript Basics Crash Course",
        "channel": "freeCodeCamp.org"
    },
    {
        "id": "vid004",
        "title": "Intro to Google Cloud APIs",
        "channel": "Google Developers"
    }
]

# --- ROUTES ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/subscriptions")
def subscriptions():
    return jsonify({"subscriptions": MOCK_SUBSCRIPTIONS})

@app.route("/search")
def search():
    query = request.args.get("q", "").lower()
    if not query:
        return jsonify({"results": []})

    results = [
        video for video in MOCK_VIDEOS
        if query in video["title"].lower() or query in video["channel"].lower()
    ]
    return jsonify({"results": results})


if __name__ == "__main__":
    app.run(debug=True)
