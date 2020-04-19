#!/home/ubuntu/Projects/info290t_venv/bin/python3

import pandas as pd
from mwviews.api import PageviewsClient
import datetime
import requests
import bs4 as bs
from sqlalchemy import create_engine
import pymysql


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


def yesterday():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_formatted = yesterday.strftime("%Y%m%d")
    return yesterday_formatted, yesterday


def wiki_webscrapping():
    # Wiki API
    p = PageviewsClient("mark-needham")
    cryptos = ["Ripple", "Bitcoin", "Ethereum", "Coinbase", "Binance", "Cryptocurrency"]
    views = p.article_views("en.wikipedia", cryptos, start=yesterday()[0], end=yesterday()[0])

    # Converting dictionary to DataFrame
    wiki = pd.DataFrame(views).T
    wiki.columns = ['Binance_wiki_views','Bitcoin_wiki_views','Coinbase_wiki_views','Crypto_wiki_views',
                    'Ethereum_wiki_views','XRP_wiki_views']

    # Return a DataFrame
    return wiki


def reddit_webscrapping():
    subreddits = ['Binance', 'Bitcoin', 'CoinBase', 'CryptoCurrency', 'Ethereum', 'Ripple', 'XRP']
    total_subscribers = []
    for subreddit in subreddits:
        url = "http://redditmetrics.com/r/" + str(subreddit)
        source = requests.get(url)
        soup = bs.BeautifulSoup(source.content, features='html.parser')
        total_subscribers.append(int(soup.find(class_='rank').text.replace(',','')))
    reddit = pd.DataFrame(data = total_subscribers, index = subreddits, columns = [str(yesterday()[1])]).T
    reddit.columns = ['Binance_reddit_subs','Bitcoin_reddit_subs','Coinbase_reddit_subs','Crypto_reddit_subs',
                    'Ethereum_reddit_subs', 'Ripple_reddit_subs', 'XRP_reddit_subs']
    return reddit


def merging_webscrapping():
    wiki = wiki_webscrapping()
    reddit = reddit_webscrapping()
    df = pd.merge(wiki, reddit, left_index=True, right_index=True)
    return df


def load_daily_data():
    df = merging_webscrapping()
    engine = create_engine('mysql+pymysql://admin:info290t@info290t-test.cebgvmmttwwo.us-east-2.rds.amazonaws.com:3306/info290t_test')
    df.to_sql('crypto_currency_daily', con = engine, schema = 'info290t_test', if_exists = 'append', index = True, index_label= 'date')


load_daily_data()

