def single_root_words(root_word, *other_words):
    same_word = []
    for i in other_words:
        if len(root_word) < len(i):
            if root_word in i:
                same_word.append(i)
        else:
            if i.lower() in root_word.lower():
                same_word.append(i)
    return same_word


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

