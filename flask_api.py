from threading import Thread
from flask import Flask, redirect, url_for, make_response
from scraper import key_word_meme
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

def fetch(query = None):
  if query == "#random":
      query = [""]
  else:
      query = query.split("+")
  print(query)
  try:
    data = key_word_meme(query)
    if (str(query).replace("['", "").replace("']", "") in data["title"].lower()) or (query == [""]):
      response = {"response":"Successfully fetched meme.", "meme":data}
    else:
      response = {"response":"Random meme sent as meme wasn't found with provided query.", "meme":data}
    
  except:
    response = {"response":"Error collecting the meme. It might be an error in your request or it might be an error on our side. If you believe it's an error on our side, please visit our documentation page."}

  return response

@cross_origin()
@app.route("/")
def home():
  response = fetch(query = "#random")
  return response

@cross_origin()
@app.route("/query=<query>/")
def search(query = None):
  return(fetch(query=query))

@cross_origin()
@app.route("/random/")
def random_meme():
  return(fetch(query = "#random"))

@cross_origin()
@app.route("/help/")
def help():
  return redirect("https://py-meme.github.io/docs/")

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=app.run(host='0.0.0.0',port=8080))
  t.start()
