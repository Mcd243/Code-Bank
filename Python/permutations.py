import hashlib
from typing import Generator, List
# pylint: disable-msg=C0103


def all_perms_yield(A: List[str], B: List[str], C: List[str]) -> Generator:
    """Calculate all possible permutations using yield.
       Yields one tuple at a time. """
    for a in A:
        for b in B:
            for c in C:
                yield a, b, c

for triple in all_perms_yield(["big", "small"],
                              ["red", "green", "blue"],
                              ["circle", "triangle", "square"]):
    # triple is a tuple, e.g. ('small', 'blue', 'triangle')
    phrase = " ".join(triple)
    phrase_hash = hashlib.md5(phrase.encode("utf-8")).hexdigest()
    if phrase_hash == "4b23449b89f1322cbcdc8620d1672f28":
        print(phrase)
        break
