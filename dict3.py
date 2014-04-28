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


 #start with dicitonary that has every letter as key in it 
def put_in_tree(word, dictio):
  """
  >>> put_in_tree('mate',{})
  {'m': {'a': {'t': {'e': {'times': 1}}}}}

  >> put_in_tree('mama',{})
  {'m': {'a': {'m': {'a': {'times': 1}}}}}

  >> put_in_tree('a',{})
  {'a': {'times': 1}}

  >>> put_in_tree('mates', {'m': {'a': {'t': {'e': {'times': 1}}}}})
  {'m': {'a': {'t': {'e': {'times': 1}, {'s': {'times': 1}}}}}}

  """
  cd = dictio
  for i in range(len(word)):
    try:
      if word[i+1] in cd[word[i]].keys():
        cd = cd[word[i]]
    except:
      try:
        if 'times' not in cd[word[i]].keys():
          cd[word[i]] = {}
      except:
        cd[word[i]].update({word[i+1] : {}})
        i = i+1
      cd = cd[word[i]]

  if cd == {}:
    cd['times'] = 1
  else:
    cd['times'] += 1  
  return dictio

put_in_tree('mate',{})