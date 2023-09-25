
import re
from collections import defaultdict, Counter
from stop_words import without_stopwords
from morphy import get_nouns, normalize


def load(path: str, encoding: str = "utf-8") -> str:
    with open(path, encoding=encoding, errors="ignore") as f:
        data = f.read()
    return data


def preprocess(text: str) -> str:
    # добавить энтити рекогнишн
    return text


def tokenize(text: str) -> list[str]:
    return re.findall(r"\w{2,}", text)


def count_words(words: list[str]) -> dict[str, int]:
    counter = {}
    for word in words:
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] += 1
    return counter


def count_words__default(words: list[str]) -> dict[str, int]:
    counter = defaultdict(int)
    for word in words:
        counter[word] += 1
    return counter


def count_words__count(words: list[str]) -> dict[str, int]:
    counter = {}
    for word in set(words):
        counter[word] = words.count(word)

    return counter


def count_words__counter(words: list[str]) -> dict[str, int]:
    counter = Counter(words)
    return counter.most_common(10)


if __name__ == "__main__":
    text = load("data/wizard_oz.txt", encoding="cp1251")
    text = preprocess(text)
    #words = tokenize(text)
    words = without_stopwords(tokenize(text))
    nouns = normalize(get_nouns(words))
    print(count_words__counter(nouns))
