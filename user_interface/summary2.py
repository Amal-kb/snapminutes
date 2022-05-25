from django.shortcuts import render

from user_interface.models import admin1, meeting

def summarygenFun(request):
    import re # relugar expression
     # natural language toolkit
    import string
    import nltk
    email=request.session['aemail']
    admin=admin1.objects.get(email=email)
    orgid=admin.orgid_id
    meet = meeting.objects.all()

   
    text=request.session['text']
    importent=request.session['agenda']
    number=request.session['number']
    number=int(number)
    print(number+2)
    print(importent)

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
    
    formatted_text = preprocess(importent)
    print(formatted_text)

    word_frequency = nltk.FreqDist(nltk.word_tokenize(formatted_text))

    highest_frequency = max(word_frequency.values())
    print(highest_frequency)

    for word in word_frequency.keys():
        #print(word)
        word_frequency[word] = (word_frequency[word] / highest_frequency)

    sentence_list =original_text.split('.')
    sentence_list

    score_sentences = {}
    for sentence in sentence_list:
        #print(sentence)
        for word in nltk.word_tokenize(sentence.lower()):
        #print(word)
            if sentence not in score_sentences.keys():
                score_sentences[sentence] = word_frequency[word]
            else:
                score_sentences[sentence] += word_frequency[word]


    dc = {k: v for k, v in score_sentences.items() if v + 0 != 0}
    print(dc)
    score_sentences=dc  

    import heapq
    best_sentences = heapq.nlargest(number, score_sentences, key = score_sentences.get)

    summary = '. '.join(best_sentences)
    
    data = {'summary':summary}
    data['text']=text
    data['agenda']=importent
    data['number']=number
    data['orgid']=orgid
    data['meet']=meet
    return render(request,'speech.html',context=data)




