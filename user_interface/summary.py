from django.shortcuts import render

def summarygenFun(request):
    import re # relugar expression
     # natural language toolkit
    import string
    import nltk

    text=request.session['text']

    original_text =text
    
    original_text = re.sub(r'\s+', ' ', original_text)

    nltk.download('punkt')

    nltk.download('stopwords')

    stopwords = nltk.corpus.stopwords.words('english')

    def preprocess(text):
        formatted_text = text.lower()
        tokens = []
        for token in nltk.word_tokenize(formatted_text):
            tokens.append(token)
        tokens = [word for word in tokens if word not in stopwords and word not in string.punctuation]
        formatted_text = ' '.join(element for element in tokens)
        return formatted_text
    
    formatted_text = preprocess(original_text)

    word_frequency = nltk.FreqDist(nltk.word_tokenize(formatted_text))

    highest_frequency = max(word_frequency.values())

    for word in word_frequency.keys():
        #print(word)
        word_frequency[word] = (word_frequency[word] / highest_frequency)

    sentence_list = nltk.sent_tokenize(original_text)

    score_sentences = {}
    for sentence in sentence_list:
        #print(sentence)
        for word in nltk.word_tokenize(sentence.lower()):
        #print(word)
            if sentence not in score_sentences.keys():
                score_sentences[sentence] = word_frequency[word]
            else:
                score_sentences[sentence] += word_frequency[word]



    import heapq
    best_sentences = heapq.nlargest(3, score_sentences, key = score_sentences.get)

    summary = ' '.join(best_sentences)
    
    data = {'summary':summary}
    data['text']=text
    return render(request,'speech.html',context=data)




