with open('result.log', 'r') as f:
    text = f.read()

tests = [t.split('\n') for t in text.split('\n-\n')]
A_wins = [t for t in tests if t[0].startswith('Player: A')]
B_wins = [t for t in tests if t[0].startswith('Player: B')]
C_wins = [t for t in tests if t[0].startswith('Player: C')]
D_wins = [t for t in tests if t[0].startswith('Player: D')]
E_wins = [t for t in tests if t[0].startswith('Player: E')]

print('Me: {}, player B: {}, player C: {}, player D: {}, player E: {}'.format(
    len(A_wins), len(B_wins), len(C_wins), len(D_wins), len(E_wins)))
