import numpy as np
import pandas as pd

from pandas import Series, DataFrame

from difflib import SequenceMatcher, get_close_matches

# SequenceMatcher 是一个比较两个字符串并根据它们的相似性返回数据的函数。通过使用 ratio()，我们将能够根据比率/百分比来量化这种相似性。
phrase1 = "Tan loves Trees."
phrase2 = "Tan loves to mount Trees."
similarity = SequenceMatcher(None, phrase1, phrase2)
print(similarity.ratio())

# get_close_matches该函数返回与作为参数传入的字符串最接近的匹配项。
# get_close_matches(word, possibilities, result_limit, min_similarity)
# word 是函数将要查看的目标单词。
# possibilities 是一个数组，其中包含函数将要查找的匹配项并找到最接近的匹配项。
# result_limit 是返回结果数量的限制（可选）。
# min_similarity 是两个单词需要具有的最小相似度才能被函数视为返回值（可选）。
word = 'Tandrew'
possibilities = ['Andrew', 'Teresa', 'Kairu', 'Janderson', 'Drew']

print(get_close_matches(word, possibilities))
