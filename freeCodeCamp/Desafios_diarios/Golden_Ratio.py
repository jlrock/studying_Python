'''
Golden Ratio (20/07/2026)

Given two numbers, determine if their ratio approximates the golden ratio.

Use a golden ratio of 1.618
Allow a tolerance of 0.01

Testes:
Aprovado:1. is_golden_ratio(21, 34) should return True.
Aprovado:2. is_golden_ratio(15, 20) should return False.
Aprovado:3. is_golden_ratio(8, 13) should return True.
Aprovado:4. is_golden_ratio(10, 16) should return False.
Aprovado:5. is_golden_ratio(1618, 1000) should return True.
Aprovado:6. is_golden_ratio(88, 55) should return False.
'''

def is_golden_ratio(a, b):
    if((abs((a/b) - 1.618) <= 0.01) or (abs((b/a) - 1.618) <= 0.01)):
        return True
    return False

print('\n', is_golden_ratio(21, 34), '\n', is_golden_ratio(15, 20), '\n', is_golden_ratio(8, 13), '\n', 
    is_golden_ratio(10, 16), '\n', is_golden_ratio(1618, 1000), '\n', is_golden_ratio(88, 55), '\n')