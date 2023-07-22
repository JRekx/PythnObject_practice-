"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder('simple.txt')
    3 word read

    >>> wf.random() in ['cat','dog','porcupine']
    true

    >>> wf.random() in ['cat','dog','porcupine']
    True

    >>> wf.random() in ['cat','dog','porcupine']
    True
    """

    def __init__(self,path):
        """Read dictonary and reports # items read."""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print (f"{len(self.word)} words read")

    def parse(self, dict_file):
        """Parse dict_file --> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word.""" 

        return random.choice(self.words) 

class SepecialWordFinder(WordFinder):
    """Specialezed WordFinder that exculdes blank lines/comments.
    
    >>> swf = SpecialWordFinder('complex.txt')
    3 words read

    >>> swf.random() in ['pear','carrot','kale']
    True

    >>> swf.random() in ['pear','carrot','kale']
    True

    >>> swf.random() in ['pear','carrot','kale']
    True
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of wrords, skipping blanks/comments"""
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
    
    
    
    
   
