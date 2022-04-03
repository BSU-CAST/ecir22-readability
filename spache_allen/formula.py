from pathlib import Path
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import sent_tokenize, TweetTokenizer

def spache(text, easy_words):
    stemmer = PorterStemmer()
    tokenizer = TweetTokenizer()
    tokens = tokenizer.tokenize(text)
    tokens = [t for t in tokens if t.isalnum()]

    num_words = len(tokens)
    if num_words == 0:
        return -1
    try:
        num_sentences = len(sent_tokenize(text))
    except LookupError:
        nltk.download('punkt')
        num_sentences = len(sent_tokenize(text))
    num_spache_complex = sum([1 for t in tokens if stemmer.stem(t.lower()) not in easy_words])

    avg_sentence_len = num_words / num_sentences
    percent_difficult_words = num_spache_complex / num_words * 100

    return (0.141 * avg_sentence_len) + (0.086 * percent_difficult_words) + 0.839


def spache_allen(text):
    spache_path = str(Path(__file__).resolve().parent.joinpath(
        "vocabulary", "spache_allen.txt"))
    with open(spache_path) as f:
        easy_words = set(line.strip() for line in f)

    return spache(text, easy_words)
