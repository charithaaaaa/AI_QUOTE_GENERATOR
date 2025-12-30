from flask import Flask, render_template, request
from google import genai
app=Flask(__name__)
#Add gemini key
client = genai.Client(api_key="AIzaSyCBejYFbe6YbrFwVvckTbRn1K2HODpapyU")
@app.route("/", methods=["GET", "POST"])
def index():
    quote= ""
    if request.method == "POST":
        topic = request.form["topic"]
        # Generate a response using Gemini
        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=f"Genertate a motivational quote about {topic}"
        )
        quote = response.text
    return render_template("index.html", quote=quote)
if __name__ == "__main__":
    app.run(debug=True)