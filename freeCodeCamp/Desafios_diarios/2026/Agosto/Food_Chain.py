'''
Food Chain (02/08/2026)

Given an array of [predator, prey] pairs, return the food chain from the apex predator down to the bottom.

The apex predator is the animal that is never prey to another animal.
Return the chain as an array of strings.

Testes:
1. get_food_chain([["cat", "mouse"]]) should return ["cat", "mouse"].
2. get_food_chain([["wolf", "deer"], ["deer", "grass"]]) should return ["wolf", "deer", "grass"].
3. get_food_chain([["hawk", "snake"], ["snake", "frog"], ["frog", "fly"]]) should return ["hawk", "snake", "frog", "fly"].
4. get_food_chain([["rabbit", "grass"], ["fox", "rabbit"], ["eagle", "fox"]]) should return ["eagle", "fox", "rabbit", "grass"].
5. get_food_chain([["seal", "salmon"], ["herring", "shrimp"], ["orca", "seal"], ["shrimp", "plankton"], ["salmon", "herring"]]) 
should return ["orca", "seal", "salmon", "herring", "shrimp", "plankton"].
'''

def get_food_chain(pairs):
    final_pairs = []
    while len(pairs) > 0:
        for par1 in pairs:
            count = 0
            for par2 in pairs:
                if par1[0] != par2[1]:
                    count += 1
            if count == len(pairs):
                final_pairs.extend(par1)
                pairs.remove(par1)
                break
    i = 0
    while i < len(final_pairs) - 1:
        if final_pairs[i] == final_pairs[i + 1]:
            final_pairs.pop(i)
        else:
            i += 1
    return final_pairs

print(get_food_chain([["cat", "mouse"]]))
print(get_food_chain([["wolf", "deer"], ["deer", "grass"]]))
print(get_food_chain([["hawk", "snake"], ["snake", "frog"], ["frog", "fly"]]))
print(get_food_chain([["rabbit", "grass"], ["fox", "rabbit"], ["eagle", "fox"]]))
print(get_food_chain([["seal", "salmon"], ["herring", "shrimp"], ["orca", "seal"], 
                    ["shrimp", "plankton"], ["salmon", "herring"]]))