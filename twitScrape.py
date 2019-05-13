import codecs, json, os
from datetime import datetime
import pandas as pd

# municiotion, cudlo , trump , sanders, 

today = datetime.now().strftime('%Y-%m-%d %H.%M')
os.system("twitterscraper realDonaldTrump -u -l 20 -o {0}.json".format(today))

with codecs.open('{0}.json'.format(today), 'r', 'utf-8') as f:
    tweets = json.load(f, encoding='utf-8')

list_tweets = [list(elem.values()) for elem in tweets]
list_columns = list(tweets[0].keys())
df = pd.DataFrame(list_tweets, columns=list_columns)

print(df.columns)

# print(df['timestamp'] > '2019-05-10') and (df['timestamp'] < '2019-05-11'))
# print(df[(df['timestamp'] > '2019-05-10') & (df['timestamp'] < '2019-05-11')])
# df[(df['timestamp'] > '2019-05-10') & (df['timestamp'] < '2019-05-11') & (df['user'] == 'realDonaldTrump')].to_csv('tweets_now.csv')

df.to_csv('{0}.csv'.format(today))
