from textblob import TextBlob
from nltk.corpus import stopwords
import nltk
import string
import spacy
import sys
from nltk import sent_tokenize, word_tokenize



STOPWORDS = set(stopwords.words('english'))
nlp = spacy.load("en") #loads spacy for english
punctionation = set(string.punctuation)
finalList = []

persons = []
places = []
organizations = []
worksOfArt = []



def main():
    if len(sys.argv) == 1:
        print("usage: {0} filename".format(sys.argv[0]))
        return 0
    elif len(sys.argv) > 2:
        print("usage: {0} 'textfile'".format(sys.argv[0]))
    try:
        FILE = open(sys.argv[1])
        rawText = FILE.read()
        words = word_tokenize(rawText)
        
    except IOError:
        print("File cant be opened")
        return 0
    print("file opened... basic analysis:")
    
    print(len(words))
    print("removing punctuation and stop words")
    
    #remover stopwords e pontuacao
    punctlist = []
    for w in words:
        if w not in punctionation :
            punctlist.append(w)
    stopedList = []
    for w in punctlist:
        if w not in STOPWORDS:
            stopedList.append(w)

    #nao sei se isto fica: Remover duplicadas
    for w in stopedList:
        if w not in finalList:
            finalList.append(w)
    
    #categories found:
    categories = []
    nlp_text = nlp(" ".join(finalList))

    for i in nlp_text.ents:
        if i.label_ not in categories:
            #make sure cateories dont repeat
            print(i.label_)
            categories.append(i.label_)

    #check if object belongs in category
    for c in categories:
        print("|----Category: "+str(c)+"----|")
        for i in nlp_text.ents:

            if i.label_ == c:
                if c == 'PERSON':
                    if str(i) not in persons:
                        persons.append(str(i))
                elif c == "GPE":
                    if str(i) not in places:
                        places.append(str(i))
                elif c == "WORK_OF_ART":
                    if str(i) not in worksOfArt:
                        worksOfArt.append(str(i))
                elif c == "ORG":
                    if str(i) not in organizations:
                        organizations.append(str(i))
                else:
                    pass
    print("--------------------------------------------")
    print("The text file "+FILENAME+" contains references for these people: ")
    print("--------------------------------------------")
    print("\n".join(persons))
    print("--------------------------------------------")
    print("These places are mentioned through the text: ")
    print("--------------------------------------------")
    print("\n".join(places))
    print("--------------------------------------------")
    print("--The text speaks of these organizations or projectspyth: --")
    print("--------------------------------------------")
    print("\n".join(organizations))
    print("--------------------------------------------")
    print("--These are works of art, or objects    : --")
    print("--------------------------------------------")
    print("\n".join(worksOfArt))
    

    



main()
