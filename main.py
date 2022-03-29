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
    df_retweeted = df.sort_values(by=['retweetCount'], ascending=False).head(n=10)[['id','retweetCount']].copy()
    return df_retweeted

# Función 2, personas con más tweets
def categorise(row): 
    return row['user']['username']
def famocillo():
    df["user_id"] = df.apply(lambda row: categorise(row), axis = 1)
    df1 = df[['user_id', 'user']].copy() 
    df1['counts'] = df1.groupby(['user_id'])['user'].transform('count')
    return df1.sort_values(by='counts',ascending=False).head(10)

# Función 3, días con más tweets
def days():
    return df.groupby(['date']).size()

print("DATAFRAME ORIGINAL:\n")
print(df.head(10))
print("\n")
# Función 1
print("DATAFRAME ORDENADO SEGÚN PRIMERA FUNCIÓN:\n")
print(retweeted())
print("\n")

# Función 2
print("DATAFRAME ORDENADO SEGÚN N° DE TWEETS DE USUARIOS:\n")
print(famocillo())
print("\n")


# Función 3
print("DATAFRAME ORDENADO SEGÚN TERCERA FUNCIÓN:\n")
print(days().head(n=10))
print("\n")
# df.info()
