#### half lower half upper string
def half_lower_half_upper(word):
    middle = len(word) // 2
    return word[:middle].lower() + word[middle:].upper()
#### reverse even indexes
def revers_even(iterable):
    if len(iterable) % 2: # odd length (last index is even)
        return iterable[::-2]
    else: # even length (last index is odd)
        return iterable[-2::-2]

#### word count
def word_count(text):
	word_dict = {}
	word_list = text.lower().split(" ")
	for word in word_list:
		if word in word_dict:
			word_dict[word] += 1
		else:
			word_dict[word] = 1
	return word_dict

#### treehouse collections challenge
def stats(adict):
    stat_list = []
    for teacher in adict:
        stat_list.append([teacher, len(adict[teacher])])
    return stat_list

# playground
messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]

messy_list.insert(0, messy_list.pop(3))
for item in messy_list.copy():
    if type(item) in [str, bool, list]:
        print("found")

text = "I do not like it Sam I Am"
print(word_count(text))
print(stats({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], #
'Kenneth Love': ['Python Basics', 'Python Collections']}))