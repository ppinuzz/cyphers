#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cyphering routines

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

from pathlib import Path
import yaml


N_CHARS_ALPHABET = 26

def Caesar(text, key, verbose=True, write_key=True, key_file='key.yaml'):
    
    if verbose:
        print("CAESAR'S CYPHER")
        print(f'Key: {key}')
    
    cyphered = ''
    N_cyphered_chars = 0
    for letter in text:
        # do not cypher numbers and punctuation
        if letter.isalpha():
            # convert to ASCII code
            code = ord(letter)
            # remove offset, so that code starts from 0
            first_char = ord('A' if letter.isupper() else 'a')
            code -= first_char
            code += key
            # "overflowing": e.g. 25 + 3 = 28 -> 2 (modular arithmetic)
            code = first_char + (code % N_CHARS_ALPHABET)
            letter = chr(code)
            N_cyphered_chars += 1
        cyphered += letter
    
    info = {'cyphered_chars': N_cyphered_chars}
    
    if write_key:
        key_data = {'key': key,
                    'cypher': 'Caesar'
                    }
        key_file = Path(key_file)
        if verbose:
            print(f'Writing key to {key_file.resolve()}...')
        with open(key_file, 'w') as file:
            yaml.safe_dump(key_data, file)
    
    if verbose:
        print(f'Cyphered {N_cyphered_chars} characters')
        print(f'Left unchanged {len(text)-N_cyphered_chars} characters')
    
    return cyphered, info



if __name__ == '__main__':
    text = ('It was a bright cold day in April, and the clocks were striking '
            'thirteen. Winston Smith, his chin nuzzled into his breast in an '
            'effort to escape the vile wind, slipped quickly through the glass '
            'doors of Victory Mansions, though not quickly enough to prevent a '
            'swirl of gritty dust from entering along with him.')
    
    # Pa dhz h iypnoa jvsk khf pu Hwyps, huk aol jsvjrz dlyl zayprpun aopyallu. Dpuzavu Ztpao, opz jopu ubggslk puav opz iylhza pu hu lmmvya av lzjhwl aol cpsl dpuk, zspwwlk xbpjrsf aoyvbno aol nshzz kvvyz vm Cpjavyf Thuzpvuz, aovbno uva xbpjrsf luvbno av wylclua h zdpys vm nypaaf kbza myvt lualypun hsvun dpao opt.
    
    cyphered, info = Caesar(text, 7)