'''
# Basic plot
import numpy as np
import matplotlib.pyplot as plt
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))
plt.bar(y_pos, height, color=(0.2, 0.4, 0.6, 0.6))

# Custom Axis title
plt.xlabel('Types of Drugs', fontweight='bold', color = 'orange', fontsize='17', horizontalalignment='center')
plt.show()
'''
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

my_list = ['india','india','india','india','dds','saf','sadf','rewqw','sadf']
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
