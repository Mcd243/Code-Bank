######################### Linear search #########################

"""search_linear.py
   Linear search for spell check
   pylint, function annotations: Mar 2021
"""


def lin_search(target: str, words: list) -> bool:
    """Linear search for target in words. words need not be sorted"""
    for word in words:
        if word == target:
            return True
    return False


# Get a list of words
wordlist = [s.strip("\n").lower() for s in open("words.txt")]    
# tests
for w in ["acomodation", "buchanan", "macintosh", "zebede"]:
    if not lin_search(w, wordlist):
        print(w)


###################### Binary search ##########################


"""search_binary.py
   Binary search for spell check
   pylint, function annotations: Mar 2021
"""


def bin_search(low: int, high: int, target: str) -> bool:
    """Binary search for target in words.
       words must be declared elsewhere and a sorted list."""
    if low >= high:
        return False
    mid = (low+high) // 2
    piv = words[mid]
    if piv == target:
        return True
    if piv < target:
        return bin_search(mid+1, high, target)
    return bin_search(low, mid, target)


# Get a list of words
words = [s.strip("\n").lower() for s in open("words.txt")]          
words.sort()  # sort the list
# tests
for w in ["acomodation", "buchanan", "macintosh", "zebede"]:
    if not bin_search(0, len(words), w):
        print(w)

##################################################################