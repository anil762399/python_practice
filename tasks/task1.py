'''_word = "   this  is    python   class day 3"
_word=_word.lstrip()
_word=_word.capitalize() 
_word=_word.replace("    ","-")
_word=_word.replace("   ","-")
_word=_word.replace("  ","-")
_word=_word.replace(" ","-")
_word=_word.replace("y","Y")   casefold
print(_word) ''' 


_word = "   this  is    python   class day 3"
#_word=_word.strip()
_word=_word.split()
print(_word)
'''
_word='-'.join(_word)
_word=_word.capitalize()
_word=_word.replace("y","Y")
print(_word) '''