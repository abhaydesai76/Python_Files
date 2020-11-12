import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

f = open("C:\\ChatBot\\chatbot.txt", "r", errors="ignore")

raw = f.read()

raw = raw.lower()
# print(raw)

# nltk.download()
nltk.download('punkt')
nltk.download('wordnet')

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

# print(sent_tokens[:])
# print(word_tokens[:])

lemmer = nltk.stem.WordNetLemmatizer()


def lemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def lemNormalize(text):
    return lemTokens((nltk.word_tokenize(text.lower().translate(remove_punct_dict))))


GREETING_INPUTS = ["hello", "hi", "greetings", "hey", "what's up"]
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me", "What do you want to know?"]


def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


def response(user_response):
    robo_response = ""
    sent_tokens.append(user_response)

    TfidVec = TfidfVectorizer(tokenizer = lemNormalize, stop_words = "english")

    tfidf = TfidVec.fit_transform(sent_tokens)

    vals = cosine_similarity(tfidf[-1], tfidf)

    idx = vals.argsort()[0][-2]

    flat = vals.flatten()
    flat.sort()

    req_tfidf = flat[-2]

    if (req_tfidf == 0):
        robo_response = robo_response + "I am sorry! I don't understand you."

        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]

        return robo_response


flag = True
print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")

while(flag == True):
    user_response = input()
    user_response = user_response.lower()

    if (user_response != "Bye!"):
        if (user_response == "Thanks" or user_response == "Thank You"):
            flag = False
            print("ROBO: You are Welcome!")
        else:
            if (greeting(user_response) != None):
                print("ROBO: " + greeting(user_response))
            else:
                print("ROBO: ", end = "")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("ROBO: Bye! Take Care!")