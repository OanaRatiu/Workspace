import re
from collections import defaultdict

def split_into_words(lines):
  """
  >>> split_into_words("a,b c!")
  ['a', 'b', 'c']

  >>split_into_words("")
  []
  """
  return re.findall(r"[\w']+", lines)


def dd():
  return defaultdict(dd)


def read_from_file(f, dictio=dd()):
  # """
  # >>> read_from_file(['a b c', 'a =b c!\\n'])
  # ['a', 'b', 'c']
  # """
  words = []
  for line in f:
    words = split_into_words(line)
    for word in words:
      put_in_tree2(word, dictio)


def put_in_tree2(word, dictio = dd()):
  """
  >>> put_in_tree2('mate') == {'m': {'a': {'t': {'e': {'times': 1}}}}}
  True

  >>> d = dd()
  >>> e = put_in_tree2('mate', d)
  >>> put_in_tree2('mates', e) == {'m': {'a': {'t': {'e': {'s': {'times': 1}, 'times': 1}}}}}
  True

  """
  cd = dictio
  for letter in word:
    cd=cd[letter]
  try :
    cd['times'] = int(cd['times']) + 1
  except TypeError:
    cd['times'] = 1
  return dictio


def trav_tree(dictio, path=[]):
  """
  sorted(trav_tree({'m': {'a': {'t': {'e': {'s': {'times': 1}, 'times': 1}}}}}))
  ['mate', 'mates']

  >>> sorted(trav_tree({'m': {'a': {'t': {'e': {'s': {'times': 1}, 'times': 1}}}}, 'z' : {'times' : 2}}))
  ['mate', 'mates']

  """
  for key in dictio:
    if key == 'times':
      if dictio[key] == 1:
        word = ''.join(path)
        yield word
    else:
      path.append(key)
      for word in trav_tree(dictio[key], path):
        yield word
      del path[-1]


if __name__ == '__main__':
  with open('words') as f:
    dictio = dd()
    read_from_file(f, dictio)
    words = trav_tree(dictio)
    for w in words:
      print w