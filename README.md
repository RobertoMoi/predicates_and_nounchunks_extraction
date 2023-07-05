# Extraction of predicates and noun chunks

Questa applicazione permette di estrarre i noun chunk e le forme verbali (predicati verbali e verbi copulativi) da un testo tramite l'algoritmo di spaCy.

L'estrazione dei noun chunk è stata perfezionata attraverso un algoritmo che unisce la testa della radice del noun chunk con il noun chunk stesso quando la loro relazione di dipendenza è uguale a "modificatore nominale".

## Installazione

1. Installare il pacchetto di spaCy tramite il comando:

`pip install -U spacy`

2. Scaricare la pipeline addestrata in italiano:

`python -m spacy download it_core_news_lg`

3. Eseguire il file python main.py

`python main.py`

### Aggiungere un testo da analizzare

1. Andare sul file text.py

2. Creare una variabile e assegnarli il testo da cui vogliamo estrarre i noun chunk e i predicati

3. Aggiungere la variabile appena creata alla lista text_list 

4. Avviare l'applicazione
