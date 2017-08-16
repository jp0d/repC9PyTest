from twython import Twython # pip install twython
import time # standard lib

#Variables that contains the user credentials to access Twitter API 
access_key = "785026461010792449-eNMv45wVs34QqQXBXHCpnoXE7O7jc7N"
access_secret = "Iz2dEMgzQy60yLwSHknHAw8LOq2oF1BqaYxPbdxUYbdYr"
consumer_key = "tzfotElrfZpw2lK88jvyNaWcp"
consumer_secret = "KQEiEQJp1qRSk8lyT7uMvyOr9pq3NyDeXYoeUmc2pJ77Tl5LHI"


twitter = Twython(consumer_key,consumer_secret,access_key,access_secret)
lis = [536732886980767744] ## this is the latest starting tweet id
for i in range(0, 16): ## iterate through all tweets
## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name="ImLeslieChow",
    count=200, include_retweets=False, max_id=lis[-1])
    time.sleep(300) ## 5 minute rest between api calls

    for tweet in user_timeline:
        print(tweet['text']) ## print the tweet
        lis.append(tweet['id']) ## append tweet id's
