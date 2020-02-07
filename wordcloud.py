from nltk.corpus import wordnet
syns = wordnet.synsets("health")
print(syns)

synonyms = []
new_syn = []

for syn in wordnet.synsets("entrepreneur"):
	for l in syn.lemmas():
		synonyms.append(l.name())

print(set(synonyms))

for syn in wordnet.synsets("business owner"):
	for l in syn.lemmas():
		synonyms.append(l.name())

print(set(synonyms))

for syn in wordnet.synsets("self-employed"):
	for l in syn.lemmas():
		synonyms.append(l.name())

print(set(synonyms))


for syn in wordnet.synsets("satisfaction"):
	for l in syn.lemmas():
		synonyms.append(l.name())

print(set(synonyms))

for syn in wordnet.synsets("health"):
	for l in syn.lemmas():
		synonyms.append(l.name())

print(set(synonyms))

for syn in wordnet.synsets("well-being"):
	for l in syn.lemmas():
		synonyms.append(l.name())

print(set(synonyms))

for syn in wordnet.synsets("affect"):
	for l in syn.lemmas():
		synonyms.append(l.name())

print(set(synonyms))

for syn in wordnet.synsets("burnout"):
	for l in syn.lemmas():
		synonyms.append(l.name())

print(set(synonyms))

for syn in wordnet.synsets("exhaustion"):
	for l in syn.lemmas():
		synonyms.append(l.name())

print(set(synonyms))

for syn in wordnet.synsets("strain"):
	for l in syn.lemmas():
		synonyms.append(l.name())

print(set(synonyms))

for syn in wordnet.synsets("stress"):
	for l in syn.lemmas():
		synonyms.append(l.name())

print(set(synonyms))

for syn in wordnet.synsets("emotion"):
	for l in syn.lemmas():
		synonyms.append(l.name())

print(set(synonyms))

for syn in wordnet.synsets("meaningfulness"):
	for l in syn.lemmas():
		synonyms.append(l.name())

print(set(synonyms))

for syn in wordnet.synsets("hedonic"):
    for l in syn.lemmas():
        new_syn.append(l.name())

print(set(new_syn))

for syn in wordnet.synsets("thriving"):
    for l in syn.lemmas():
        new_syn.append(l.name())

print(set(new_syn))
