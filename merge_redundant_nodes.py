from remove_index_from_node import remove_index_from_node

"""
unisce due nodi adiacenti che contengono le stesse parole e rimuove il nodo con indice più basso
"""


def merge_redundant_nodes(nodes):
    words_with_index = []
    nodes_with_only_word = []

    # inizializza l'indice per scorrere la lista dei nodi
    i = 0

    # posizione della stringa all'interno della lista di liste -> [[stringa, indice iniziale, indice finale]]
    word_index = 0

    # posizione degli indici di inizio e di fine del noun chunk all'interno della lista di liste
    start_index = 1
    end_index = 2

    # segnala se in un nodo adiacente è presente una parola ripetuta
    there_is_repeated_word = False

    # per ogni elemento del nodo
    for element in nodes:
        # estrai le singole parole all'interno di un nodo e salvale in una lista
        only_words = element[word_index].split()

        # per ogni parola presente in un singolo nodo
        for word in only_words:
            # inserisci all'interno di una lista la parola, l'indice iniziale e l'indice finale
            words_with_index.append([word, element[start_index], element[end_index]])

        if i < len(nodes) - 1:
            i += 1

            # scorre ogni singola parola estratta dal nodo attuale
            for word in words_with_index:
                # se la parola appena estratta è contenuta all'interno del nodo adiacente
                # e se uno dei suoi indici si trova tra l'intervallo di inizio e di fine del nodo
                if (" " + word[word_index] + " ") in (" " + nodes[i][word_index] + " ") and \
                        (nodes[i][start_index] <= word[start_index] <= nodes[i][end_index] or
                         nodes[i][start_index] <= word[end_index] <= nodes[i][end_index]):

                    # rimuovi quella parola dal nodo attuale
                    nodes[i][word_index] = nodes[i][word_index].replace(word[word_index], "")

                    there_is_repeated_word = True

                # se la parola attuale è l'ultima parola estratta da un nodo
                # e se è presente una parola ripetuta
                if word == words_with_index[-1] and there_is_repeated_word:
                    # unisci i due nodi
                    nodes[i][word_index] = nodes[i-1][word_index] + nodes[i][word_index]
                    # rimuovi il nodo precedente che aveva delle parole in comune con il nodo attuale
                    nodes.pop(i-1)

            # reimposta il flag a false per il prossimo controllo
            there_is_repeated_word = False

    # lista dei nodi aggiornata senza indici
    nodes_with_only_word = remove_index_from_node(nodes)

    # restituisce la nuova lista di nodi
    return nodes_with_only_word
