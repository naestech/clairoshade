import tweepy

# replace these with your own bearer token
bearer_token = 'your_bearer_token'

# authenticate to twitter
client = tweepy.Client(bearer_token=bearer_token)

# search tweets containing the keywords "clairo shade"
search_query = 'clairo shade'
response = client.search_recent_tweets(query=search_query, max_results=100, tweet_fields=['public_metrics'])

# sort tweets by retweet count
tweets = response.data
if tweets:
    sorted_tweets = sorted(tweets, key=lambda tweet: tweet.public_metrics['retweet_count'], reverse=True)

    # get the 5 most popular tweets
    top_tweets = sorted_tweets[:5]

    # print the links to the top tweets
    for tweet in top_tweets:
        tweet_id = tweet.id
        tweet_url = f"https://twitter.com/twitter/status/{tweet_id}"
        print(tweet_url)
else:
    print("no tweets found.")
