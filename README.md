# autopost-rss-blogger


Here is an example of code using Python and the feedparser library to get the RSS feed from a website and post it to a Blogspot blog using the Blogger API, and then repeat the process every 30 minutes:

This script will connect to the RSS feed, gets the entries and post them to blogger. Then it will wait for 30 minutes and repeat the process.

It is important to mention that, it's always best to get permission from the website owner before scraping their content. Also, some websites may have a limit on the number of requests you can make to their RSS feed, so you should make sure to not exceed that limit to avoid getting blocked.

Also, this is just an example, you may want to make some changes based on your requirements, like checking the last time the script posted something and only post the new feed entries after that time.


Cirrus CI is a cloud-based continuous integration (CI) and continuous delivery (CD) platform that allows you to run tests and deploy your code automatically. To use the above code in Cirrus CI, you will need to create a configuration file called .cirrus.yml in the root of your repository. This file tells Cirrus CI what to do when a change is pushed to your repository.

Here's an example of how you can use the above code to automatically post new RSS feed entries to your Blogspot blog using Cirrus CI:


This configuration file tells Cirrus CI to run the post_rss_feed_to_blogger.py script as a task. The script is using two python packages, google-api-python-client and feedparser, so we need to install them before running the script.

You will also need to provide your credentials.json file in your repository, and make sure that you have Blogger API enabled.

You will also need to provide the blog_id in the script and make sure that the script has all the necessary information to run.

You also need to set up the trigger for the script to run, it can be a webhook, a schedule or a manual trigger.

With this setup, every time you push changes to your repository, Cirrus CI will automatically run the script and post new entries from the RSS feed to your Blogspot blog.

Note that, if you have a large number of feeds, and you are running the script frequently, you may want to limit the number of posts in each run.




