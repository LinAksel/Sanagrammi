from random import sample
from collections import defaultdict
from xml.etree import ElementTree

root = ElementTree.parse('sanalista.xml').getroot()
words = []
for element in root:
    word = element[0].text
    words.append(word)

def find_anagrams(word):
    chars = defaultdict(int)
    anagrams = []
    for char in word:
        chars[char] += 1

    for w in words:
        if len(w) > len(word):
            continue

        if w == word:
            continue

        chars_copy = chars.copy()
        is_anagram = True
        for char in w:
            if chars_copy[char] < 1:
                is_anagram = False
                break
            chars_copy[char] -= 1

        if is_anagram and not w in anagrams:
            anagrams.append(w)
    return anagrams

def sample_words(amount: int) -> list:
    return sample(words, amount)

def random_word():
    word = sample_words(1)[0]
    while len(find_anagrams(word)) < 20:
        print(word)
        word = sample_words(1)[0]
    return word

def check_anagram(word: str, candidate: str) -> bool:
    if not candidate in words:
        return False

    chars = defaultdict(int)
    for char in word:
        chars[char] += 1    

    is_anagram = True
    for char in candidate:
        if chars[char] < 1:
            is_anagram = False
            break
        chars[char] -= 1

    return is_anagram
  
