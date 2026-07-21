'''
Word Blender (21/07/2026)

Given two words, return a new word by combining the first half of the first word with the second half of the second word.

For odd-length words, the first half is the shorter half.

Testes:
Aprovado:1. blend_words("turtle", "toucan") should return "turcan".
Aprovado:2. blend_words("chipmunk", "flamingo") should return "chipingo".
Aprovado:3. blend_words("falcon", "pelican") should return "falican".
Aprovado:4. blend_words("hyena", "iguana") should return "hyana".
Aprovado:5. blend_words("scorpion", "gorilla") should return "scorilla".
Aprovado:6. blend_words("platypus", "wolverine") should return "platerine".
'''

import math

def blend_words(word1, word2):
    tam_1a_metade = math.floor(len(word1)/2)
    tam_2a_metade = math.floor(len(word2)/2)
    
    primeira_metade = word1[:tam_1a_metade]
    segunda_metade = word2[tam_2a_metade:]

    final_word = primeira_metade + segunda_metade
    
    return final_word

print(blend_words("turtle", "toucan"))
print(blend_words("chipmunk", "flamingo"))
print(blend_words("falcon", "pelican"))
print(blend_words("hyena", "iguana"))
print(blend_words("scorpion", "gorilla"))
print(blend_words("platypus", "wolverine"))
