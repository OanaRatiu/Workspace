import re

def split_into_words(lines):
  """
  >>> split_into_words("a,b c!")
  ['a', 'b', 'c']

  >>split_into_words("")
  []
  """
  return re.findall(r"[\w']+", lines)


def read_from_file(f):
  # """
  # >>> read_from_file(['a b c', 'a =b c!\\n'])
  # ['a', 'b', 'c']
  # """
  words = []
  for line in f:
    words = split_into_words(line)
    for word in words:
      put_in_tree(word)

  
def put_in_tree(word, dictio):
  """
  >>> put_in_tree('mama',{'m':{0}})
  {'m':{'a':{'m':{'a':{0}}}}}
  """
  cd = dictio
  for i in range(len(word)):
    if word[i+1] in cd[word[i]]:
      cd = cd[word[i]]
      i+=1
    else:
      cd[word[i]] = {word[i+1]:{0}}




