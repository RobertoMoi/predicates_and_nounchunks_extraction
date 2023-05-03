import spacy
from spacy.matcher import Matcher
from spacy.util import filter_spans

from text import text_list

from remove_punctuation import remove_punctuation

from extract_noun_chunks import extract_noun_chunks
from extract_verbs import extract_verbs

from merge_redundant_nodes import merge_redundant_nodes

from remove_index_from_node import remove_index_from_node

if __name__ == '__main__':
    nlp = spacy.load("it_core_news_lg")

    noun_chunks_list = []
    noun_chunks_with_root_head = []
    merged_noun_chunks = []

    for text in text_list:
        text_without_punctuation = remove_punctuation(text, nlp)

        doc = nlp(text_without_punctuation)

        print("\nNoun chunk - radice noun chunk - dipendenza radice - testa della radice noun chunk:")
        extract_noun_chunks(doc, noun_chunks_with_root_head, noun_chunks_list)

        merged_noun_chunks.extend(noun_chunks_with_root_head)

        noun_chunks_with_root_head = remove_index_from_node(noun_chunks_with_root_head)

        merged_noun_chunks = merge_redundant_nodes(merged_noun_chunks)
       
        print(f"\nNoun chunks: \n{noun_chunks_list}")
        print(f"\nNoun chunks concatenati all'head della radice con nodi ripetitivi: \n{noun_chunks_with_root_head}")
        print(f"\nNoun chunks concatenati all'head della radice senza nodi ripetitivi: \n{merged_noun_chunks}")
        print(f"\nForme verbali: \n{extract_verbs(Matcher, nlp, doc, filter_spans)}")

        noun_chunks_with_root_head.clear()
        noun_chunks_list.clear()
        merged_noun_chunks.clear()
