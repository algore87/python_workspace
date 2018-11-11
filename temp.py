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

# +-----------------------------------+
# |             tuples                |
# +-----------------------------------+
#### tuple packing/unpacking
def multiply(*args):
    multiplyer = 1
    for arg in args:
        multiplyer *= arg
    return multiplyer

def stringcases(string):
    try:
        strcasetuple = string.upper(), string.lower(), string.capitalize(), string[::-1]
        return strcasetuple
    except AttributeError as err:
        print(err)
        return -1

# playground
print(stringcases(34))