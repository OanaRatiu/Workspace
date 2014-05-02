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


def read_from_file(f):
    dictio = dd()
    words = []
    for line in f:
        words = split_into_words(line)
        for word in words:
            put_in_tree2(word, dictio)
    return dictio


def dd():
    return defaultdict(dd)

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


def parse_dictionary(dictio, word = [], single_words = []):
    """
    >>> d = dd()
    >>> d = {'m': {'a': {'t': {'e': {'s': {'times': 1}, 'times': 1}}}}}
    >>> s_w = parse_dictionary(d, [], [])
    >>> s_w == ['mates' , 'mate']
    True

    >>> s_w = parse_dictionary({'m': {'a': {'t': {'e': {'s': {'times': 1}, 'times': 1}}}}, 'z' : {'times' : 1}, 'w': {'times': 1}}, [], [])
    >>> set(s_w) == set(['mates', 'mate', 'z' , 'w'])
    True

    >>> parse_dictionary({}, [], [])
    []

    """
    for key in dictio:
        if key == 'times':
            if dictio['times'] == 1:
                cw = ''.join(word)
                single_words.append(cw)
        else:
            word.append(key)
            parse_dictionary(dictio[key], word, single_words)
            del word[-1]
    return single_words


if __name__ == '__main__':
    with open('word') as f:
        for word in parse_dictionary(read_from_file(f), [], []):
            print word

