#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Core script containing the main function of the entire package

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

from pathlib import Path
import yaml
import cypher.cyphers as cyphers
from colorama import just_fix_windows_console
# make ANSI colours work on Windows without installing anything else
# (does nothing on other OSs)
just_fix_windows_console()


def main(plain_file, out_file, cypher=None, options={}, verbose=True):
    
    plain_file = Path(plain_file)
    if verbose:
        print(f'Reading plain text file {plain_file.resolve()}...')
    # read a single string with '\n' in it
    with open(plain_file, 'r') as file:
        plain_text = file.read()
    
    match cypher.lower():
        case 'caesar':
            if verbose:
                print('Cyphering method selected: Caesaer')
            cypher_text, info = cyphers.Caesar(plain_text, key=options['key'], verbose=verbose)
        case 'rot13':
            if verbose:
                print('Cyphering method selected: ROT13 '
                      "(equivalent to Caesar's with key = 13")
            # special case of Caesar with key = 13, so that calling the
            # cyphering command on the cyphered text will return the plain
            # text (because 13+13 = 26, and thus A will be coded to A -> N -> A)
            cypher_text, info = cyphers.Caesar(plain_text, key=13, verbose=verbose)
    
    out_file = Path(out_file)
    if verbose:
        print(f'Writing cyphered text to {out_file.resolve()}...')
    # read a single string with '\n' in it
    with open(out_file, 'w') as file:
        file.write(cypher_text)
                


if __name__ == '__main__':
    plain_file = '../examples/PridePrejudice.txt'
    out_file = '../examples/out.txt'
    main(plain_file, out_file)