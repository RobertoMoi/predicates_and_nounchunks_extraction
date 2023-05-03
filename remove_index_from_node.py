def remove_index_from_node(nodes):
    nodes_without_index = []
    word_index = 0  # indice delle parole all'interno della lista

    # viene generata una nuova lista che contiene solo le parole
    for element in nodes:
        nodes_without_index.append(element[word_index])

    return nodes_without_index
