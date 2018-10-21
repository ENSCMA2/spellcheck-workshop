import nltk
nltk.download("gutenberg")
nltk.download("punkt")

from collections import Counter 

from nltk.corpus import gutenberg 
from nltk.tokenize import word_tokenize as tokenizer

corpus = [] 

for txt in gutenberg.fileids(): 
	raw_text = gutenberg.raw(txt) 
	tokenized_text = tokenizer(raw_text) 
	corpus.extend(tokenized_text) 

word_corpus = Counter(corpus)
print(word_corpus)

def prob(word, N=sum(word_corpus.values())): 
	return word_corpus[word] / N

def edits1(word):
	letters = 'abcdefghijklmnopqrstuvwxyz'
	splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]  
	deletes = [L + R[1:] for L, R in splits if R]
	transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
	replaces   = [L + c + R[1:] for L, R in splits if R for c in letters]
	inserts = [L + c + R for L, R in splits for c in letters]
	return set(deletes + transposes + replaces + inserts) 

def edits2(word):
	return (e2 for e1 in edits1(word) for e2 in edits1(e1))

def known(words): 
    return set(w for w in words if w in word_corpus)
  
def candidates(word): 
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def correction(word): 
    return max(candidates(word), key=prob)

def testset(lines):
    return [(right, wrong) 
        for (right, wrongs) 
        in (line.split(':') for line in lines) 
        for wrong in wrongs.split()]

def spelltest(tests):
    good, unknown = 0, 0
    n = len(tests)
    for right, wrong in tests:
        w = correction(wrong)
        good += (w == right)
        if w != right:
            unknown += (right not in word_corpus)
    print(str(good / n * 100) + '% of ' + str(n) + ' correct')

spelltest(testset(open('spell-testset1.txt')))

wrong_word = input('Type in a word!')
while wrong_word != 'stop':
    print(correction(wrong_word))
    wrong_word = input('Type in a word!')