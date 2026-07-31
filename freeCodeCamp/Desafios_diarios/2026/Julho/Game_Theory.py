'''
Game Theory (23/07/2026)

Given two equal length strings representing two players' strategies for a game, return the scores as an array [player1, player2].

The given strings will only contain one of two letters: "C" (cooperate) or "D" (defect).
Each character represents one round, scored as follows:
If both players cooperate, each scores 3.
If both players defect, each scores 1.
If one player defects and the other cooperates, the defector scores 5 and the cooperator scores 0.

Testes:
Aprovado:1. play_game("CCCC", "CCCC") should return [12, 12].
Aprovado:2. play_game("DDDD", "DDDD") should return [4, 4].
Aprovado:3. play_game("CCDD", "CDDD") should return [5, 10].
Aprovado:4. play_game("CCCDCDCCCDDC", "CCDDCDCDDCCD") should return [24, 34].
Aprovado:5. play_game("DDCCDDDDCDDCDDDCDD", "CCDCCCDCCCDCCCCDCC") should return [66, 21].
'''

def play_game(p1, p2):
    comprimento = len(p1)
    pointsP1=0
    pointsP2=0

    for i in range(comprimento):
        if p1[i]=='C' and p2[i]=='C':
            pointsP1+=3
            pointsP2+=3
        if p1[i]=='D' and p2[i]=='D':
            pointsP1+=1
            pointsP2+=1
        if p1[i]=='D' and p2[i]=='C':
            pointsP1+=5
        if p2[i]=='D' and p1[i]=='C':
            pointsP2+=5
    
    return [pointsP1, pointsP2]

print(play_game("CCCC", "CCCC"))
print(play_game("DDDD", "DDDD"))
print(play_game("CCDD", "CDDD"))
print(play_game("CCCDCDCCCDDC", "CCDDCDCDDCCD"))
print(play_game("DDCCDDDDCDDCDDDCDD", "CCDCCCDCCCDCCCCDCC"))
