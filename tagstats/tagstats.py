#! /usr/bin/env python3

from collections import namedtuple, Counter
import re

Node = namedtuple("Node", ["children", "tags"])
tokenizer = re.compile(r"^[^\w@#/+-]+|\W*\s+[^\w@#/+-]*", re.U)

def index(tagDict):
    root = Node({}, set())

    for tag, phrases in tagDict.items():
        for phrase in phrases:
            node = root
            for word in [w for w in (tokenizer.split(phrase) if tokenizer else phrase) if len(w) > 0]:
                node = node.children.setdefault(word, Node({}, set()))
            node.tags.add(tag)

    return root


def __search(root, line):
    matched = Counter()

    for i in range(len(line)):
        node = root

        for word in line[i:]:
            if word not in node.children:
                break

            node = node.children[word]

            for tag in node.tags:
                matched[tag] += 1

    return matched


def compute(content, tagDict, root=None):
    if root is None:
        root = index(tagDict)

    counter = {
        tag: [0] * len(content)
        for tag in tagDict
    }

    for i, line in enumerate(content):
        for tag, count in __search(
                root,
                [w for w in (tokenizer.split(line) if tokenizer else line) if len(w) > 0]
            ).items():
            counter[tag][i] += count

    return counter
