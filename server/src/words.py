from random import sample
from collections import defaultdict
from xml.etree import ElementTree

root = ElementTree.parse('sanalista.xml').getroot()
words = []
for element in root:
    word = element[0].text
    words.append(word)

def sample_words(amount: int) -> list:
    return sample(words, amount)

def check_anagram(word: str, candidate: str) -> bool:
    if not candidate in words:
        print('word not found')
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
  
