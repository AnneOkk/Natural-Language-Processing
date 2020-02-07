from nltk.corpus import wordnet
syn = wordnet.synsets('entrepreneur')[0]
syn.name()
syn.definition()
syn.hypernyms()[0].hyponyms()
syn.hypernym_paths()

syn2 = wordnet.synsets('well-being')[0]
syn2.name()
syn2.definition()
syn2.hypernyms()[0].hyponyms()
syn2.hypernym_paths()

