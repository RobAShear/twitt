from twitterscraper import query_tweets
from datetime import datetime

today = datetime.now()
print(today)
if __name__ == "__main__":
    list_of_tweets = query_tweets('realDonaldTrump', limit=20)

    for tweet in query_tweets('realDonaldTrump', begindate=today, limit=20):
        print(tweet)


