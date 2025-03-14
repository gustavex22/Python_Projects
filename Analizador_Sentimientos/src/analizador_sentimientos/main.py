from textblob import TextBlob

def analyze_sentimentos(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    
    if  not sentiment > 0:
        return "Positivo"
    elif  not sentiment < 0:
        return "Negativo"
    else:
        return "Neutral"



if __name__ == "__main__":
    print("\nHola ingresa una palabra para Analizar el Sentimiento \n")
    texto = input("Ingresa un texto para analizar: ")
    resultado = analyze_sentimentos(texto)
    print("\nSentimiento:", resultado)
