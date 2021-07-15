import praw
import time
import pandas as pd
import logging
import threading
import matplotlib.pyplot as plt
import squarify
from sentiment_reddit_config import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.downloader.download('vader_lexicon')

'''*****************************************************************************
This program uses Vader SentimentIntensityAnalyzer to calculate a ticker/token compound value.
Limitations:
It depends mainly on the defined parameters for current implementation:
It completely ignores the heavily down voted comments, and there can be a time when
the most mentioned ticker is heavily down voted, but you can change that in upvotes variable.
****************************************************************************'''

start_time = time.time()
reddit = praw.Reddit(
    user_agent="Comment Extraction",

# replace with information from your Reddit account

    client_id="REDDIT_CLIENT_ID",
    client_secret="REDDIT_CLIENT_SECRET"
)
logging.info('logged into Reddit')
print('logged into Reddit')


def sentiment_reddit():
    threading.Timer(300, sentiment_reddit).start()

#    
#
# set the program parameters
#
#
    subs = ['CryptoCurrency', 'CryptoMarkets', 'EthTrader', 'Investing', 'Crypto_General', 'Bitcoin', 'CryptoCurrencyTrading', 'Coinbase', 'wallstreetbets']  # sub-reddit to search
    post_flairs = {'Daily Discussion', 'Weekend Discussion', 'Discussion'}  # posts flairs to search || None flair is automatically considered
    goodAuth = {'AutoModerator'}  # authors whom comments are allowed more than once
    uniqueCmt = True  # allow one comment per author per symbol
    ignoreAuthP = {'example'}  # authors to ignore for posts
    ignoreAuthC = {'example'}  # authors to ignore for comment
    upvoteRatio = 0.70  # upvote ratio for post to be considered, 0.70 = 70%
    ups = 20  # define # of up votes, post is considered if up votes exceed this #
    limit = 10  # define the limit, comments 'replace more' limit
    upvotes = 2  # define # of up votes, comment is considered if up votes exceed this #
    picks = 200  # define # of picks here, prints as "Top ## picks are:"
    picks_ayz = 200  # define # of picks for sentiment analysis

    posts, count, c_analyzed, tickers, titles, a_comments = 0, 0, 0, {}, [], {}
    cmt_auth = {}

    for sub in subs:
        subreddit = reddit.subreddit(sub)
        hot_python = subreddit.hot()  # sorting posts by hot
        # Extracting comments, symbols from subreddit
        for submission in hot_python:
            flair = submission.link_flair_text
            author = submission.author

            # checking: post up vote ratio # of up votes, post flair, and author
            if submission.upvote_ratio >= upvoteRatio and submission.ups > ups and (
                    flair in post_flairs or flair is None) and author not in ignoreAuthP:
                submission.comment_sort = 'new'
                comments = submission.comments
                titles.append(submission.title)
                posts += 1
                submission.comments.replace_more(limit=limit)
                for comment in comments:
                    # try except for deleted account?
                    try:
                        auth = comment.author.name
                    except:
                        pass
                    c_analyzed += 1

                    # checking: comment up votes and author
                    if comment.score > upvotes and auth not in ignoreAuthC:
                        split = comment.body.split(" ")
                        for word in split:
                            word = word.replace("$", "")
                            # upper = ticker, length of ticker <= 5, excluded words,
                            if word.isupper() and len(word) <= 5 and word not in blacklist and word in crypto:

                                # unique comments, try/except for key errors
                                if uniqueCmt and auth not in goodAuth:
                                    try:
                                        if auth in cmt_auth[word]: break
                                    except:
                                        pass

                                # counting tickers
                                if word in tickers:
                                    tickers[word] += 1
                                    a_comments[word].append(comment.body)
                                    cmt_auth[word].append(auth)
                                    count += 1
                                else:
                                    tickers[word] = 1
                                    cmt_auth[word] = [auth]
                                    a_comments[word] = [comment.body]
                                    count += 1

                                # sorts the dictionary
    symbols = dict(sorted(tickers.items(), key=lambda item: item[1], reverse=True))
    top_picks = list(symbols.keys())[0:picks]
    # time = (time.time() - start_time)

    # print top picks
    # print("It took {t:.2f} seconds to analyze {c} comments in {p} posts in {s} subreddits.\n".format(t=time, c=c_analyzed, p=posts, s=len(subs)))
    print("Posts analyzed saved in titles")
    # for i in titles: print(i)  # prints the title of the posts analyzed
    logging.info(top_picks)
    print(f"\n{picks} most mentioned picks: ")
    times = []
    top = []
    for i in top_picks:
        print(f"{i}: {symbols[i]}")
        times.append(symbols[i])
        top.append(f"{i}: {symbols[i]}")

    # Applying Sentiment Analysis
    scores, s = {}, {}

    vader = SentimentIntensityAnalyzer()
    # adding custom words from config
    vader.lexicon.update(new_words)

    picks_sentiment = list(symbols.keys())[0:picks_ayz]
    for symbol in picks_sentiment:
        stock_comments = a_comments[symbol]
        for cmnt in stock_comments:
            score = vader.polarity_scores(cmnt)
            if symbol in s:
                s[symbol][cmnt] = score
            else:
                s[symbol] = {cmnt: score}
            if symbol in scores:
                for key, _ in score.items():
                    scores[symbol][key] += score[key]
            else:
                scores[symbol] = score

        # calculating avg.
        for key in score:
            scores[symbol][key] = scores[symbol][key] / symbols[symbol]
            scores[symbol][key] = "{pol:.3f}".format(pol=scores[symbol][key])

    # printing sentiment analysis
    print(f"\nSentiment analysis of top {picks_ayz} picks:")
    df = pd.DataFrame(scores)
    df.index = ['Bearish', 'Neutral', 'Bullish', 'Total/Compound']
    df = df.T
    # log the dataframe
    logging.info('dataframe head - {}'.format(df.to_string()))
    print(df)