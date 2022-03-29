import numpy as np 
import pandas as pd 
import json

# df = pd.read_json('https://www.kaggle.com/datasets/prathamsharma123/farmers-protest-tweets-dataset-raw-json')
# df.info()
# with open('m.json', 'r') as handle:
#     json_data = [json.loads(line) for line in handle]
# df = pd.read_json(json_data)
# df.info()

# df = pd.DataFrame()
name_columns = ['url','date', "id", "user", "retweetCount",'lang','likeCount','media','mentionedUsers','outlinks','quoteCount','quotedTweet','renderedContent','replyCount','source','sourceLabel','sourceUrl','tcooutlinks']
df1 = pd.DataFrame(columns=name_columns)
with open('m.json', 'r') as handle:
    for line in handle:
        # print(json.loads(line))
        df1 = df1.append(json.loads(line), ignore_index=True)
df = df1[['date', "id", "user", "retweetCount"]].copy()


# Función 1, top 10 tweets con más retweets
def retweeted():
    return

print(df.tail)
df.info()
