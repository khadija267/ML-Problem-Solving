# Convert all the strings in the documents set to their lower case. Save them into a list called 'lower_case_documents'. 
documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']

lower_case_documents = []
for i in documents:
    lower_case_documents.append(i.lower())
# Remove all punctuation from the strings in the document set. Save them into a list called 'sans_punctuation_documents'. 
sans_punctuation_documents = []
import string

for i in lower_case_documents:
    sans_punctuation_documents.append(i.translate(str.maketrans('', '', string.punctuation)))

# Tokenize the strings stored in 'sans_punctuation_documents' using the split() method. Store the final document set in a list called 'preprocessed_documents'.
preprocessed_documents = []
for i in sans_punctuation_documents:
    preprocessed_documents.append(i.split(' '))
'''
create a dictionary with the keys being each word in each document and the corresponding values being the frequncy of occurrence of that word. Save each Counter dictionary as an item in a list called 'frequency_list'.
'''
frequency_list = []
import pprint
from collections import Counter

for i in preprocessed_documents:
    frequency_counts = Counter(i)
    frequency_list.append(frequency_counts)
pprint.pprint(frequency_list)
