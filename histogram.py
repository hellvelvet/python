def histogram(word):
    result = list(word)
    unique_characters = []
    
    for character in result:
        if character not in unique_characters:
            unique_characters.append(character)
    
    for character in unique_characters:
        count = 0  # Initialize count to zero for each unique character
        for c in result:
            if c == character:
                count += 1
        print(character, count * "*")

word = "ekmek"
histogram(word)
