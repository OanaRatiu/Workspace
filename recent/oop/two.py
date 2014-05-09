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
        return self.config_dict[key]

    def values(self):
        return self.config_dict.values()

    def items(self):
        return self.config_dict.items()

    def keys(self):
        return self.config_dict.keys()
        
    def __getitem__(self, key, default=None):
        try:
            return self.config_dict[key]
        except:
            return default


class MyFormat(object):
    """Format class for my own config file"""
    def __init__(self):
        pass



    def get_all_items(self, string_all_file):
        """
        >>> a = MyFormat()
        >>> a.get_all_items("") == {}
        True
        >>> a.get_all_items("a : 1\\nb : 'c'\\nd : #f,g") == {'a': 1, 'b': 'c', 'd': ['f', 'g']}
        True
        """
        my_format_dict = {}
        if string_all_file is not "":
            lines = string_all_file.split("\n")
            for line in lines:
                key, value = line.split(" : ")
                if not key[0].isdigit():
                    if value[0] == "'":
                        my_format_dict[key] = value.replace("'","")
                    elif value[0] == "#":
                        my_format_dict[key] = value.replace("#","").split(',')
                    elif value.isdigit():
                        my_format_dict[key] = int(value)
        return my_format_dict



class INIFormat(object):
    def __init__(self):
        pass

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


class DiskReader(object):
    def get_all_file(self, file_name):
        with open(file_name) as f:
            return f.read()





if __name__=="__main__":
    r = DiskReader()
    r.get_all_file("ini")
    a = INIFormat()
    #sample_config = "[mysqld]\nuser = mysql\npid-file = /var/run/mysqld/mysqld.pid\na = skip-external-locking\n"
    dict = a.get_all_items(sample_config)
    for key, value in dict.items():
        print str(key) + "   " + str(value)

    # a = MyFormat()
    # dict = a.get_all_items("a : 1\nb : 'c'\nd : #f,g")
    # for key, value in dict.items():
    #     print str(key) + "   " + str(value)