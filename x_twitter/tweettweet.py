import tweepy

auth = tweepy.OAuth1UserHandler(
    'woyuuDExrwV2lXMirBw9TFR5y', '4l12DlmxP909Ds6KZF2lzPWY1pSDQCZh22ShNw5DU1iIGCY1E7', '39403149-PWjdwa8yjb2Ji1PDlIgjuOVIOjw3nv2aHyH84W9hV', 'Y4l4vYzneuTJrEgAeaa0M29k4bVPtVFCzui48oaqIMFaD'
)

api = tweepy.API(auth)

print(api.get_list())
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)