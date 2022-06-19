# Reddit Saves Classifier

## Overview
Reddit allows users to save posts for later use. However, finding those posts later on is cumbersome.
As someone who saves a lot of posts and doesn't always read  them in a timely manner, I would like to be able to catalog
and access older saved posts more easily.

This program will use the Reddit API to catalog all saved posts by subreddit, by month of the post, or by post type and
place the URLs into dedicated directories. The user can then choose to open any of the posts through their default browser.
This program will also allow users to mass un-save posts by adding them to a dedicated directory.

## Built With
[Reddit API](https://www.reddit.com/dev/api/#GET_user_{username}_saved)

[PRAW](https://praw.readthedocs.io/en/latest/index.html)

## Features

### Retrieve and Store Saved Posts
Using Reddit's API, pull all saved posts for a user and sort them according to user-defined criteria and find data associated
with each post such as parent link, flair, post type, etc. This data will then be used to create directories within a
user-defined master directory. For example, all saved posts can be split up into folders according to their subreddit.

### Open Posts and Parent Links with Default Browser
After sorting and classification, user will be able to open posts according to several user-input arguments. For example
a user could choose to open the parent link to view the original website post of an article, or open the reddit link to
read/post comments.

### Un-save Posts
Because the original intent of this project is to help users sort through and clear a backlog of saved posts, it would be
helpful to be able to mass un-save posts that one decides are no longer relevant or interesting. To that end, I propose an
"un-save directory" where users can move the posts they want to un-save from the original folders, and then run a function
to iterate through that directory and unsave all posts inside.

### GUI
To facilitate opening posts and moving them between directories, I think a simple GUI would be useful. 
