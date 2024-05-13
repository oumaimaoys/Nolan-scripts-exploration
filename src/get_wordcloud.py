from wordcloud import WordCloud
import matplotlib.pyplot as plt



def getWordCloud(text_file_path, i = 0, stop_words = []):
    
    # get text from file
    text = open(text_file_path).read().lower()

    # generate word cloud
    wordcloud = WordCloud(random_state= 8,
                          normalize_plurals = False,
                          width=600,
                          height= 300,
                          max_words=300,
                          stopwords=stop_words).generate(text)
    
    # vizualize word cloud
    fig, ax = plt.subplots(1,1, figsize=(9,6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    i += 1
    plt.savefig('data/wordClouds/' + text_file_path[-4:] + str(i) + '.png')
    plt.show()

# common stop words
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']

# particular stop words for the script
words = ['CONT\'D', 'V.O', 'OWENS', 'int','sarah','CUTTER', 'ANGIER', 'OLIVIA','JULIA','BORDEN','FALLON','FISHER','ROOT','SAUL','MERRIT','JESS','MRS. BORDEN','MRS. ANGIER']

# get word cloud for the text file
getWordCloud('data\Scripts\\2006 The Prestige Scripts.txt', 0, stop_words + words)
