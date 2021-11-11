from flask import Flask

app = Flask(__name__)

def fetch(query = None, token = None):
    output = ""
    if token == None:
        output =  f"User searched with '{query}' and did not use a token."
    elif query == None:
        output = f"User used the token '{token}' but did not enter any search queries."
    else:
        output =  f"User searched with '{query}' and used token '{token}'"
    
    return {"response":output}

@app.route("/")
def home():
    return 'click <a href = "url">here</a> for documentation.'

@app.route("/query=<query>/")
def search(query = None):
    return(fetch(query=query))

@app.route("/<token>/query=<query>/")
def prem_search(token, query):
    return(fetch(query = query, token = token))

@app.route("/<token>/")
def prem_search_noquery(token):
    return(fetch(token = token))

@app.route("/<token>/<query>")
def prem_search_wrongquery(token, query):
    return {"response":f"User used token '{token}' but did not enter the search query properly."}

if __name__ == "__main__":
    app.run()