[![PyPI version](https://img.shields.io/pypi/v/TagStats.svg)](https://pypi.python.org/pypi/TagStats/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/TagStats.svg)](https://pypi.python.org/pypi/TagStats/)
[![PyPI license](https://img.shields.io/pypi/l/TagStats.svg)](https://pypi.python.org/pypi/TagStats/)

A concise yet efficient implementation for computing the statistics of each tag's set of key phrases over input lines in Python 3.
One of the major applications is for [sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis), where each tag is a sentiment with the respective key phrases describing the sentiment.

# How it Works

A [trie](https://en.wikipedia.org/wiki/Trie) structure is constructed to index all the key phrases. Then each line is matched towards the index to compute the respective statistics.
The time complexity is $O(m^2 \cdot n)$, where $m$ is the maximum number of words in each line and $n$ is the number of lines.

# Installation

This package is available on PyPI. Just use `pip3 install -U TagStats` to install it.

# Usage

You can simply call `compute(content, tagDict)`, where `content` is a list of lines and `tagDict` is a dictionary with each tag name as key and the respective set of key phrases as value.

``` python
from tagstats import compute

print(compute(
    [
        "a b c",
        "b c",
        "a c e"
    ],
    {
        "+": ["a b", "a c"],
        "-": ["b c"]
    }
))
```

The output is a dictionary with each tag name as key and the respective totaled frequencies for lines as value.

``` python
{'+': [1, 0, 1], '-': [1, 1, 0]}
```

You can change the default tokenizer, by specifying a compiled regex as separator to `tagstats.tagstats.tokenizer`. You can disable the tokenizer to allow matching over word boundaries, by specifying `None`.

You can pre-build the index by calling `index(tagDict)`, and later reuse it more than once as an optional parameter of `compute(content, tagDict, index)`. 

# Tip

I strongly encourage using PyPy instead of CPython to run the script for best performance.
