import httpx

URLS = [
    "https://raw.githubusercontent.com/stopwords-iso/stopwords-ru/master/stopwords-ru.txt"
    ]

def save_from_url(urls: str):
    stopwords = set()
    for url in urls:
        r = httpx.request('GET', url)
        current_stopwords = r.text.split('\n')
        stopwords |= set (current_stopwords)

    #content = r.text
    with open('data/stopwords.txt', 'w', encoding = "utf-8") as f:
        f.write('\n'. join(stopwords))

    #print (content)

def load_stopwords(path: str = "data/stopwords.txt") -> set[str]:
    stopwords = set()

    with open(path, encoding="utf-8") as f:
        for line in f:
            stopwords.add(line.rstrip())
    
    return stopwords

def without_stopwords(words: list[str]) -> list[str]:
    stopwords = load_stopwords()
    #filter list[lambda word: word not in stopwords, words] #Альтернативный вариант нижней строчки
    return [word for word in words if word.lower() not in stopwords] 

if __name__ == "__main__":
    save_from_url(URLS)

#ДОЛЖЕН СОЗНАТЬСЯ ФАЙЛИК СО СЛОВАМИ В DATA