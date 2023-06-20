import re
def Insert_by_most_recent (sorted , value):
    i = 0
    while value['year'] > sorted[i]['year']:
        i+=1
    # print(i)
    while i < len(sorted):
        temp = sorted[i]
        sorted[i] = value 
        value = temp
        i+=1
    sorted.append(value)
    

def By_most_recent(array):
    len_array = len(array)
    if len_array == 0:
        return []
    sorted = []
    sorted.append(array[0])
    # print(sorted)

    for i in range (1, len_array):
        Insert_by_most_recent(sorted , array[i])
        # print(sorted)
        
    return sorted


def insert_alphabetical (sorted , value):
    i = 0
    pattern = r'^(A *|An *|The *)\s'
    match = re.search(pattern, value['title'] , re.IGNORECASE)
    if  not match :

        while i < len(sorted) and value['title'] > sorted[i]['title']  :
            i+=1
        # print(i)
        while i < len(sorted):
            temp = sorted[i]
            sorted[i] = value 
            value = temp
            i+=1
        sorted.append(value)
    

def Alphabetical(array):
    sorted = []
    sorted.append(array[0])
    len_array = len(array)
    if len_array == 0:
        return []
    # print(sorted)

    for i in range (1, len_array):
        insert_alphabetical(sorted , array[i])
        # print(sorted)
        
    return sorted

if __name__ == "__main__":
    array = [{"title":"C" , "year" : 5 , "genres" :["action"]} , {"title":"An B" , "year" : 2 , "genres" :["action"]} , {"title":"TA" , "year" : 1 , "genres" :["action"]}]
    print(By_most_recent(array))
    print(Alphabetical(array))






