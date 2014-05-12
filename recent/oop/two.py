import io
import string
import urllib
import ConfigParser

class Config(object):
    """Configuration class that gathers all other options"""
    def __init__(self, config_format):
        self.config_dict = {}
        self.format = config_format

    def fill_dictionary(self):
        for key, value in self.format:
            self.config_dict[key] = value

    def get(self, key, default=None):
        """
        >>> sample_config = "my_number : 12\\nmy_string : 'abc'"
        >>> b = StringReader(sample_config)
        >>> a = MyFormat(b)
        >>> c = Config(a)
        >>> c.fill_dictionary()
        >>> c.get('my_number')
        12
        >>> c.get('my_string')
        'abc'
        """
        try:
            return self.config_dict[key]
        except:
            return default

    def values(self):
        """
        >>> sample_config = "my_number : 12\\nmy_string : 'abc'"
        >>> b = StringReader(sample_config)
        >>> a = MyFormat(b)
        >>> c = Config(a)
        >>> c.fill_dictionary()
        >>> c.values()
        [12, 'abc']
        """
        return self.config_dict.values()

    def items(self):
        """
        >>> sample_config = "my_number : 12\\nmy_string : 'abc'"
        >>> b = StringReader(sample_config)
        >>> a = MyFormat(b)
        >>> c = Config(a)
        >>> c.fill_dictionary()
        >>> c.items()
        [('my_number', 12), ('my_string', 'abc')]
        """
        return self.config_dict.items()

    def keys(self):
        """
        >>> sample_config = "my_number : 12\\nmy_string : 'abc'"
        >>> b = StringReader(sample_config)
        >>> a = MyFormat(b)
        >>> c = Config(a)
        >>> c.fill_dictionary()
        >>> c.keys()
        ['my_number', 'my_string']
        """
        return self.config_dict.keys()
        
    def __getitem__(self, key, default=None):
        """
        >>> sample_config = "my_number : 12\\nmy_string : 'abc'"
        >>> b = StringReader(sample_config)
        >>> a = MyFormat(b)
        >>> c = Config(a)
        >>> c.fill_dictionary()
        >>> c['my_number']
        12
        >>> c['some_random_value']
        """
        try:
            return self.config_dict[key]
        except:
            return None
        


class MyFormat(object):
    """Format class for my own config file"""
    def __init__(self, reader):
        self.reader = reader

    def split_line(self, line):   
        """
        >>> a = MyFormat(None)
        >>> sample_config = "my_number : 12\\n"
        >>> a.split_line(sample_config)
        ('my_number', 12)
        """
        line = line.replace("\n","")
        key, value = line.split(" : ")
        if not key[0].isdigit():
            if value[0] == "'":
                return key, value.replace("'","")
            elif value[0] == "#":
                return key, value.replace("#","").split(',')
            elif value.isdigit():
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
            k, v = self.split_line(line)
            yield k, v


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
        ab 1
        b c
        d 987
        """
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        config.readfp(io.BytesIO(self.reader.read()))
        for section in config.sections(  ):
            for option in config.options(section):
                yield option, config.get(section, option)


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
    #for key, value in a:
    #    print str(key) + " " + str(value)

    c = FileReader("ini")
    d = INIFormat(c)
    #for key, value in d:
    #   print str(key) + " " + str(value)

    conf = Config(a)
    conf.fill_dictionary()
    #print conf.get('my_number')

    w = WebReader("http://hastebin.com/raw/okefajelan")
    d = INIFormat(w)
    # for key, value in d:
    #   print str(key) + " " + str(value)

    conf = Config(d)
    conf.fill_dictionary()
    print conf.get('an_int')
