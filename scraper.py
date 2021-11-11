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
    'image url': rand_sub.url,
    'author': rand_sub.author.name,
    'upvotes': rand_sub.ups,
    'downvotes': rand_sub.downs
  }

  return data

def key_word_meme(keywords):
  clientid = "tkECW-CTMUvaa8vSkGdSbw"
  clientsecret = "rA1bjxaqNYR107eKFmEgKJDdXFC44g"
  useragent = "memeAPI"
  reddit = praw.Reddit(client_id=clientid, client_secret=clientsecret, user_agent=useragent)

  subreddit = reddit.subreddit("memes")
  top = subreddit.top(limit = 100)

  subs = []
  for submission in top:
    subs.append(submission)

  key_count = len(keywords)
  collection = {}

  i = 1
  while i <= key_count:
    collection[str(i)] = []
    i += 1

  j = key_count
  while j > 0:
    for sub in subs:
      a = 0
      for keys in keywords:
        if keys in sub.title.lower():
          a += 1
      if a == j:
        collection[str(j)].append(sub)
    j -= 1
  
  index = None
  k = key_count
  get = False
  while k > 0:
    if len(collection[str(k)]) != 0:
      get = True
      index = k 
    k -= 1
    if get == True:
      break
  
  if index==None:
    final_send_sub = random.choice(subs)
  else:
    final_send_sub = random.choice(collection[str(index)])

  data = {
    'title': final_send_sub.title,
    'post url': f"https://www.reddit.com/{final_send_sub.id}",
    'image url': final_send_sub.url,
    'author': final_send_sub.author.name,
    'upvotes': final_send_sub.ups,
    'downvotes': final_send_sub.downs
  }
  
  return data
