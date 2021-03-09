import json
import csv
import re
from os import listdir

fields = ['Jornal', 'Assunto', 'Data', 'Tweet_ID', 'Tweet']
filename = 'BrazilianTweetsDataset.csv'
mypath = "C:/Users/luisa/Desktop/LCA/MiniProject/data"  
files = listdir(mypath)

with open(filename, 'w',  newline='', encoding = 'utf8') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = '\t')
    csvwriter.writerow(fields)

    for f in files:
        directory = mypath + '/' + f
        with open(directory, encoding="utf8") as json_file:
            file = json.load(json_file)
            for i in file['meta']:
                newspaper = i['newspaper']
                topic = i['topic']
                date = i['date']
            for tweet in file['data']:
                tweet_id = tweet['id']
                tweet_text = tweet['text']
                #tweet_text = re.sub(r'(^|\s)\@(.+?)(\s|$)', r'\1', tweet['text'])

                row = [newspaper, topic, date, tweet_id, tweet_text]
                csvwriter.writerow(row)
                    
