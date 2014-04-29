import re

class Word(object):
  def __init__(self, myw):
    self.uniq = 0
    self.myw = myw


def modifyState(word):
  """
  >>> a = modifyState(Word("a"))
  >>> a.uniq == 1
  True
  """
  word.uniq = 1
  return word


def compare_words(word1, word2):
  """
  >>> compare_words(Word('a'), Word('b'))
  -1
  """
  return cmp(word1.myw, word2.myw)


def sorting(myl, modify=modifyState, compare=compare_words):
  """
  >>> sorting(["b", "a", "d", "c"], str, cmp)
  ['a', 'b', 'c', 'd']

  >>> sorting([], None, None)
  []

  >>> sorting(['a','b','a','c'], str, cmp)
  ['a', 'b', 'c']

  """
  if len(myl) > 1:
    lm = len(myl)
    middle = len(myl)//2
    left = myl[:middle]
    right = myl[middle:]

    sorting(left, modify, compare)
    sorting(right, modify, compare)

    left_index = 0
    right_index = 0
    index = -1

    while left_index < len(left) and right_index < len(right):
      if index > 0:
        if compare( left[left_index], myl[index]) == 0:
          left_index = left_index + 1 
          myl[index] = modify(myl[index])
          continue
        if compare( right[right_index], myl[index]) == 0:
          right_index = right_index + 1
          myl[index] = modify(myl[index])
          continue
      if compare( left[left_index], right[right_index]) == 0: 
        index = index + 1
        myl[index] = left[left_index]
        myl[index] = modify(myl[index])
        right_index = right_index + 1
        left_index = left_index + 1
      else:
        if compare( left[left_index], right[right_index]) == -1:
          index = index + 1 
          myl[index] = left[left_index]
          left_index = left_index + 1       
        elif compare( left[left_index], right[right_index]) == 1:   
          index = index + 1
          myl[index] = right[right_index]
          right_index = right_index + 1
          


    while left_index < len(left):
      if compare( left[left_index], myl[index]) == 0:
        left_index = left_index + i
        myl[index] = modify(myl[index])
      else:
        index = index + 1
        myl[index] = left[left_index]
        left_index = left_index + 1
        

    while right_index < len(right):
      if compare( right[right_index], myl[index]) == 0:
        right_index = right_index + 1
        myl[index] = modify(myl[index])
      else:
        index = index + 1
        myl[index] = right[right_index]
        right_index = right_index + 1

    if index < lm:
      for p in range(lm-index-1):
        myl.pop()

  return myl


# l = []
# w1 = Word("aa")
# w2 = Word("fgh")
# w3 = Word("ca")
# w4 = Word("aa")
# w5 = Word("chf")
# w6 = Word("fgh")
# w7 = Word("aa")
# w8 = Word("b")
# w9 = Word("b")
# l.append(w1)
# l.append(w2)
# l.append(w3)
# l.append(w4)
# l.append(w5)
# l.append(w6)
# l.append(w7)
# l.append(w8)
# l.append(w9)
# sorting(l)
# for word in l:
#   print word.myw + " " + str(word.uniq)



def split_into_words(lines):
  """
  >>> split_into_words("a,b c!")
  ['a', 'b', 'c']

  >>split_into_words("")
  []
  """
  return re.findall(r"[\w']+", lines)






def checkf():
  with open('word','r') as f:
    delimiters = ['\n',' ', ',', '.', '?', '!', ':', '"']
    #lines = f.readlines()
    lines = []
    lines.append("am fost, dfsadfsa da-sda!! dsaf, das.!!\n dsadfas fasfda")
    lines.append("dasdasfsa gfdf")
    for delimiter in delimiters:
        new_words = []
        for word in lines:
            new_words += word.split(delimiter)
        lines = new_words
    print new_words

#checkf()

