'''
Morse Code (31/07/2026)

Given a Morse code string, return the decoded message using the following table:

Code	Letter	Code	Letter
.-	    A	    -.	    N
-...	B	    ---	    O
-.-.	C	    .--.	P
-..	    D	    --.-	Q
.	    E	    .-.	    R
..-.	F	    ...	    S
--.	    G	    -	    T
....	H	    ..-	    U
..	    I	    ...-	V
.---	J	    .--	    W
-.-	    K	    -..-	X
.-..	L	    -.--	Y
--	    M	    --..	Z

Letters are separated by a single space
Words are separated by three spaces

Testes:
Aprovado:1. decode_morse("--..") should return "Z".
Aprovado:2. decode_morse("... --- ...") should return "SOS".
Aprovado:3. decode_morse("..-. .-. . . -.-. --- -.. . -.-. .- -- .--.") should return "FREECODECAMP".
Aprovado:4. decode_morse(".... . .-.. .-.. ---   .-- --- .-. .-.. -..") should return "HELLO WORLD".
Aprovado:5. decode_morse("- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   
.--- ..- -- .--. . -..   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --.") should return 
"THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG".
'''

def decode_morse(code):
    tabela_morse = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', 
                    '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', 
                    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', 
                    '-..-': 'X', '-.--': 'Y', '--..': 'Z'}

    vetor_texto = []
    palavras = code.split('   ')
    for palavra in palavras:
        letras = palavra.split()
        vetor_texto.extend(letras)
        vetor_texto.append(' ')
    vetor_texto.pop(-1)

    texto = ''
    for letra in vetor_texto:
        if letra in tabela_morse:
            texto += tabela_morse[letra]
        else:
            texto += letra
    return texto

print(decode_morse("--.."))
print(decode_morse("... --- ..."))
print(decode_morse("..-. .-. . . -.-. --- -.. . -.-. .- -- .--."))
print(decode_morse(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."))
print(decode_morse("- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. . -..   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --."))
