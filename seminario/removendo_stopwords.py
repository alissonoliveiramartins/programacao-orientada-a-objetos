import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords

# inserimos um texto aleatório
texto = "João amava Teresa que amava Raimundo que amava Maria que amava Joaquim que amava Lili que não amava ninguém."

sentences = nltk.sent_tokenize(texto)

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    newwords = [word for word in words if word not in stopwords.words('portuguese')]
    sentences[i] = ' '.join(newwords)
    
print (sentences)