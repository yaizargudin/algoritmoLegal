from flask import Flask, request
import re
from unicodedata import normalize
import evaluacion


prioridad_baja = 0.5
priodad_alta = 1

app = Flask(__name__)
umbral = priodad_alta

preguntas = evaluacion.evaluar



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


@app.route('/',methods=["POST","GET"])
def webhook():
    indice = 0

    if request.method == "GET":
        return "Error not conected to DF"
    elif request.method == "POST":
        payload = request.json
        user_response = (payload['queryResult']['queryText'])
        bot_response = (payload['queryResult']['fulfillmentText'])

        if(payload['queryResult']['action'].find('evaluar_') != -1):
            print("Pregunta: ", payload['queryResult']['fulfillmentText']) #TODO Agregar al diccionario


        if('allRequiredParamsPresent' in payload['queryResult']):
            print("FINAL DE EVALUACION")

            for parameter, value in payload['queryResult']['parameters'].items():
                if(value != ""):
                    if(eliminar_diacriticos(value.lower()) == "si"):
                        indice += 0

                    elif(eliminar_diacriticos(value.lower()) == "no"):
                        indice += preguntas[parameter]["importancia"]
                        
                        
            if(indice >= umbral):
                print(" Tu algoritmo no supera esto bla bla bla...")
                return {
                        "fulfillmentText": 'Tu algoritmo no supera esto. Gracias por completar la evaluación de su algoritmo IA de roboadvisors. ¿Necesita alguna cosa más?',
                        "source": 'webhook'
                        }
            else:
                return {
                    "fulfillmentText": 'Tu algoritmo supera esto bla bla bla...',
                    "source": 'webhook',
                }




        if user_response or bot_response !="":
            print("User: "+user_response)
            print("Bot: "+bot_response)




            return"Message received"
        else:
            print(request.data)
            return"200"

if __name__ == '__main__':
    app.run(debug=True)