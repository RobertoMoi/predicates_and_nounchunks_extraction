'''
estrae i noun chunks da un testo passato come parametro e successivamente vengono inseriti in una lista.
'''


def extract_noun_chunks(text, nodes, noun_chunks_list):
    for chunk in text.noun_chunks:
        # rappresentano gli indici delle parole che fanno parte del noun chunk
        start = chunk.start  # indice di inizio
        end = chunk.end - 1  # indice di fine

        print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)

        # il noun chunk appena trovato viene inserito in una lista
        noun_chunks_list.append(chunk.text)

        # se la dipendenza tra il "root" del chunk e il suo "head" è di tipo "nmod"
        # e se il testo del head non è già incluso nel testo del chunk
        if chunk.root.dep_ == "nmod" and str(chunk.root.head.text) not in str(chunk.text):
            # allora aggiungi alla lista dei nodi la concatenazione tra il testo dell'head e il noun chunk
            # insieme ai loro indici
            nodes.append([chunk.root.head.text + " " + chunk.text, chunk.root.head.i, end])
        else:  # altrimenti aggiungi solo il noun chunk con gli indici di inizio e di fine
            nodes.append([chunk.text, start, end])
