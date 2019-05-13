import codecs, json, os
from datetime import datetime
from datetime import timedelta
import pandas as pd
import sqlite3
# municiotion, cudlo , trump , sanders,

conn = sqlite3.connect('trumptweets.db')
c = conn.cursor()


today = datetime.now().strftime('%Y-%m-%d %I:%M %p')
os.system("twitterscraper realDonaldTrump -u -l 1000 -o '{0}'.json".format(today))

with codecs.open('{0}.json'.format(today), 'r', 'utf-8') as f:
    tweets = json.load(f, encoding='utf-8')

list_tweets = [list(elem.values()) for elem in tweets]
list_columns = list(tweets[0].keys())
df = pd.DataFrame(list_tweets, columns=list_columns)
df['timestamp'] = pd.to_datetime(df['timestamp']) - timedelta(hours=7)
print(df.columns)
df = df[['text', 'timestamp', 'url', 'user']]


# print(df['timestamp'] > '2019-05-10') and (df['timestamp'] < '2019-05-11'))
# print(df[(df['timestamp'] > '2019-05-10') & (df['timestamp'] < '2019-05-11')])
# df[(df['timestamp'] > '2019-05-10') & (df['timestamp'] < '2019-05-11') & (df['user'] == 'realDonaldTrump')].to_csv('tweets_now.csv')

# df.to_csv('{0}.csv'.format(today))
df.to_sql('tweets', conn)
c.execute("delete from tweets where user != 'realDonaldTrump'")

conn.commit()
conn.close()
#UPDATE tweets SET timestamp=DATETIME(timestamp, '-240 minutes')
#delete from tweets where user != 'realDonaldTrump'
