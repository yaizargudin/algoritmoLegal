# Este archivo usa el encoding: utf-8
import random
import json

import torch

from model import NeuralNet
from Utils.nlp_utils import bag_of_words, tokenize, eliminar_diacriticos


def chat_bot_pytorch():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    with open('intents.json', 'r', encoding="utf-8") as json_data:
        intents = json.load(json_data)

    FILE = "data.pth"
    #data = torch.load(FILE)
    data = torch.load(FILE, map_location=device)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    bot_name = "Al"
    print("Bienvenido a la asesoria de Algoritmo Legal")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        # Eliminar diacríticos y convertir texto a minúsculas
        sentence = eliminar_diacriticos(sentence)
        sentence = tokenize(sentence.lower())
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)
        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.8:
            for intent in intents['intents']:
                # TODO Aqui podemos saber sobre que esta preguntando poder manejar la conversación... Tipos de chats a los que preguntar
                # Forzar alguna respuesta etc..

                if tag == intent["tag"]:
                    response  = random.choice(intent['responses'])
                    print(f"{bot_name}: {response}")

        else:
            print(f"{bot_name}: Podrias repetir, ¿por favor?")
