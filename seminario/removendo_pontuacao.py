import nltk
nltk.download('punkt')
from nltk import word_tokenize
import string 

pontuacao = list(string.punctuation)

pontuacao.append("''")
print('Pontuações : ',pontuacao,'\n')

frase = '''He said,"that's it."'''

frase = word_tokenize(frase)
print('Frase "tokenizada" :',frase,'\n')

sem_pontuacao = []
for i in frase:
  if i not in pontuacao:
    sem_pontuacao.append(i)

print(' '.join(sem_pontuacao))