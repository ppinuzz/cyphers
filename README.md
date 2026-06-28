# List of common cyphers #

## Available cyphers ##
- Caesar
- ROT13, a specific case of Caesar with a length 13 key

Only the international alphabet `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`
is cyphered, all the other symbols will stay the same. In ASCII encoding, this is
```
ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz
^                        ^ ^                        ^
65                      90 97                       122
```
Don't use accents like `è`, use `e'` instead

### Caesaer ###
The $n$-th letter is substituted with the $n+k$-th, being $k$ the key. It uses
modular arithmetics, therefore Y gets cyphered as B if $k = 3$ (i.e. Y + 3 -> Z)


### ROT13 ###
Caesaer's cypher, but with $k = 13$. Since there are 26 letters in the international 
alphabet, calling ROT13 on the cyphered text obtained by ROT13 will decypher it:
it's a total shift of 26 places, i.e. an identity shift where A + 26 -> A