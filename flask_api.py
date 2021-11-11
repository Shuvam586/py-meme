from flask import Flask, redirect, url_for
from scraper import key_word_meme

app = Flask(__name__)

def fetch(query = None):
    if query == "#random":
        query = [""]
    else:
        query = query.split("+")
    print(query)
    try:
        data = key_word_meme(query)
        response = {"response":"Successfully fetched meme.", "meme":data}
    
    except:
        response = {"response":"Error collecting the meme. It might be an error in your request or it might be an error on our side. If you believe it's an error on our side, please visit our documentation page."}

    return response

@app.route("/")
def home():
    return(fetch(query = "#random"))

@app.route("/query=<query>/")
def search(query = None):
    return(fetch(query=query))

@app.route("/help/")
def help():
    return redirect("https://www.youtube.com/")

if __name__ == "__main__":
    app.run()