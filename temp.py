messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]

messy_list.insert(0, messy_list.pop(3))
for item in messy_list.copy():
    if type(item) in [str, bool, list]:
        print("found")