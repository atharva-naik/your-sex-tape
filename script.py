#!/usr/bin/python
import os
import json
import praw
import time
import random
import logging
import colors
from colors import color
from dotenv import load_dotenv
# Enter your correct Reddit information into the variable below
load_dotenv()
userAgent = 'Title of your sex tapes'
ID = os.getenv('ID')
secret = os.getenv('SECRET')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
numFound = 0

reddit = praw.Reddit(user_agent=userAgent, client_id=ID,
                     client_secret=secret, username=username, password=password)
# phrase that the bot replies with
# makes a set of keywords to find in subreddits
logging.basicConfig(filename='app.log', filemode='w',
                    format='%(asctime)s: %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# subreddits = ['cursedcomments']  # subreddits to be monitored
# subs = []
# for sub in subreddits:
#     subs.append(reddit.subreddit(sub))
jokes = json.load(open('jokes.json', 'r'))
comment_ids = json.load(open('comments.json', 'r'))

while True:
    print(color("re running loop ...", fg='yellow', style='bold'))
    for comment in reddit.inbox.mentions():
        print(color(comment.author.name, fg='red', style='bold'))
        print(color(comment.subreddit, fg='green', style='bold'))
        bot_phrase = ""
        # print(comment.id)
        if 'u/your-sex-tape' in comment.body:
            if comment.id not in comment_ids:
                commentor = comment.author.name
                bot_phrase += f"{commentor} has summoned me, so here goes:\n\n"
                bot_phrase += jokes[random.randint(0, len(jokes)-1)]+'\n\n'
                bot_phrase += "github: http://github.com/atharva-naik/your-sex-tape\n"
                # logging
                try:
                    comment.reply(bot_phrase)
                    comment_ids[comment.id] = commentor
                    print(f"replying to {commentor}")
                except praw.exceptions.RedditAPIException:
                    print(color("I has low karma :(", fg='blue', style='italic'))
                    pass
            else:
                print(color("I has done my work :)",
                            fg='blue', style='italic'))

    json.dump(comment_ids, open('comments.json', 'w'))
    time.sleep(10)
    os.system("clear")
    # comment.reply(bot_phrase)
    # n_title = submission.title.lower() # makes the post title lowercase so we can compare our keywords with it.
    # for i in keywords: # goes through our keywords
    #     if i in n_title: # if one of our keywords matches a title in the top 10 of the subreddit
    #         numFound = numFound + 1

    #         print('Bot replying to: ') # replies and outputs to the command line
    #         print("Title: ", submission.title)
    #         print("Text: ", submission.selftext)
    #         print("Score: ", submission.score)
    #         print("---------------------------------")
    #         print('Bot saying: ', bot_phrase)
    #         print()
    #         submission.reply(bot_phrase)

    #     if numFound == 0:
    #         print()
    #         print("Sorry, didn't find any posts with those keywords, try again!")
