# ChatBotNLP

![Cabecera](https://user-images.githubusercontent.com/9929241/133822593-4deb76f4-0007-4c12-828e-18923ce69ca8.png)

Chatbot basado en NLP para una IA fiable


Pasos a realizar para la creación del chat bot sobre IA Fiable:

1. Buscar información sobre bibliotecas de _Natural Language Processing_ :
  * Actualmente estamos trabajando sobre NLTK y redes neuronales
  * Sería interesante saber como funcionan las bibliotecas [Transformer](https://huggingface.co/transformers/usage.html)
  * Opciones descartadas --> [Dialogflow](https://dialogflow.cloud.google.com/)
  * He visto que el tema 9 y 10 de la asignatura de PNL habla sobre Chatbots. Sería conveniente leerlo.

2. El chat bot será capaz de clasificar segun la entrada del usuario que tipo de aplicación esta desarrollando el usuario.

3. Cuando identifiquemos que tipo de aplicación estamos usando el chat realizará un grupo de preguntas asociadas "QuestionAnswering"

4. El chabot será capaz de guardar las respuesta.

5. En base a las respuestas, el chatbot será capaz de realizar un calculo para puntuar la aplicación del usuario.



## Flujo de trabajo

1. Tokenización de las cadenas para el entrenamiento
```python
from nltk import ToktokTokenizer

tokenize(sentence)
```

2. Leminizar el texto para el entrenamiento

```python
!python -m spacy download es_core_news_sm

import spacy
#Tokenización y leminizar el texto
nlp = spacy.load('es_core_news_sm')
tokenized_text = nlp(text)
tokenized_text = [token.lemma_ for token in tokenized_text]
```
