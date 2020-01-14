import spacy
nlp = spacy.load('en_core_web_sm')
nlp.Defaults.stop_words |={"�"}
from collections import Counter

# Linguistic Inquiry and Word Count
# Characterization of the Affective Norms for English Words by discrete emotional categories
Happiness=['abundance','acceptance','ace','achievement','admired','adorable','advantage','adventure','affection','agility','agreement','alive','ambition','angel','applause','aroused','athletics','autumn','awed','baby','bake','bar','bath','bhtub','beach','beautiful','beauty','bed','beverage','bird','birthday','bless','bliss','blond','blossom','body','bouquet','brave','breast','breeze','bride','bright','brother','bunny','butterfly','cake','candy','capable','car','carefree','caress''cash','casino','champ','champion','charm','cheer','child','chocolate','christmas','church','circus','clouds','coast','color','comedy','comfort','confident','cook','cottage','couple','cozy','crown','cuddle','cuisine','cute','dawn','daylight','dazzle','decorate','delight','desire','devoted','diamond','dignified','dinner','diploma','dog','dollar','dove','dream','earth','easy','easygoing','eat','ecstasy','education','elated','elegant','engaged','enjoyment','erotic','excellence','excitement','exercise','fame','family','famous','fantasy','fascinate','favor','festive','flirt','flower','food','fragrance','free','freedom','friend','friendly','fun','game','garter','gentle','gift','girl','glamour','glory','god','gold','golfer','good','graduate','grateful','green','greet','grin','hamburger','handsome','happy','heal','health','heart','heaven','holiday','home','honest','honey','honor','hope','hopeful','horse','hug','humane','humor','idea','imagine','impressed','improve','incentive','infant','innocent','inspire','inspired','intellect','intercourse','interest','intimate','jelly','jewel','joke','jolly','joy','joyful','justice','kids','kind','kindness','kitten','knowledge','lake','lamb','laughter','lavish','leader','learn','legend','leisurely','liberty','life','lively','lottery','love','loved','loyal','lucky','luscious','lust','luxury','magical','mail','masterful','melody','merry','mighty','millionaire','miracle','money','mother','movie','muffin','muscular','music','naked','natural','nature','nice','nourish','nursery','ocean','optimism','outdoors','outstanding','palace','pancakes','paradise','party','passion','pasta','peace','penthouse','perfection','perfume','pet','pie','pillow','pizza','pleasure','politeness','powerful','present','prestige','pretty','pride','profit','progress','promotion','protected','proud','puppy','quality','rabbit','radiant','radio','rainbow','refreshment','relaxed','rescue','respect','respectful','restaurant','reunion','reward','riches','rollercoaster','romantic','safe','sailboat','saint','salad','sapphire','satisfied','save','savior','scholar','secure','silk','silly','skijump','sky','sleep','smooth','snow','snuggle','social','soft','song','soothe','spirit','spouse','spring','star','strong','success','sugar','sun','sunlight','sunrise','sunset','sweetheart','talent','terrific','thankful','thoughtful','thrill','tidy','toy','travel','treasure','treat','triumph','triumphant','trophy','trust','truth','tune','untroubled','useful','vacation','valentine','victory','virtue','warmth','water','waterfall','wealthy','wedding','wife','win','wink','wise','wish','wit','woman','yacht','young','youth','zest']
angerList = ['activate', 'aggressive', 'annoy', 'answer', 'arrogant', 'astonished', 'basket', 'bastard', 'betray', 'bold', 'boxer', 'building', 'bullet', 'coarse', 'coin', 'cold', 'column', 'computer', 'concentrate', 'contempt', 'contents', 'cork', 'corridor', 'curious', 'detail', 'embattled', 'face', 'fight', 'finger', 'foul', 'fraud', 'frigid', 'gangrene', 'gender', 'hairpin', 'hammer', 'headlight', 'idiot', 'immature', 'impair', 'ink', 'insane', 'iron', 'item', 'journal', 'kerchief', 'kettle', 'knife', 'lawn', 'lump', 'man', 'masturbate', 'meek', 'mighty', 'moment', 'month', 'muddy', 'mutation', 'name', 'neurotic', 'nurse', 'obsession', 'opinion', 'owl', 'paint', 'paralysis', 'patient', 'pervert', 'pistol', 'plane', 'poster', 'powerful', 'priest', 'putrid', 'quick', 'razor', 'reserved', 'river', 'salute', 'scorching', 'scornful', 'seasick', 'selfish', 'ship', 'sinful', 'slow', 'slush', 'solemn', 'spray', 'startled', 'stool', 'stove', 'tamper', 'tease', 'thief', 'tomb', 'toxic', 'truck', 'unit', 'victim']
fear = ['addict', 'alert', 'alimony', 'allergy', 'alley', 'ankle', 'anxious', 'army', 'astronaut', 'avalanche', 'bathroom', 'bathtub', 'beast', 'bees', 'black', 'blackmail', 'burn', 'bus', 'busybody', 'cabinet', 'cane', 'cannon', 'cat', 'cell', 'cellar', 'chair', 'chance', 'circle', 'city', 'clock', 'coffin', 'confused', 'controlling', 'corpse', 'crash', 'crisis', 'crutch', 'curtains', 'custom', 'cut', 'cyclone', 'dagger', 'damage', 'dark', 'dead', 'demon', 'dentist', 'destroy', 'diver', 'door', 'dreadful', 'elevator', 'engine', 'ennui', 'event', 'fire', 'flood', 'foam', 'foot', 'fork', 'fur', 'germs', 'glacier', 'glass', 'gossip', 'guilty', 'gun', 'gymnast', 'habit', 'hand', 'haphazard', 'hard', 'hat', 'hawk', 'hell', 'highway', 'history', 'hostile', 'hotel', 'hungry', 'hurricane', 'hurt', 'icebox', 'identity', 'insolent', 'invest', 'kerosene', 'key', 'kick', 'king', 'legend', 'leprosy', 'lesbian', 'letter', 'lice', 'lighthouse', 'lightning', 'limber', 'lion', 'listless', 'loneliness', 'louse', 'machine', 'malice', 'mangle', 'mantel', 'market', 'medicine', 'memory', 'method', 'mildew', 'modest', 'moody', 'mosquito', 'muscular', 'naked', 'narcotic', 'news', 'nun', 'obesity', 'overwhelmed', 'pamphlet', 'passage', 'penis', 'person', 'pest', 'pinch', 'plain', 'poison', 'power', 'prick', 'punishment', 'quart', 'rage', 'rattle', 'reptile', 'revolver', 'rigid', 'rock', 'rude', 'scandal', 'scapegoat', 'scissors', 'scorn', 'scurvy', 'serious', 'sheltered', 'shotgun', 'sissy', 'skyscraper', 'snob', 'spanking', 'stomach', 'stupid', 'suicide', 'syphilis', 'table', 'taxi', 'tense', 'thermometer', 'thorn', 'tobacco', 'tool', 'tragedy', 'trumpet', 'twilight', 'umbrella', 'upset', 'utensil', 'venom', 'vigorous', 'volcano', 'wasp', 'watch', 'white']
disgust = ['abortion', 'absurd', 'adult', 'alien', 'aloof', 'anguished', 'bland', 'blase', 'blister', 'blond', 'blubber', 'board', 'body', 'bowl', 'boy', 'burdened', 'butter', 'carcass', 'clumsy', 'cockroach', 'context', 'coward', 'crude', 'dirty', 'egg', 'embarrassed', 'excuse', 'fabric', 'fish', 'flabby', 'frog', 'garment', 'greed', 'grenade', 'gripe', 'hairdryer', 'hay', 'horse', 'impotent', 'indifferent', 'industry', 'infatuation', 'inferior', 'inhabitant', 'insult', 'intruder', 'invader', 'jealousy', 'ketchup', 'knot', 'lie', 'locker', 'loser', 'madman', 'maniac', 'measles', 'messy', 'milk', 'mistake', 'morbid', 'museum', 'mushroom', 'nectar', 'nude', 'obey', 'obscene', 'odd', 'pain', 'paper', 'part', 'penalty', 'penthouse', 'pig', 'pity', 'poetry', 'poverty', 'pressure', 'pungent', 'quarrel', 'quiet', 'rat', 'red', 'repentant', 'resent', 'revolt', 'rifle', 'riot', 'roach', 'rough', 'runner', 'scalding', 'scared', 'scorpion', 'sentiment', 'severe', 'shriek', 'sick', 'skeptical', 'slap', 'slum', 'snake', 'sour', 'space', 'sphere', 'starving', 'statue', 'storm', 'street', 'subdued', 'suffocate', 'surgery', 'swamp', 'swift', 'tank', 'teacher', 'termite', 'theory', 'thought', 'time', 'toothache', 'tornado', 'trunk', 'ugly', 'urine', 'vagina', 'vandal', 'vanity', 'vehicle', 'vest', 'village', 'virgin', 'wagon', 'waste', 'weapon', 'whore', 'window', 'yellow']
sadness = ['accident', 'ache', 'agony', 'alcoholic', 'appliance', 'arm', 'avenue', 'bandage', 'bankrupt', 'banner', 'bar', 'barrel', 'bench', 'bereavement', 'blasphemy', 'blind', 'blue', 'book', 'bored', 'bottle', 'broken', 'cancer', 'chaos', 'chin', 'consoled', 'cord', 'corner', 'corrupt', 'cow', 'crushed', 'death', 'debt', 'decompose', 'defeated', 'defiant', 'deformed', 'delayed', 'derelict', 'deserter', 'despairing', 'destruction', 'detached', 'detest', 'dirt', 'disappoint', 'disaster', 'discomfort', 'discouraged', 'disdainful', 'displeased', 'distressed', 'divorce', 'doctor', 'drown', 'dummy', 'dump', 'dustpan', 'elbow', 'errand', 'failure', 'fall', 'false', 'farm', 'fat', 'fatigued', 'fault', 'feeble', 'fever', 'field', 'handicap', 'hardship', 'headache', 'helpless', 'heroin', 'hide', 'hinder', 'hit', 'hooker', 'hostage', 'hydrant', 'idol', 'ignorance', 'illness', 'immoral', 'infection', 'injury', 'insect', 'insecure', 'jelly', 'jug', 'lamp', 'lantern', 'lazy', 'lightbulb', 'lost', 'malaria', 'manner', 'material', 'menace', 'metal', 'mind', 'mischief', 'morgue', 'mountain', 'mystic', 'needle', 'nonchalant', 'nonsense', 'nuisance', 'obnoxious', 'offend', 'office', 'option', 'overcast', 'patent', 'pencil', 'people', 'phase', 'plant', 'prairie', 'python', 'radiator', 'rain', 'regretful', 'reverent', 'ridicule', 'rusty', 'scar', 'scream', 'seat', 'shadow', 'shy', 'skull', 'smallpox', 'spider', 'square', 'stagnant', 'stiff', 'stress', 'suspicious', 'taste', 'terrible', 'timid', 'tower', 'traitor', 'tree', 'trouble', 'troubled', 'tumor', 'ulcer', 'unhappy', 'useless', 'vampire', 'violin', 'voyage', 'weary', 'wicked', 'windmill', 'world', 'wounds', 'writer']

#reader = csv.reader(f)
#people = ['abduction', 'abortion', 'absurd', 'abundance', 'abuse', 'acceptance', 'accident', 'ace', 'ache', 'achievement', 'activate', 'addict', 'addicted', 'admired', 'adorable', 'adult', 'advantage', 'adventure', 'affection', 'afraid', 'aggressive', 'agility', 'agony', 'agreement', 'air', 'alcoholic', 'alert', 'alien', 'alimony', 'alive', 'allergy', 'alley', 'alone', 'aloof', 'ambition', 'ambulance', 'angel', 'anger', 'angry', 'anguished', 'ankle', 'annoy', 'answer', 'anxious', 'applause', 'appliance', 'arm', 'army', 'aroused', 'arrogant', 'art', 'assassin', 'assault', 'astonished', 'astronaut', 'athletics', 'autumn', 'avalanche', 'avenue', 'awed', 'baby', 'bake', 'bandage', 'bankrupt', 'banner', 'bar', 'barrel', 'basket', 'bastard', 'bath', 'bathroom', 'bathtub', 'beach', 'beast', 'beautiful', 'beauty', 'bed', 'bees', 'beggar', 'bench', 'bereavement', 'betray', 'beverage', 'bird', 'birthday', 'black', 'blackmail', 'bland', 'blase', 'blasphemy', 'bless', 'blind', 'bliss', 'blister', 'blond', 'bloody', 'blossom', 'blubber', 'blue', 'board', 'body', 'bold', 'bomb', 'book', 'bored', 'bottle', 'bouquet', 'bowl', 'boxer', 'boy', 'brave', 'breast', 'breeze', 'bride', 'bright', 'broken', 'brother', 'brutal', 'building', 'bullet', 'bunny', 'burdened', 'burial', 'burn', 'bus', 'busybody', 'butter', 'butterfly', 'cabinet', 'cake', 'cancer', 'candy', 'cane', 'cannon', 'capable', 'car', 'carcass', 'carefree', 'caress', 'cash', 'casino', 'cat', 'cell', 'cellar', 'cemetery', 'chair', 'champ', 'champion', 'chance', 'chaos', 'charm', 'cheer', 'child', 'chin', 'chocolate', 'christmas', 'church', 'circle', 'circus', 'city', 'cliff', 'clock', 'clothing', 'clouds', 'clumsy', 'coarse', 'coast', 'cockroach', 'coffin', 'coin', 'cold', 'color', 'column', 'comedy', 'comfort', 'computer', 'concentrate', 'confident', 'confused', 'consoled', 'contempt', 'contents', 'context', 'controlling', 'cook', 'cord', 'cork', 'corner', 'corpse', 'corridor', 'corrupt', 'cottage', 'couple', 'cow', 'coward', 'cozy', 'crash', 'crime', 'criminal', 'crisis', 'crown', 'crucify', 'crude', 'cruel', 'crushed', 'crutch', 'cuddle', 'cuisine', 'curious', 'curtains', 'custom', 'cut', 'cute', 'cyclone', 'dagger', 'damage', 'dancer', 'danger', 'dark', 'dawn', 'daylight', 'dazzle', 'dead', 'death', 'debt', 'deceit', 'decompose', 'decorate', 'defeated', 'defiant', 'deformed', 'delayed', 'delight', 'demon', 'dentist', 'depressed', 'depression', 'derelict', 'deserter', 'desire', 'despairing', 'despise', 'destroy', 'destruction', 'detached', 'detail', 'detest', 'devil', 'devoted', 'diamond', 'dignified', 'dinner', 'diploma', 'dirt', 'dirty', 'disappoint', 'disaster', 'discomfort']
#trial = ['i','we','you','relativ','focus','future','sexual','they','affect','work','time','achieve','negemo','anx','anger','religion','money','focuspast','social','family','friend','netspeak','swear','motion','male','cogproc','insight','score','filler','leisure','discrep','tentat','certain','focus','present','sad','death','percept','see','hear','space','female','assent','bio','body','health','home','cause','post','length','ingest','rives','affiliation','informal','differ','power','reward','risk','nonflu','feel']
print("Here we go...")
#angerList = ['anger','angry','despise','disturb','enraged','frustrated','irritate','mad','noisy','outrage','rejected']
categories = [Happiness, angerList, fear, disgust, sadness]
#print(people)
opioid = ["fentanyl","heroin","hydrocodone","hydromorphone","methadone","oxycodone","oxymorphone","tramadol"]

file_name = 'tops.txt'
introduction_file_text = open(file_name, 'r', encoding='utf-8').read()

#to remove white spaces present in the text file
intro = " ".join(introduction_file_text.split())

complete_doc = nlp(intro)
question = '�'
# complete_doc = nlp(complete_text)
# Remove stop words and punctuation symbols
words = [token.lemma_ for token in complete_doc
         if not token.is_stop and not token.is_punct]
onlywords = [token.lower() for token in words
         if not token.isnumeric()]

# List to get the total no. of words from discrete emotional categories
# List to get the total no. of words form each discrete emotional categories
mylist=[]
matchList=[]

# count variable to count no. of words
totalWordCount = 0
totalMatchCount = 0

#loop for calculating total no. of words for each categories and for all categories

for category in categories:
    for word in onlywords:
        for content in category:
            if word == content:
                totalWordCount = totalWordCount+1
                totalMatchCount = totalMatchCount+1
                mylist.append(word)
    matchList.append(totalMatchCount)
    totalMatchCount = 0

# Getting count of all words using Counter function of the Collection class                
counted = Counter(mylist)
print(counted)
print(str(totalWordCount)+" is the total Word Count")
print(matchList)

# definition of the percentage function
def percentage(part, whole):
  return 100 * float(part)/float(whole)

# printing the share of each discrete emotional category
for each in matchList:
    percent = percentage(each, totalWordCount)
    print(percent)
    
#percent = percentage(matchList[0], totalWordCount)
#print(str(percent)+"% of words are from the selected category")
word_freq = Counter(words)
# 20 commonly occurring words with their frequencies
common_words = word_freq.most_common(20)
print(common_words)

'''
import csv

with open('sentiment.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)

finalcount = Counter(your_list)
print(finalcount)

for x in common_words:
    if "like" in common_words:
        print(x)

#print (common_words)

#Unique words
#unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
#print ('\nUnique Words: ',unique_words)
'''
