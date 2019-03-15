import nltk
import spacy
import re
from thesaurus import Word
import sys
import glob
import pandas as pd
import numpy as np
'''redact names'''
def redact_names(data):
    text=data
    doc=nlp(text)
    for entity in doc.ents:
        if entity.label_=='PERSON':
            stats.append([entity.text,len(entity.text),'Name'])
            text=text.replace(entity.text,'█'*len(entity.text))
    return text

'''redact addresses'''
def redact_addresses(data):
    text=data
    doc=nlp(text)
    for entity in doc.ents:
        if entity.label_=='FAC':
            stats.append([entity.text,len(entity.text),'Addresses'])
            text=text.replace(entity.text,'█'*len(entity.text))
    return text

'''redact dates'''
def redact_dates(data):
    text=data
    doc=nlp(text)
    for entity in doc.ents:
        if entity.label_=='DATE':
            stats.append([entity.text,len(entity.text),'Date'])
            text=text.replace(entity.text,'█'*len(entity.text))
    return text

'''redact phones'''
def redact_phones(data):
    text=data
    import re
    phone_numbers=[]
    phone_numbers=re.findall(r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}',text)
    for i in phone_numbers:
        stats.append([i,len(i),'Phone'])
        text=text.replace(i,'█'*len(i))
    return text

'''redact genders'''
def redact_genders(data):
    text=data
    genders_list=['he','she','him','her','his','hers','male','female','man','woman','men','women','He','She','Him','Her','His','Hers','Male','Female','Man','Woman','Men','Women','HE','SHE','HIM','HER','HIS','HERS','MALE','FEMALE','MAN','WOMAN','MEN','WOMEN']
    genders=''
    genders_lower=[]
    for i in genders_list:
        genders_lower.append(i.lower())
    for i in nltk.word_tokenize(data):
        if i.lower() in genders_lower:
            stats.append([i,len(i),'Gender'])
            genders+='█'*len(i)
            genders+=' '
        elif i=='.':
            genders+=i
            genders+=''
        else:
            genders+=i
            genders+=' '
    return genders

'''redact concept'''
def redact_concept(data,concept):
    from thesaurus import Word
    w = Word(concept)
    w1=[]
    for i in w .synonyms():
        w1.append(i.lower())
    w1.append(concept)
    concept1=''
    #sent=data.split('\n')
    for i in nltk.word_tokenize(data):
        if i.lower() in w1:
            stats.append([i,len(i),'Concept'])
            concept1+='█'*len(i)
            concept1+=' '
        elif i=='.':
            concept1+=i
            concept1+=''
        else:
            concept1+=i
            concept1+=' '
    return concept1

list=[]
list=sys.argv
files=[]
nlp = spacy.load('en_core_web_sm')
stats=[[]]
for i in range(len(list)):
    if list[i] == '--input':
        files.extend(glob.glob(list[i+1]))
for i in files:
    File = open(i) 
    data = File.read()
    for j in range(len(list)):
        if list[j] == '--names':
            data=redact_names(data)
        if list[j] == '--genders':
            data=redact_genders(data)
        if list[j] == '--dates':
            data=redact_dates(data)
        if list[j] == '--addresses':
            data=redact_addresses(data)
        if list[j] == '--phones':
            data=redact_phones(data)
        if list[j] == '--concept':
            data=redact_concept(data,list[j+1])
        if list[j] == '--output':
            file=open(i[:-4]+'.redacted.txt',"w")
            file.write(data)
            file.close()
        if list[j] == '--stats':
            df=pd.DataFrame(stats)
            df.to_csv(r'stats.txt', header=None, index=True, sep=' ', mode='a')

