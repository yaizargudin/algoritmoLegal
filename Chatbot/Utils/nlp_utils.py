import nltk
import numpy as np
# nltk.download('punkt')
from nltk import ToktokTokenizer
from nltk.stem import SnowballStemmer
from nltk.stem.porter import PorterStemmer
import spacy
import re
from unicodedata import normalize

stemerSpanish = PorterStemmer()

nlp = spacy.load('es_core_news_sm')

def eliminar_diacriticos(palabra):
    """
    Función para eliminar los diacríticos de la palabra de entrada
    :param palabra:
    :return:
    """
    # -> NFD (forma descompuesta) y eliminar diacríticos
    palabra = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
        normalize("NFD", palabra), 0, re.I
    )
    # -> NFC (forma compuesta) y devuelve palabra
    return normalize('NFC', palabra)

def tokenize(sentence):
    """
    Función para dividir en tokens una frase
    :param sentence:
    :return:
    """
    m_took: ToktokTokenizer = ToktokTokenizer()
    # return nltk.word_tokenizer(sentence)
    return m_took.tokenize(sentence)


def stem(word):
    """
    TODO: Buscar un stemmer en español, ahora mismo se va a entrenar con las palabras completas
    :param word:
    :return:
    """
    tokenized_text = nlp(word)
    tokenized_text = [token.lemma_ for token in tokenized_text]
    return stemerSpanish.stem(tokenized_text[0].lower())


def bag_of_words(tokenized_sentence, all_words):
    """
    Devuelve una bow
    1 por cada palabra conocida que existe en la oración, 0 en caso contrario
    ejemplo:
    sentence = ["hello", "how", "are", "you"]
    all_words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bag   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0

    return bag