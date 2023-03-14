import os.path as osp

TREE_FILE = osp.join(osp.dirname(__file__), "9k.tree")
NAMES_FILE = osp.join(osp.dirname(__file__), "9k.names")


class Wordnet9000:
    def __init__(self):
        with open(NAMES_FILE) as f:
            self.names = f.read().splitlines()
        with open(TREE_FILE) as f:
            raw_tree = f.read().splitlines()

        self.raw_tree = {}
        for idx, line in enumerate(raw_tree):
            raw_child, raw_parent = line.split()
            parent_idx = int(raw_parent)
            if parent_idx == -1:
                parent = ""
            else:
                parent = raw_tree[parent_idx].split()[0]
            child = raw_tree[idx].split()[0]
            self.raw_tree[child] = parent

        self.raw2name = {
            raw_line.split()[0]: name for raw_line, name in zip(raw_tree, self.names)
        }
        self.name2raw = {v: k for k, v in self.raw2name.items()}

    def is_ancestor(self, word1, word2):
        """Returns:
        0 if word1 is an ancestor of word2
        1 if word2 is an ancestor of word1
        -1 if neither word1 nor word2 is an ancestor of the other"""
        raw_word1 = self.name2raw[word1]
        raw_word2 = self.name2raw[word2]
        if self._is_ancestor(raw_word1, raw_word2):
            return 0
        elif self._is_ancestor(raw_word2, raw_word1):
            return 1
        return -1

    def _is_ancestor(self, raw_word1, raw_word2):
        """Returns True if word1 is an ancestor of word2."""
        while raw_word2 != "":
            if raw_word1 == raw_word2:
                return True
            raw_word2 = self.raw_tree[raw_word2]
