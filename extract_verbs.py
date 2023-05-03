"""
estrae i verbi copulativi e i predicati verbali da un testo passato in input
"""


def extract_verbs(Matcher, nlp, text, filter_spans):

    # definisce il pattern per trovare i predicati verbali e i verbi copulativi
    pattern = [[{'POS': 'AUX'}, {'POS': 'AUX'}, {'POS': 'VERB'}],
               [{'POS': 'AUX'}, {'POS': 'VERB'}],
               [{'POS': 'AUX', 'OP': '+'}],
               [{'POS': 'VERB', 'OP': '+'}]
               ]

    # inizializza un'istanza del matcher
    matcher = Matcher(nlp.vocab)
    matcher.add("forme verbali", pattern)

    # ricerca tutte le corrispondenze del pattern nel testo passato come parametro e restituisce una lista di tuple
    matches = matcher(text)
    # inserisce tutte le corrispondenze trovate in una lista
    spans = [text[start:end] for match_id, start, end in matches]

    # restituisce la lista con tutte le parole trovate dal matcher che rispettino il pattern definito in precedenza
    # filter_spans evita che alcune parole possono essere stampate più volte
    return filter_spans(spans)

