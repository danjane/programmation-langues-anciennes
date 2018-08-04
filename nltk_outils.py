from cltk.stem.lemma import LemmaReplacer
from cltk.stem.latin.j_v import JVReplacer
from cltk.tokenize.word import WordTokenizer

def tokenize(text, language = "latin"):
    jv_replacer = JVReplacer()
    text = jv_replacer.replace(text.lower())

    t = WordTokenizer(language)
    l = LemmaReplacer(language)

    text_word_tokens = t.tokenize(text)

    # Garde les mots de plus de trois characters
    ## text_word_tokens = [token for token in text_word_tokens if token not in ['.', ',', ':', ';','*']]
    text_word_tokens = [token for token in text_word_tokens if len(token) > 3]

    text_word_tokens = l.lemmatize(text_word_tokens)

    return text_word_tokens