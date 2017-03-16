wordclean = sorted(list(set([word.strip().lower() for word in open('words','r')])))


sorted('lives')
sorted('lives') == sorted('elvis')
sorted('love') == sorted('hate')
def signature(word):
    return ''.join(sorted(word))
signature('lives')
'/'.join(['a','b','c'])
def anagram(word):
    return [w for w in wordclean if signature(w) == signature(word)]
print(anagram('dictionary'))
import collections
words_bysig = collections.defaultdict(list)
for word in wordclean:
    words_bysig[signature(word)].append(word)
print(words_bysig[:10])
