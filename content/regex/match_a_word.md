Title: Match A Word
Slug: match_a_word
Summary: Match A Word
Date: 2016-05-01 12:00
Category: Regex
Tags: Basics
Authors: Samira Ouaaz



Based on: [Regular Expressions Cookbook](http://shop.oreilly.com/product/0636920023630.do)

## Preliminaries


```python
# Load regex package
import re
```

## Create some text


```python
# Create a variable containing a text string
text = 'The quick brown fox jumped over the lazy brown bear.'
```

## Apply regex


```python
# Find any word of three letters
re.findall(r'\b...\b', text)
```




    ['The', 'fox', 'the']


