import feedparser
import google.auth
from googleapiclient.discovery import build
import time

# Set up the Blogger API client
credentials = google.auth.credentials.Credentials.from_service_account_file('path/to/credentials.json')
blogger = build('blogger', 'v3', credentials=credentials)

# The ID of your blog can be found in the URL of your blog's homepage (e.g. https://YOUR_BLOG_ID.blogspot.com/)
blog_id = '5996827985750087258'

while True:
    # Get the RSS feed from the website
    feed_url = 'https://www.abplive.com/home/feed'
    feed = feedparser.parse(feed_url)

    # Iterate through the items in the RSS feed
    for item in feed.entries:
        # Check if the post already exists in the blog
        existing_posts = blogger.posts().list(blogId=blog_id, q=f'title:{item.title}').execute()
        if existing_posts['items']:
            # If the post already exists, skip it
            continue
        # Create a new post on your blog
        post = {
            'title': item.title,
            'content': item.content[0].value
        }
        new_post = blogger.posts().insert(blogId=blog_id, body=post).execute()
        print(f'Post "{item.title}" created with ID: {new_post["id"]}')
    # Wait for 30 minutes before getting the RSS feed again
    time.sleep(1800)
