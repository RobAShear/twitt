from twitter_scraper import get_tweets

for tweet in get_tweets('realDonaldTrump', pages=25):
    print(tweet['text'])

