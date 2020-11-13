from collections import defaultdict 

strings = ['сон', 'нос', 'сорт', 'трос', 'торт', 'рост']
def group_anagrams(strings): 
    m = defaultdict(list) 
    for s in strings:
        m[tuple(sorted(s))].append(s) 
    return list(m.values())

print(group_anagrams(strings))