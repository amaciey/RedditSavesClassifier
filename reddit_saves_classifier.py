import sys
import re
import os
import json
import time
import praw

reddit = praw.Reddit("bot1")

# Creates praw ListGenerator object containing post ids of all saved posts by the user
saved_posts = reddit.user.me().saved(limit=5)

# Iterates through saved posts, prints out the subreddit, and un-saves posts which have been deleted
for i in saved_posts:
    try:
        print(reddit.submission(id=str(i)).subreddit)

    except:
        print("That Post has been deleted")
        reddit.submission(id=str(i)).unsave()

