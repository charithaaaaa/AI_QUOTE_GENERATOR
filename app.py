from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv
import os
app=Flask(__name__)
#Add gemini key
client = genai.Client(api_key=os.getenv("api"))
@app.route("/", methods=["GET", "POST"])
def index():
    quotes= []
    if request.method == "POST":
        topic = request.form["topic"]
        prompt = f"""Generate a motivational quotes about {topic}.
        each quote should be on a new line."""
        # Generate a response using Gemini
        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=prompt
        )
        quotes = response.text.strip().split("\n")
    return render_template("index.html", quotes=quotes)
if __name__ == "__main__":
    app.run(debug=True)