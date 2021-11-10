import praw 
import random

def meme_getter():
  clientid = "tkECW-CTMUvaa8vSkGdSbw"
  clientsecret = "rA1bjxaqNYR107eKFmEgKJDdXFC44g"
  useragent = "memeAPI"
  reddit = praw.Reddit(client_id=clientid, client_secret=clientsecret, user_agent=useragent)

  subreddit = reddit.subreddit("memes")
  top = subreddit.top(limit = 100)

  subs = []

  for submission in top:
      subs.append(submission)

  rand_sub = random.choice(subs)

  data = {
    'title': rand_sub.title,
    'post url': f"https://www.reddit.com/{rand_sub.id}",
    'image url': rand_sub.url
  }

  return data