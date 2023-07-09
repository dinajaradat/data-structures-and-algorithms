def left_join(hashmap1 , hashmap2):
    output = []

    if len(hashmap1) == 0 :
        return output

    for key in hashmap1:
        if key in hashmap2:
            antonym = hashmap2[key]
        else:
            antonym = None

        output.append([key, hashmap1[key] , antonym]) 
    
    return output

hashmap1 = {'diligent':'employed', 'fond':'enamored', 'guide':'usher', 'outfit':'garb', 'wrath':'anger'}
hashmap2 = {'diligent':'idle', 'fond':'averse', 'guide':'follow', 'flow':'jam', 'wrath':'delight'}

print(left_join(hashmap1,hashmap2))