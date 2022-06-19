import sys
import re
import os
import json
import time
import praw

reddit = praw.Reddit("bot1")

user_txt_file_path = '/Users/austinmaciey/Documents/'

if not os.path.exists(user_txt_file_path + 'Saved Reddit Posts'):
    os.mkdir(user_txt_file_path + 'Saved Reddit Posts')

# Creates praw ListGenerator object containing post ids of all saved posts by the user
saved_posts = reddit.user.me().saved(limit=1000)

# Iterates through saved posts, prints out the subreddit, and un-saves posts which have been deleted
for i in saved_posts:
    try:
        if not os.path.exists(
                user_txt_file_path + 'Saved Reddit Posts/' + str(reddit.submission(id=str(i)).subreddit) + ".html"):
            with open(
                    user_txt_file_path + 'Saved Reddit Posts/' + str(reddit.submission(id=str(i)).subreddit) + ".html",
                    'w') as f:
                f.writelines(
                    f'<a href="{reddit.submission(id=str(i)).shortlink}">{reddit.submission(id=str(i)).title}</a>')
                f.close()

        else:
            with open(
                    user_txt_file_path + 'Saved Reddit Posts/' + str(reddit.submission(id=str(i)).subreddit) + ".html",
                    'a') as f:
                # TODO: search for the link or title in the html and only add it if not already present
                f.writelines(
                    f'<br/> <a href="{reddit.submission(id=str(i)).shortlink}">{reddit.submission(id=str(i)).title}</a>')
                f.close()

    except:
        print("That Post has been deleted")
        #reddit.submission(id=str(i)).unsave()

# TODO: write a function to read .txt files and look for flags to unsave posts

