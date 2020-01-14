import gensim
import numpy as np
import spacy
from spacy import displacy
from gensim.corpora import Dictionary
from gensim.models import LdaModel
import matplotlib.pyplot as plt
#import sklearn
#import keras
import pprint
import pyLDAvis
import warnings
import os

#Wordcloud of Top N words in each topic
from matplotlib import pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import matplotlib.colors as mcolors
warnings.filterwarnings('ignore')
'%matplotlib inline'

file_name = 'real.txt'
introduction_file_text = open(file_name, 'r', encoding='utf-8').read()
text = " ".join(introduction_file_text.split())

print('LDA RESULTS:\n')
nlp = spacy.load("en_core_web_sm")
my_stop_words = [u'�','today','like','get','feel','day','time']
for stopword in my_stop_words:
    lexeme = nlp.vocab[stopword]
    lexeme.is_stop = True

doc = nlp(text.lower())
#print(doc)

# we add some words to the stop word list
texts, article = [], []
for w in doc:
    # if it's not a stop word or punctuation mark, add it to our article!
    if w.text != '\n' and not w.is_stop and not w.is_punct and not w.like_num and w.text != 'I':
        # we add the lematized version of the word
        article.append(w.lemma_)
    # if it's a new line, it means we're onto our next document
    if w.text == '@@@@@@@@@@':
        texts.append(article)
        article = []
bigram = gensim.models.Phrases(texts)
#print(texts[1])

dictionary = Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
#print(corpus[100])

ldamodel = LdaModel(corpus=corpus, num_topics=10, id2word=dictionary)

'''
for i in range(0, ldamodel.num_topics-1):
    print (ldamodel.print_topic(i))
'''

ldamodel.save('model10.gensim')
topics = ldamodel.print_topics(num_words=10)
for topic in topics:
    print(topic)

'%matplotlib inline'
import matplotlib.pyplot as plt

exp_vals = [83,72,35,24,23,15,6,4]
exp_labels = ['heroin' , 'methadone', 'fentanyl', 'tramadol', 'oxycodone', 'hydrocodone', 'oxymorphone', 'hydromorphone']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0.1, 0, 0,0,0,0,0)  # explode 1st slice

# Plot
plt.pie(exp_vals, explode=explode, labels=exp_labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
#plt.pie(exp_vals,labels=exp_labels)
plt.title("Commonly discussed Drugs")
plt.show()

'''
# Libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image   # to import the image

my_list = ['heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'heroin', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'methadone', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'fentanyl', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'tramadol', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'oxycodone', 'hydrocodone', 'hydrocodone', 'hydrocodone', 'hydrocodone', 'hydrocodone', 'hydrocodone', 'hydrocodone', 'hydrocodone', 'hydrocodone', 'hydrocodone', 'hydrocodone', 'hydrocodone', 'hydrocodone', 'hydrocodone', 'hydrocodone', 'oxymorphone', 'oxymorphone', 'oxymorphone', 'oxymorphone', 'oxymorphone', 'oxymorphone', 'hydromorphone', 'hydromorphone', 'hydromorphone', 'hydromorphone']
unique_string=(" ").join(my_list)
#selecting image for the data
wave_mask = np.array(Image.open( "images.jpg"))
 
# Make the figure
wordcloud = WordCloud(mask=wave_mask, width=480, height=480, background_color="white").generate(unique_string)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
'''
