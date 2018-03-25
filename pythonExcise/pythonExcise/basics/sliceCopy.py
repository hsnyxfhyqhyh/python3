words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# words[:] if a slice copy of the original list, so the loopthing logic 
for w in words[:]:
    if len(w) > 6:
        words.insert(0,w)

print(words)
    