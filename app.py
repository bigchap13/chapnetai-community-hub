from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/founder-story")
def founder_story():
    return render_template("founder_story.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/joshuas-journey")
def joshuas_journey():
    return render_template("joshuas_journey.html")

@app.route("/grant-finder")
def grant_finder():
    return render_template("grant_finder.html")

@app.route("/ecosystem-map")
def ecosystem_map():
    return render_template("ecosystem_map.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/health")
def health():
    return {
        "service": "ChapNetAI Community Hub",
        "status": "online",
        "visibility": "public"
    }

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5055, debug=True)
