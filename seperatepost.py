import praw
import sys
import numpy as np
import spacy
import warnings
import os
from collections import Counter

nlp = spacy.load('en_core_web_sm')

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

reddit = praw.Reddit(client_id='TTgEI818GlCKFw',
                     client_secret='Y-MhscbZD6TpLOSADaUTtO6tP4s',
                     user_agent='trialapp/0.0 by sapienhwaker')
					
#print(reddit.read_only)  # Output: True

subreddit = reddit.subreddit('opiates')
hot_opiates = subreddit.hot()

total = []
commentscore = []
submissionscore = []
f = open('newfile.txt', 'a', encoding='utf-8')
i = 0
one = 0
tally = 0
doc = []
for submission in hot_opiates:
    if not submission.stickied:#and not submission.selftext == ''
        tally = tally + 1
        doc.append(submission.title+' '+submission.selftext)


independent = ['want','i','me','my','myself','feel','gone','legal','illegal','banned','ban','punish','punishment','fear','afraid','what','how','pain','shots','shot','inject','imagine','tablets','tablet','pill','pills','when','who','where','whose','whome','girl','boy','friend','no','die','dream','sleep','sound','slept','joy','addict','addicted','rehab','leave','left','rid','enough','plan','intend','love','life','job','career','hope','hopeless','disgust','struggle','sad','worry','antidepressant','think','feeling','bed','away','care']

for document in doc:
    #print(doc[0])
    document = " ".join(document.split())
    #print(doc[0])
    data = nlp(document)

    words = [token.lemma_ for token in data
         if not token.is_stop and not token.is_punct]
    onlywords = [token.lower() for token in words
         if not token.isnumeric()]

    f.write(str(onlywords))

    mylist = []
    matchList = []
    totalWordCount = 0
    totalMatchCount = 0

    for word in onlywords:
            for content in independent:
                if word == content:
                    totalWordCount = totalWordCount+1
                    totalMatchCount = totalMatchCount+1
                    mylist.append(word)

    counted = Counter(mylist)
    f.write(str(counted))
f.close()

print(tally)
#print(str(totalWordCount)+" is the total Word Count")
#print(matchList)

#print(len(submissionscore))

# Python code to demonstrate  
# addition of two list  
# naive method  
  
# printing original lists 
#print ("Original list 1 : " + str(total)) 
#print ("Original list 2 : " + str(submissionscore)) 
