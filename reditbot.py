import praw
import re
import time

reddit = praw.Reddit(client_id='3EVAn8emGngfAw',
            client_secret='psdsi-B6YxzBsKO6vXOEwPrQyeFFoA',
            user_agent='1', #Credits and these can be changed
            username='foofoostuttin',
            password='Akinlosotu9653')


subreddits = ['funny','PewdiepieSubmissions'] #Targeted Subreddit names you can set your own subreddits by adding the names as following.
pos=0
errors = 0

title = "Funny" #Your post title
url = "https://www.youtube.com/watch?v=gSmZoDmWOWw" #your url goes here

def post():
    global subreddits
    global pos
    global errors
    try:
        subreddit = reddit.subreddit(subreddits[pos])
        subreddit.submit(title,url=url)
        print("Posted to" + subreddits[pos])

        pos = pos+1

        if(pos <= len(subreddits) - 1):
            post()
        else:
            print("Done")
    except praw.exceptions.APIException as e:
        if(e.error_type == "RATELIMIT"):
            delay = re.search("minutes?", e.message)

            if delay:
                delay_seconds = float(int(delay.group(1))*60)
                time.sleep(delay_seconds)
                post()
            else:
                delay = re.search("seconds",e.message)
                delay_seconds = float(delay.group(1))
                time.sleep(delay_seconds)
                post()

    except:
        errors = errors + 1
        if(errors > 5):
            print("Crashed")
            exit(1)


post()
