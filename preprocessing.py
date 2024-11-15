import nltk
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

nltk.download('punkt')
nltk.download('stopwords')

factory = StemmerFactory()
stemmer = factory.create_stemmer()

text = 'NLP memiliki banyak sekali fungsi: bisa untuk membuat chatbot, analisis sentimen, grammar check, mengekstrak informasi, dan lainnya.'

text = text.lower()
print("case folding:", text)

text = text.translate(str.maketrans("", "", string.punctuation))
print("Punctual removal:", text)

tokens = word_tokenize(text)
print("Tokenization:", tokens)

stop_words = set(stopwords.words('indonesian'))
filtered_tokens = [word for word in tokens if word not in stop_words and word.isalnum()]
print("Stop words removal:", filtered_tokens)

stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
print("Stemming:", stemmed_tokens)
