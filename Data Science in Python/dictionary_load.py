word = open('words','r')
wordlist = word.readlines()
wordlist[:10]
len(wordlist)
wordclean = [word.strip().lower() for word in wordlist]
wordclean[:10]
wordunique = list(set(wordclean))
wordunique
wordunique.sort()
wordclean = sorted(list(set([word.strip().lower() for word in open('words','r')])))
