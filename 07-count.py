sent="What a match"
counter = {}

for c in sent:
    if c.isalpha():
        c = c.lower()
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    
for l, f in counter.items():
    print(f"Letter: {l}, Frequency: {f}")
        
