from Scanner import Tokenizer
import sys

#This creates a single instance of the tokenizer that will be used for all of parsing
class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = Tokenizer(sys.argv[1])
        return cls.instance
        
    
    