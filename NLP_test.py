import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer 
from keras.api.models import Sequential, load_model
from keras.api.layers import Dense, Activation, Dropout
from keras.api.optimizers import SGD 
from googletrans import Translator
from controls.sound_control import sesli_cevap
def installation_chat():
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('punkt_tab')

    lemmatizer = WordNetLemmatizer()
    intents = json.loads(open("intens.json").read())  # Dikkat: dosya adı doğru olmalı
    words = []
    classes = []
    documents = []
    ignore_letters = ['?','!','.','']

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            word_list = nltk.word_tokenize(pattern)
            words.extend(word_list)
            documents.append((word_list, intent['tag']))
            if intent['tag'] not in classes:
                classes.append(intent['tag'])

    # Lemmatiize ve gereksiz karakterleri temizle
    words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_letters]
    words = sorted(set(words))
    classes = sorted(set(classes))

    # Kelimeler ve sınıfları pickle ile kaydet
    pickle.dump(words, open('words.pkl', 'wb'))
    pickle.dump(classes, open('classes.pkl', 'wb'))

    # Eğitim verisini oluştur
    training = []
    output_empty = [0] * len(classes)

    for document in documents:
        bag = []
        word_patterns = document[0]
        word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]

        # Bag oluşturma (kelimelerin varlığına göre 1 veya 0 ekleme)
        for word in words:
            bag.append(1) if word in word_patterns else bag.append(0)

        output_row = list(output_empty)
        output_row[classes.index(document[1])] = 1
    
        if len(bag) == len(words) and len(output_row) == len(classes):
            training.append([bag, output_row])
        else:
            print("Length mismatch:", len(bag), len(output_row))
    
    random.shuffle(training)
    
    training = np.array(training, dtype=object)
    

    train_x = list(training[:,0])
    train_y = list(training[:,1])

    model = Sequential()
    model.add(Dense(128,input_shape=(len(train_x[0]),), activation = 'relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation = 'relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(train_y[0]), activation = 'softmax'))
    sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy',optimizer = sgd, metrics=['accuracy'])

    hist = model.fit(np.array(train_x), np.array(train_y), epochs=200,batch_size =5,verbose=1)
    model.save('chatbotmodel.h5',hist)

 
def start_chat(komut):
    lemmatizer = nltk.WordNetLemmatizer() 
    intents = json.loads(open('intens.json').read()) 
    words = pickle.load(open('words.pkl', 'rb'))
    classes = pickle.load(open('classes.pkl', 'rb')) 
    model = load_model('chatbotmodel.h5') 
    def clean_up_sentence(sentence):
        sentence_words = nltk.word_tokenize(sentence) 
        print(f"Tokenized words: {sentence_words}")   
        word_patterns = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]  
        return word_patterns
    
    def bag_of_words(sentence):
        sentence_words = clean_up_sentence(sentence)
        bag = [0] * len(words)
        for w in sentence_words:
            for i, word in enumerate(words):
                if word == w:
                    bag[i] = 1
        return np.array(bag)
    
    def predict_class(sentence):
        p = bag_of_words(sentence)
        res = model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.1
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
        return return_list
    
    def get_response(intents_list, intents_json):
        try:
            tag = intents_list[0]['intent']
            list_of_intents = intents_json['intents']
            for i in list_of_intents:
                if i['tag'] == tag:
                    result = random.choice(i['responses'])
                    break
        except IndexError:
            result = "I don't understand!"
        return result
    import requests
    URL = "https://api.mymemory.translated.net/get"

# Çeviri fonksiyonu
    def translate(text, source_lang, target_lang):
        params = {
            "q": text,
            "langpair": f"{source_lang}|{target_lang}"
        }
        response = requests.get(URL, params=params)
        
        # JSON formatında gelen cevaptan çeviriyi alıyoruz
        if response.status_code == 200:
            return response.json()['responseData']['translatedText']
        else:
            print("Çeviri hatası:", response.text)
            return None

    # İngilizceyi Türkçeye çevirme
    def english_to_turkish(english_text):
        return translate(english_text, 'en', 'tr')

    # Türkçeyi İngilizceye çevirme
    def turkish_to_english(turkish_text):
        return translate(turkish_text, 'tr', 'en')
     
    message = komut
    ints = predict_class(turkish_to_english(message))
    res = get_response(ints, intents)
    print(english_to_turkish(res))
    sesli_cevap(english_to_turkish(res))
