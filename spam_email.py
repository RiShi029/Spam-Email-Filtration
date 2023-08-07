# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 16:15:40 2023

@author: Rishi Shivhare
"""

import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

import os
filename = "/tmp/not_exist/vectorizer.pkl"
os.makedirs(os.path.dirname(filename), exist_ok=True)
data = 'sadasdas'
with open('/tmp/not_exist/vectorizer.pkl', 'wb') as f:
    pickle.dump(data, f)

tfidf = pickle.load(open('E:/Project/Spam mine/vectorizer.pkl','rb'))
model = pickle.load(open('E:/Project/Spam mine/model.pkl','rb'))

st.title("Email Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")