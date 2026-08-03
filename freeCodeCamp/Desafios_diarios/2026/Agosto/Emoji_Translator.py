'''
Tradutor de Emojis (03/08/2026)

Dada uma sequência de emojis, retorne a frase correspondente utilizando a seguinte tabela:

Emoji	Palavra
👶	    "baby"
🐱	    "cat"
🐕	    "dog"
🐟	    "fish"
🥵	    "hot"
🧊	    "ice"
🪨       "rock"
🦈	    "shark"
🍲	    "soup"
⭐	   "star"
Retorne as palavras separadas por espaços.

Testes:
Aprovado: 1. get_emoji_phrase("🪨⭐") deve retornar "rock star".
Aprovado: 2. get_emoji_phrase("🥵🐕") deve retornar "hot dog".
Aprovado: 3. get_emoji_phrase("👶🦈") deve retornar "baby shark".
Aprovado: 4. get_emoji_phrase("⭐🐟") deve retornar "star fish".
Aprovado: 5. get_emoji_phrase("🧊🧊👶") deve retornar "ice ice baby".
Aprovado: 6. get_emoji_phrase("🐱🐟🍲") deve retornar "cat fish soup".
'''

def get_emoji_phrase(s):
    emojis = {'👶':"baby", '🐱':"cat", '🐕':"dog", '🐟':"fish", '🥵':"hot", 
            '🧊':"ice", '🪨':"rock", '🦈':"shark", '🍲':"soup", '⭐':"star"}
    texto=''
    for emoji in s:
        texto += emojis[emoji]
        texto += ' '
    n = len(texto)
    textoFinal = texto[:(n-1)]
    return textoFinal

print(get_emoji_phrase("🪨⭐"))
print(get_emoji_phrase("🥵🐕"))
print(get_emoji_phrase("👶🦈"))
print(get_emoji_phrase("⭐🐟"))
print(get_emoji_phrase("🧊🧊👶"))
print(get_emoji_phrase("🐱🐟🍲"))