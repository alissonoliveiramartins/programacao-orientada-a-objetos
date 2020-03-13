import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('mac_morpho')
nltk.download('averaged_perceptron_tagger')
import string 

#Lista de todas as pontuações
pontuacao = list(string.punctuation)

sentence = "Dr. lucas, Nunca deixe ninguém te dizer que não pode fazer alguma coisa. Se você tem um sonho tem que correr atrás dele. As pessoas não conseguem vencer e dizem que você também não vai vencer. Se você quer uma coisa corre atrás."

#Separação do texto em frases
frase = nltk.tokenize.sent_tokenize(sentence)
print(frase,'\n')

#Separação do texto em palavras
tokens = nltk.word_tokenize( sentence )
print(tokens,'\n')

#Criando uma lista com todos os stop words
stop_words = set(stopwords.words( "portuguese" ))

#Removendo Stop_words
filtrado = [ word for word in tokens if not word in stop_words ]
print(filtrado,'\n')

#Removendo Pontuação
limpo = [ word for word in filtrado if not word in pontuacao ]
print(limpo,'\n')

text = "John saw the book on the table"
#Palavras com as Tag
analisada = nltk.pos_tag(nltk.word_tokenize(text))
print(analisada,'\n')
