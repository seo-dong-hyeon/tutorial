import GetOldTweets3 as got
from bs4 import BeautifulSoup
import datetime
import time
from random import uniform
from tqdm.notebook import tqdm
import pandas as pd
import matplotlib.pyplot as plt

class TwitterCrawler:
    def __init__(self):
        self.days_range = []
        start = datetime.datetime.strptime("2020-04-07", "%Y-%m-%d")
        end = datetime.datetime.strptime("2020-04-14", "%Y-%m-%d")
        self.date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

    def make_condition(self):
        for date in self.date_generated:
            self.days_range.append(date.strftime("%Y-%m-%d"))

        print("=== 설정된 트윗 수집 기간은 {} 에서 {} 까지 입니다 ===".format(self.days_range[0], self.days_range[-1]))
        print("=== 총 {}일 간의 데이터 수집 ===".format(len(self.days_range)))

        # 수집 기간 맞추기
        start_date = self.days_range[0]
        end_date = (datetime.datetime.strptime(self.days_range[-1], "%Y-%m-%d")
                    + datetime.timedelta(days=1)).strftime("%Y-%m-%d")  # setUntil이 끝을 포함하지 않으므로, day + 1

        # 트윗 수집 기준 정의
        self.tweetCriteria = got.manager.TweetCriteria().setQuerySearch('막말') \
            .setSince(start_date) \
            .setUntil(end_date) \
            .setMaxTweets(-1)

    def collect_data(self):
        # 수집 with GetOldTweet3
        print("Collecting data start.. from {} to {}".format(self.days_range[0], self.days_range[-1]))
        start_time = time.time()
        tweet = got.manager.TweetManager.getTweets(self.tweetCriteria)

        print("Collecting data end.. {0:0.2f} Minutes".format((time.time() - start_time) / 60))
        print("=== Total num of tweets is {} ===".format(len(tweet)))

        # initialize
        self.tweet_list = []

        for index in tqdm(tweet):
            # 메타데이터 목록
            username = index.username
            link = index.permalink
            content = index.text
            tweet_date = index.date.strftime("%Y-%m-%d")
            tweet_time = index.date.strftime("%H:%M:%S")
            retweets = index.retweets
            favorites = index.favorites

            # 결과 합치기
            info_list = [tweet_date, tweet_time, username, content, link, retweets, favorites]
            self.tweet_list.append(info_list)

            # 휴식
            time.sleep(uniform(1, 2))

            twitter_df = pd.DataFrame(self.tweet_list,
                                      columns=["date", "time", "user_name", "text", "link", "retweet_counts",
                                               "favorite_counts"])

            # csv 파일 만들기
            twitter_df.to_csv("sample_twitter_data_{}_to_{}.csv".format(self.days_range[0], self.days_range[-1]), index=False,
                              encoding='utf-8')
            print("=== {} tweets are successfully saved ===".format(len(self.tweet_list)))

            # 파일 확인하기
            df_tweet = pd.read_csv('sample_twitter_data_{}_to_{}.csv'.format(self.days_range[0], self.days_range[-1]))
            print(df_tweet['text'].head(20))







