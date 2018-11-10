# Quick Python Reference
## Slicing
*Works for Str, List*
### Notation
    iterable_obj[start:stop:step]
*lists are muteable, strings are not. If you use* `[:]` *(slicing notation) you always work with a copy*
### Examples
#### half lower half upper string
    def half_lower_half_upper(word):
        middle = len(word) // 2
        return word[:middle].lower() + word[middle:].upper()
#### reverse even indexes
    def revers_even(iterable):
        if len(iterable) % 2:
            return iterable[::-2]
        else:
            return iterable[-2::-2]
