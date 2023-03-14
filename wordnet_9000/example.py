import argparse
import random

from wordnet_9000 import Wordnet9000

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    # Add an argument that takes 0, 1, or 2 strings (words)
    parser.add_argument("words", type=str, nargs="*")
    args = parser.parse_args()

    w = Wordnet9000()

    if len(args.words) < 2:
        # Just print all parents of a word, select a random word if none is given
        if len(args.words) == 0:
            word = random.choice(w.names)
        else:
            word = args.words[0]
            assert word in w.names, f"{word} is not in Wordnet9000!"
        print(f"Word: {word}")
        print("Parents:")
        word = w.name2raw[word]
        while word != "":
            word = w.raw_tree[word]
            if word != "":
                print(w.raw2name[word])
    elif len(args.words) == 2:
        # Check if the two words are ancestors of each other
        word1, word2 = args.words
        assert word1 in w.names, f"{word1} is not in Wordnet9000!"
        assert word2 in w.names, f"{word2} is not in Wordnet9000!"
        ind = w.is_ancestor(word1, word2)
        if ind == 0:
            print(f"{word1} is an ancestor of {word2}")
        elif ind == 1:
            print(f"{word2} is an ancestor of {word1}")
        else:
            print(f"{word1} and {word2} are not ancestors of the other")
    else:
        raise ValueError("Too many arguments!")
