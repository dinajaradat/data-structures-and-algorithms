def most_common_word(string):
    string = string.lower().replace('?', '').replace('.', '').replace(',', '').replace('!', '')

    word_count = {}
    
    for word in string.split():
        if word not in word_count:
            word_count[word] = 1
    
        else:
            word_count[word] += 1
    # print(word_count)
    
    max_count = 0
    most_common = ''
    
    for word, count in word_count.items():
        if count > max_count:
            max_count = count
            most_common = word
    
    return most_common
    


string1 = "In a galaxy far far away"
string2 = "Taco cat ate a taco"
string3 = "No. Try not. Do or do not. There is no try."


print(most_common_word(string1)) 
print(most_common_word(string2))  
print(most_common_word(string3)) 
