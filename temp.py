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

messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]

messy_list.insert(0, messy_list.pop(3))
for item in messy_list.copy():
    if type(item) in [str, bool, list]:
        print("found")