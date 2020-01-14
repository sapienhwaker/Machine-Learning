import praw
import sys
import gensim
import numpy as np
import spacy
import sklearn
import keras
import pprint
import pyLDAvis
import warnings
import os

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

reddit = praw.Reddit(client_id='TTgEI818GlCKFw',
                     client_secret='Y-MhscbZD6TpLOSADaUTtO6tP4s',
                     user_agent='trialapp/0.0 by sapienhwaker')
					
#print(reddit.read_only)  # Output: True

subreddit = reddit.subreddit('opiates')
hot_opiates = subreddit.top()

total = []
commentscore = []
submissionscore = []
f = open('tops.txt', 'a', encoding='utf-8')
i = 0
one = 0
counted = 0
for submission in hot_opiates:
    if not submission.stickied and one is 0:
        #one = 1
        f.write('Title: {}, Content: {}, ups: {}, downs: {}'.format(submission.title,submission.selftext,submission.ups,submission.downs))
        submissionscore.append(submission.ups)
        submission.comments.replace_more(limit=0)
        comments = submission.comments.list()
        for comment in comments:
            #f.write(20*'--')
            counted = counted + 1
            f.write(comment.body.translate(non_bmp_map))
        f.write(' @@@@@@@@@@ ')
        total.append(counted)
        i=i+1
        counted = 0
f.close()

print(len(total))
print(len(submissionscore))
  
# addition of two list  
  
# printing original lists 
print ("Total Upvotes : " + str(total)) 
print ("Total Comments and Replies : " + str(submissionscore)) 
  
# using naive method to  
# add two list  
res_list = [] 
for i in range(0, len(total)): 
    res_list.append(total[i] + submissionscore[i]) 
  
# printing resultant list  
print ("Resultant list is : " + str(res_list))
'''
filereader=open("data.txt", "r")
text = filereader.read()

print('got the text')
nlp = spacy.load("en_core_web_sm")
my_stop_words = [u'say', u'\'s', u'mr', u'be', u'said', u'says', u'saying', 'today']
for stopword in my_stop_words:
    lexeme = nlp.vocab[stopword]
    lexeme.is_stop = True

doc = nlp(text.lower())


# we add some words to the stop word list
texts, article = [], []
for w in doc:
    # if it's not a stop word or punctuation mark, add it to our article!
    if w.text != '\n' and not w.is_stop and not w.is_punct and not w.like_num and w.text != 'I':
        # we add the lematized version of the word
        article.append(w.lemma_)
    # if it's a new line, it means we're onto our next document
    if w.text == '\n':
        texts.append(article)
        article = []
bigram = gensim.models.Phrases(texts)
print(texts[1])
texts = [bigram[line]] for line in texts]
for line in texts:
    texts = bigram[line]
print(texts)
dictionary = Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
print(corpus[100])

ldamodel = LdaModel(corpus=corpus, num_topics=10, id2word=dictionary)

for i in range(0, ldamodel.num_topics-1):
    print (ldamodel.print_topic(i))

ldamodel.save('model10.gensim')
topics = ldamodel.print_topics(num_words=4)
for topic in topics:
    print(topic)

cols = [color for name, color in mcolors.TABLEAU_COLORS.items()]  # more colors: 'mcolors.XKCD_COLORS'

cloud = WordCloud(stopwords=my_stop_words,
                  background_color='white',
                  width=2500,
                  height=1800,
                  max_words=10,
                  colormap='tab10',
                  color_func=lambda *args, **kwargs: cols[i],
                  prefer_horizontal=1.0)

topics = ldamodel.show_topics(formatted=False)

fig, axes = plt.subplots(2, 2, figsize=(10,10), sharex=True, sharey=True)

for i, ax in enumerate(axes.flatten()):
    fig.add_subplot(ax)
    topic_words = dict(dictionary[i][1])
    cloud.generate_from_frequencies(topic_words, max_font_size=300)
    plt.gca().imshow(cloud)
    plt.gca().set_title('Topic ' + str(i), fontdict=dict(size=16))
    plt.gca().axis('off')
    
plt.subplots_adjust(wspace=0, hspace=0)
plt.axis('off')
plt.margins(x=0, y=0)
plt.tight_layout()
plt.show()
'''
