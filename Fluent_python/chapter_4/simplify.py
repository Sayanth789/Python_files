import unicodedata
import string 

def shave_marks(txt):
    """ Remove all diacritic marks """
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)

def shave_marks_latin(txt):
    """Remove all diacritic marks from Latin base characters"""
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False 
    preserve = []

    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue # ignore diacritic on Latin base char 
        preserve.append(c)

        # If it isn't combining char, it's a new base char
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters

    shaved = ''.join(preserve)

    return unicodedata.normalize('NFC', shaved)

single_map = str.maketrans("""‚ƒ„ˆ‹‘’“”•–—˜›""",  # <1>
                           """'f"^<''""---~>""")


multi_map = str.maketrans({
    '€': 'EUR',
    '…': '...',
    'Æ': 'AE',
    'æ': 'ae',
    'Œ': 'OE',
    'œ': 'oe',
    '™': '(TM)',
    '‰': '<per mille>',
    '†': '**',
    '‡': '***',
})

multi_map.update(single_map)

def dewinize(txt):
    """ 
    Replace Win1252 symbols with ASCII chars or sequences
    """

def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt)) 
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks) 

  
