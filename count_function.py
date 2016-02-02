def letter_count(a, b):
    count = 0
    for w in a:
        if w == b:
            count += 1
    return count

word = raw_input('enter your word:')
letter = raw_input('Letter:')
print word.count(letter, 0, len(word))
print word.capitalize()

