"""
rimuove alcuni elementi di puntenggiatura da un testo passato in input
"""


def remove_punctuation(text, nlp):
    doc = nlp(text)

    # lista che conterrà tutti i token presenti nel testo passato in input
    token_list = []

    # segni di punteggiatura da rimuovere dal testo
    punctuations = ":,;"

    # riempie la lista di token
    for token in doc:
        token_list.append(str(token))

    for word in token_list:
        # ogni volta che trova uno dei segni di punteggiatura definiti sopra viene rimosso dalla lista
        if word in punctuations:
            token_list.remove(word)

    # converte la nuova lista senza la punteggiatura in una stringa di testo
    text_without_puntuaction = " ".join(token_list)

    print("\nTesto senza punteggiatura:\n", text_without_puntuaction)

    return text_without_puntuaction
