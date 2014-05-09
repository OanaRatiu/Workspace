import io
import string
import ConfigParser

class Config(object):
    """Configuration class that gathers all other options"""
    def __init__(self, config_format, reader, parser):
        self.config_dict = {}
        self.format = config_format
        self.reader = reader
        self.parser = parser

    def get(self, key):
        try:
            return self.config_dict[key]
        except:
            return default

    def values(self):
        return self.config_dict.values()

    def items(self):
        return self.config_dict.items()

    def keys(self):
        return self.config_dict.keys()
        
    def __getitem__(self, key, default=None):
        return self.config_dict[key]
        


class MyFormat(object):
    """Format class for my own config file"""
    def __init__(self, reader):
        self.reader = reader

    def split_line(self, line):   
        """
        >>> a = MyFormat()
        >>> a.split_line("a : 1") 
        [('a', 1)]
        >>> a.split_line("b : #f,g")
        [('b', ['f', 'g'])]
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
        for line in self.reader:
            k, v = self.split_line(line)
            yield k, v




class INIFormat(object):
    def __init__(self, reader):
        self.reader = reader

    def get_all_items(self, string_all_file):
        """
        >>> sample_config = "[mysqld]\\nab = 1\\nb = c\\nd = 987\\n"
        >>> a = INIFormat()
        >>> a.get_all_items("") == {}
        True
        >>> a.get_all_items(sample_config) == {'ab': '1', 'b': 'c', 'd': '987'}
        True
        """
        iniformat_dict = {}
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        config.readfp(io.BytesIO(string_all_file))
        for section in config.sections(  ):
            for option in config.options(section):
                iniformat_dict[option] = config.get(section, option)
        return iniformat_dict

    def set_line(self, line):
        self.line = line



class FileReader(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def __iter__(self):
        with open(self.file_name) as f:
            for line in f:
                yield line





if __name__=="__main__":
    b = FileReader("my_config")
    a = MyFormat(b)
    for key, value in a:
        print str(key) + " " + str(value)