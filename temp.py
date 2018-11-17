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
    return string.upper(), string.lower(), string.capitalize(), string[::-1]

def combo(iter_1, iter_2):
    """
    Assume both iterables has same length
    combo([1, 2, 3], 'abc')
    Output:
    [(1, 'a'), (2, 'b'), (3, 'c')]
    """
    combo_list = []
    for x in range(len(iter_1)):
        tupl = iter_1[x], iter_2[x]
        combo_list.append(tupl)
    return combo_list

# +-----------------------------------+
# |             sets                  |
# +-----------------------------------+
COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

text = "I do not like it Sam I Am"
print(word_count(text))
print(stats({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], #
'Kenneth Love': ['Python Basics', 'Python Collections']}))

def covers(set_of_topics):
    course_list = []
    for course in COURSES:
        if len(COURSES[course] & set_of_topics) == len(set_of_topics):
            course_list.append(course)
    return course_list

# playground
print(covers({"conditions", "input"}))

# +-----------------------------------+
# |          Object Orientation       |
# +-----------------------------------+
class RaceCar():
    def __init__(self, color, fuel_remaining, **kwargs):
        self.laps = 0

        self.color = color
        self.fuel_remaining = fuel_remaining
        self.__dict__.update(kwargs)
    
    def run_lap(self, length):
        self.fuel_remaining -= 0.125 * length
        self.laps += 1

class Fruit():
	def squeeze(self):
		print("Squeezing")



