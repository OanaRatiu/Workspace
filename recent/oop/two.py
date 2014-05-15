import io
import string
import urllib
import urllib2
import ConfigParser

class Config(object):
    """Configuration class that gathers all other options"""

    def __init__(self, config_format):
        self.config_dict = {}
        for key, value in config_format:
            self.config_dict[key] = value

    def get(self, key, default=None):
        """
        >>> c = Config([['my_number', 12], ['my_string', 'abc']])
        >>> c.get('my_number')
        12
        >>> c.get('my_string')
        'abc'
        """
        return self.config_dict.get(key, default)

    def values(self):
        """
        >>> c = Config([['my_number', 12], ['my_string', 'abc']])
        >>> c.values()
        [12, 'abc']

        """
        return self.config_dict.values()

    def items(self):
        """
        >>> c = Config([['my_number', 12], ['my_string', 'abc']])
        >>> c.items()
        [('my_number', 12), ('my_string', 'abc')]

        """
        return self.config_dict.items()

    def keys(self):
        """
        >>> c = Config([['my_number', 12], ['my_string', 'abc']])
        >>> c.keys()
        ['my_number', 'my_string']

        """
        return self.config_dict.keys()
        
    def __getitem__(self, key):
        """
        >>> c = Config([['my_number', 12], ['my_string', 'abc']])
        >>> c['my_number']
        12
        >>> c['some_random_value'] # doctest:+IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        KeyError:

        """
        return self.config_dict[key]        


class MyFormat(object):
    """Format class for my own config file"""

    def __init__(self, reader):
        self.reader = reader
        self.types = {}

    def _split_line(self, line):   
        """
        >>> a = MyFormat(None)
        >>> a.add_type('url', urllib2.quote)
        >>> sample_config = "my_number : 12\\n"
        >>> a.split_line(sample_config)
        ('my_number', 12)
        >>> a.split_line ("my_type2 : $url$http://")
        ('my_type2', 'http%3A//')
        """
        line = line.strip()
        key, value = line.split(" : ", 1)
        if key[0].isdigit():
            raise ValueError('Invalid format')
        elif value[0] == '$':
            custom_name, value = value[1:].split('$', 1)
            if custom_name in self.types:         #[1] pt ca primul e ''
                return key, self.types[custom_name](value)

    def _convert_to_list(self, list_to_be):
        """
        >>> a = MyFormat(None)
        >>> a.add_type('float', float)
        >>> sample_config = "my_list : #1,'a',34,'list',$float$1.23"
        >>> a.convert_to_list(sample_config)
        ['a', 34, 'list', 1.23]
        """
        list_to_be = list_to_be.lstrip('#')
        lists = list_to_be.split(',')
        result = []
        for element in lists:
            if element[0] == "'":
                result.append(str(element.replace("'","")))
            elif element[0].isdigit():
                result.append(int(element.replace("'","")))
            elif element[0] == '$':
                values = element.split('$')
                if values[1] in self.types:         #[1] pt ca primul e ''
                    result.append(self.types[values[1]](values[2]))
        return result

    def _as_value(self, s):
        if s.startswith("'") and s.endswith("'"):
            return value[1, -1]
        elif s[0] == "#":
            return self._convert_to_list(value)
        elif s.isdigit():
            return key, int(value)

    def __iter__(self):
        """
        >>> sample_config = "my_number : 12\\nmy_string : 'abc'"
        >>> b = StringReader(sample_config)
        >>> a = MyFormat(b)
        >>> for key, value in a:
        ...     print key, value
        my_number 12
        my_string abc
        """
        for line in self.reader:
            yield self._split_line(line)

    def add_type(self, type, convert_function):
        self.types[type] = convert_function



class INIFormat(object):
    def __init__(self, reader):
        self.reader = reader

    def __iter__(self):
        """
        >>> sample_config = "[mysqld]\\nab = 1\\nb = c\\nd = 987\\n"
        >>> b = StringReader(sample_config)
        >>> a = INIFormat(b)
        >>> for key, value in a:
        ...     print key, value
        mysqld_ab 1
        mysqld_b c
        mysqld_d 987
        """
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        config.readfp(io.BytesIO(self.reader.read()))
        for section in config.sections():
            for option in config.options(section):
                yield '%s_%s' % (section, option), config.get(section, option)


class FileReader(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def __iter__(self):
        with open(self.file_name) as f:
            for line in f:
                yield line

    def read(self):
        with open(self.file_name) as f:
            return f.read()


class StringReader(object):
    def __init__(self, my_string):
        self.string = my_string

    def __iter__(self):
        """
        >>> a = StringReader("ab = 1\\nb = c\\nd = 987\\n")
        >>> for line in a:
        ...     print line
        ab = 1
        b = c
        d = 987
        """
        for line in self.string.split('\n'):
            if line.strip() != '':
                yield line

    def read(self):
        return self.string


class WebReader(object):
    def __init__(self, url):
        self.url = url
   
    def __iter__(self):
        """
        >>> w = WebReader("http://hastebin.com/raw/okefajelan")
        >>> for value in w:
        ...     print value
        [Section1]
        an_int = 15
        a_bool = true
        a_float = 3.1415
        baz = fun
        bar = Python
        foo = %(bar)s is %(baz)s!
        """
        f = urllib.urlopen(self.url)
        for line in f:
            if line.strip() != '':
                yield line.replace('\n','')

    def read(self):
        """
        >>> w = WebReader("http://hastebin.com/raw/okefajelan")
        >>> w.read()
        '[Section1]\\nan_int = 15\\na_bool = true\\na_float = 3.1415\\nbaz = fun\\nbar = Python\\nfoo = %(bar)s is %(baz)s!'
        """
        return urllib.urlopen(self.url).read()


if __name__=="__main__":
    b = FileReader("my_config")
    a = MyFormat(b)
    a.add_type('float', float)
    a.add_type('url', urllib2.quote)
    for key, value in a:
        print str(key) + " " + repr(value)

    c = FileReader("ini")
    d = INIFormat(c)
    # for key, value in d:
    #    print str(key) + " " + str(value)

    conf = Config(a)
    conf.fill_dictionary()
    #print conf.get('my_number')

    w = WebReader("http://hastebin.com/raw/okefajelan")
    d = INIFormat(w)
    # for key, value in d:
    #   print str(key) + " " + str(value)

    # conf = Config(d)
    # conf.fill_dictionary()
    # print conf.get('an_int')
