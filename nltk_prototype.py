import nltk 
import random
import string
import warnings
import sklearn
warnings.filterwarnings('ignore')
#nltk.download('punkt')
#nltk.download('wordnet')
#nltk.download('omw-1.4')

f= open('text.text','r',errors='ignore')
raw = f.read()

tokens_sen = nltk.sent_tokenize(raw)
tokens_words = nltk.word_tokenize(raw)

greet_inp = ['hello','hi','hey','sup','whats up']
greet_out = ['hi','hi there','hello','yes sir']

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in greet_inp:
            return random.choice(greet_out)



#print(tokens_sen)
#print(tokens_words)

lemmer = nltk.stem.WordNetLemmatizer()

def lemToken(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct),None) for punct in string.punctuation)

def lemNormalize(text):
    return lemToken(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

def response(user_response):
    chatbot_response = ''
    tokens_sen.append(user_response)
    TfdifVec = TfidfVectorizer(tokenizer = lemNormalize, stop_words = "english")
    tfidf = TfdifVec.fit_transform(tokens_sen)
    vals = cosine_similarity(tfidf[-1],tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf ==0:
        chatbot_response = chatbot_response+ 'i am sorry i dont understand'
        return chatbot_response
    else:
        chatbot_response= chatbot_response + tokens_sen[idx]
        return chatbot_response

if __name__ == '__main__':
    flag = True
    print('yo, my name is senku. i love one piece, i can tell you about one piece')
    while flag==True:
        user_response = input()
        user_response = user_response.lower()
        if user_response != 'bye':
            if user_response == 'hello' or user_response == 'hi':
                flag = False 
                print(' heyyyy')
            else:
                if greeting(user_response)!= None:
                    print(greeting(user_response))
                else :
                    print(response(user_response))
                    tokens_sen.remove(user_response)
        else :
            flag=False
            print('bye')
        

