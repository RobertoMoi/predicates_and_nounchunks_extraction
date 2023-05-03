'''
contiene tutti i noun chunks e i predicati/verbi dei testi da analizzare estratti con chatGPT,
per ogni testo vengono create due liste:
     - la prima contiene i noun chunks
     - la seconda contiene i predicati/verbi
'''

# macchina di Turing
noun_chunks_turing = ['La macchina di Turing',
                      'un modello astratto',
                      'una macchina',
                      'algoritmi',
                      'un nastro potenzialmente infinito',
                      'simboli',
                      'la computabilità massima',
                      'qualsiasi problema calcolabile',
                      'gli algoritmi Turing-computabili'
                      ]

predicates_turing = ['è',
                     'definisce',
                     'eseguire',
                     'dotata di',
                     'può leggere',
                     'può scrivere',
                     'possieda',
                     'risolvere',
                     'possono essere implementati',
                     'si dicono'
                     ]


# campionato di Serie A
noun_chunks_serieA = ['Il campionato di Serie A',
                      'la massima divisione professionistica',
                      'il calcio italiano maschile',
                      'la Lega Nazionale Professionisti Serie A',
                      "l'egida della FIGC",
                      'la prima edizione',
                      'il 1898',
                      "l'attuale formula",
                      'girone unico',
                      'la Juventus',
                      'la squadra più titolata',
                      '36 vittorie',
                      "l'Inter",
                      'la formazione più presente',
                      'la posizione della Serie A',
                      'il ranking UEFA',
                      'il numero delle squadre italiane',
                      'le coppe europee',
                      'il 2021',
                      'il 3º posto',
                      'la classifica mondiale dei campionati',
                      "l'IFFHS"
                      ]

predicates_SerieA = ['è',
                     'gestito',
                     'risale',
                     'è',
                     'è',
                     'è',
                     'determina',
                     'qualificate',
                     'posizionato',
                     'stilata'
                     ]

# Trattato di Maastricht
noun_chunks_trattatoMaastricht = ['Il Trattato di Maastricht',
                                  'la firma',
                                  'rappresentanti di 12 Paesi',
                                  'l\'Italia',
                                  'la città olandese di Maastricht',
                                  'l\'entrata in vigore',
                                  'la creazione dell\'Unione Europea',
                                  'la cooperazione tra i paesi',
                                  'nuovi ambiti',
                                  'la politica estera',
                                  'la sicurezza comune',
                                  'la cooperazione in materia di giustizia e affari interni',
                                  'le Comunità Europee',
                                  'tre organizzazioni',
                                  'la collaborazione economica',
                                  'la Comunità economica europea',
                                  'la Comunità europea del carbone e dell\'acciaio',
                                  'la Comunità europea dell’energia atomica'
                                  ]

predicates_trattatoMaastricht = ['è stato firmato',
                                 'è entrato in vigore',
                                 'è stato fondamentale',
                                 'è stata rafforzata e allargata',
                                 'avevano dato vita'
                                 ]


# Biathlon

noun_chunks_biathlon = ['Il biathlon',
                        'Uno sport invernale',
                        'Lo sci di fondo',
                        'Il tiro a segno',
                        'La carabina',
                        'La pratica competitiva',
                        'Pattuglia militare',
                        'Uno sport astruso',
                        'Costante crescita',
                        'Uno dei più popolari',
                        'Gli sport invernali',
                        'Il successo',
                        'La gestione',
                        'International Biathlon Union',
                        "L'organizzazione internazionale",
                        'Attività e interessi',
                        "Vent'anni"
                        ]

predicates_biathlon = ['è',
                       'combina',
                       'deriva',
                       'potrebbe essere considerato',
                       'è',
                       'è in costante crescita',
                       'è dovuto',
                       'cura',
                       'ha saputo adattare',
                       'promuovere',
                       'vendere'
                       ]

# Giacomo Leopardi

noun_chunks_giacomo_leopardi = ['Giacomo Leopardi',
                                'un poeta',
                                'filosofo',
                                'scrittore',
                                'filologo italiano',
                                'una delle più importanti figure della letteratura mondiale',
                                'il maggior poeta dell\'Ottocento italiano',
                                'uno dei principali esponenti del romanticismo letterario',
                                'questa corrente',
                                'la sua riflessione sull\'esistenza e sulla condizione umana',
                                'un importante filosofo',
                                'la qualità lirica della sua poesia',
                                'un protagonista centrale nel panorama letterario e culturale internazionale',
                                'l\'età di 39 anni',
                                'il dibattito sull\'opera leopardiana', 'gli esegeti',
                                'l\'analisi filosofica dei contenuti e significati dei suoi testi',
                                'un precursore dell\'Esistenzialismo']

predicates_giacomo_leopardi = ['è stato', 'considerato', 'è considerato', 'ha sempre criticato', 'rendono',
                              'lo ha reso', 'Morì', 'ha portato', 'approfondire', 'vedono']

# bitcoin
noun_chunks_bitcoin = ['Il Bitcoin',
                       'una criptovaluta',
                       'il 2009',
                       'Satoshi Nakamoto',
                       'una riserva di valore',
                       'molto volatile',
                       'il valore',
                       'la leva domanda e offerta',
                       'la rete Bitcoin',
                       'il possesso e il trasferimento pseudo-anonimo delle monete',
                       'i dati necessari', 'utilizzare i propri bitcoin',
                       'uno o più personal computer',
                       'dispositivi elettronici',
                       'smartphone',
                       'forma di "portafoglio" digitale',
                       'terze parti',
                       'funzioni simili',
                       'una banca',
                       "l'unico dato",
                       'un pagamento',
                       "l'indirizzo bitcoin",
                       'un codice alfanumerico',
                       'la struttura peer-to-peer della rete Bitcoin',
                       'la mancanza di un ente centrale',
                       'qualunque autorità',
                       'il blocco dei trasferimenti'
                       ]

predicates_bitcoin = ['creata',
                      'viene considerata',
                      'è determinato',
                      'consente',
                      'possono essere salvati',
                      'mantenuti',
                      'svolgono',
                      'identificato',
                      'rende impossibile',
                      'il blocco dei trasferimenti'
                      ]


# spedizione dei mille
noun_chunks_spedizione_dei_mille = ['La spedizione dei Mille',
                                    "l'impresa più importante del Risorgimento italiano",
                                    'Nino Bixio',
                                    'Francesco Crispi',
                                    'Giuseppe Garibaldi',
                                    'due piroscafi',
                                    'Quarto',
                                    'Genova',
                                    '1162 volontari',
                                    'Talamone',
                                    'i Mille',
                                    'Sicilia',
                                    'la dittatura',
                                    'il re Vittorio Emanuele II',
                                    'le truppe borboniche',
                                    'Palermo',
                                    'il controllo del Regno delle Due Sicilie',
                                    'Vittorio Emanuele II',
                                    'Teano',
                                    'la spinta decisiva',
                                    'il processo di unificazione nazionale italiana',
                                    'intellettuali',
                                    'professionisti',
                                    'insegnanti',
                                    'operai',
                                    'artigiani'
                                    ]

predicates_spedizione_dei_mille = ['rappresenta',
                                   'fu ideata',
                                   'convinsero',
                                   'guidare',
                                   'partirono',
                                   'rimasero',
                                   'passarono',
                                   'arrivati',
                                   'proclamò',
                                   'sconfisse',
                                   'occupando',
                                   'depose',
                                   'rappresentò',
                                   'vide',
                                   'la partecipazione'
                                   ]

# giove
noun_chunks_giove = ['Il pianeta Giove',
                     'il sistema solare',
                     'il quinto posto',
                     'distanza',
                     'il Sole',
                     'un gigante gassoso',
                     'composizione',
                     'idrogeno',
                     'elio',
                     'tracce',
                     'altri gas composti',
                     'una struttura pluristratificata',
                     'una vasta atmosfera',
                     'bande e zone di tonalità variabili',
                     'rotazione',
                     'aspetto',
                     'uno sferoide schiacciato ai poli',
                     'un intenso campo magnetico',
                     'una magnetosfera estesa',
                     'una quantità di energia',
                     'meccanismo di Kelvin-Helmholtz',
                     'il suo intenso campo gravitazionale',
                     'le orbite degli altri pianeti nel sistema solare',
                     'i detriti',
                     'i pianeti più interni',
                     'numerosi satelliti',
                     'un sistema di anelli',
                     'orbite',
                     'due gruppi di asteroidi troiani'
                     ]

predicates_giove = ['è',
                    'si trova',
                    'costituito',
                    'ha',
                    'caratterizzata',
                    'conferisce',
                    'emette',
                    'riceve',
                    'perturba',
                    'ripulisce',
                    'stabilizza'
                    ]

# wsop

noun_chunks_wsop = ['Le World Series of Poker (WSOP)',
                    'l\'evento di poker sportivo più prestigioso del mondo',
                    'ogni anno a Las Vegas',
                    'l\'espansione europea delle WSOP',
                    'World Series of Poker Europe',
                    'le World Series of Poker Asia Pacific',
                    'Giocatori di tutto il mondo',
                    'una serie di tornei',
                    'tutte le specialità del poker',
                    'varie quote di iscrizione',
                    '500 a 50 000 dollari',
                    'il torneo più importante',
                    'il titolo di campione del mondo',
                    'la specialità del poker Texas hold\'em',
                    'la variante senza limite',
                    'il giocatore vincitore di ogni torneo',
                    'un consistente premio in denaro',
                    'un prestigioso braccialetto delle WSOP'
                    ]

predicates_wsop = ['sono',
                   'vengono disputate',
                   'è organizzata',
                   'sono state introdotte',
                   'si sfidano',
                   'comprendenti',
                   'varie quote di iscrizione',
                   'assegna',
                   'giocato',
                   'viene assegnato'
                   ]

# barriera corallina

noun_chunks_barriera_corallina = ['La barriera corallina',
                                  'una formazione rocciosa sottomarina',
                                  'coralli',
                                  'mari e oceani tropicali',
                                  'queste formazioni',
                                  'la biodiversità',
                                  'isole e lagune',
                                  'mare profondo',
                                  'acque a bassa penetrazione della luce',
                                  'acque profonde senza luce',
                                  'la costa',
                                  'la fascia marginale',
                                  'la piattaforma carbonatica',
                                  'il mare',
                                  'lo 0,1% del fondo oceanico della Terra',
                                  'il 25% di tutte le specie marine del pianeta'
                                  ]

predicates_barriera_corallina = ['è',
                                 'si trova',
                                 'sono',
                                 'possono creare',
                                 'possono essere presenti',
                                 'si trovano',
                                 'costituiscono',
                                 'supportano'
                                 ]