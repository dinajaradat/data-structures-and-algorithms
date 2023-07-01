from cc30.linkedlist import LinkedList

class HashTable():
    def __init__(self,size=4):
        self.size = size
        self.map = [None]*size

    def custom_hash(self, key):
        sum_of_asccii = 0
        for ch in key:
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp = sum_of_asccii*599
        indx = temp%self.size
        return indx
    
    def set(self, key, value):
        hashed_key = self.custom_hash(key)
        if not self.map[hashed_key]: 
            self.map[hashed_key] = [key,value]
        else: 
            if isinstance(self.map[hashed_key], LinkedList):
                self.map[hashed_key].add([key,value])
            else:
                chain = LinkedList()
                exsiting_pair = self.map[hashed_key]
                new_pair = [key, value]
                self.map[hashed_key] = chain
                chain.add(exsiting_pair)
                chain.add(new_pair)

    def hash(self, key):
        return self.custom_hash(key)

    def get(self, key):
        hashed_key = self.custom_hash(key)
        if isinstance(self.map[hashed_key], LinkedList):
            bucket = self.map[hashed_key]
            for i in bucket:
                if i[0] == key:
                    return i[1]
                

        else:
            if self.map[hashed_key] and self.map[hashed_key][0] == key:
                return self.map[hashed_key][1]


    def has(self, key):
        hashed_key = self.custom_hash(key)
        if isinstance(self.map[hashed_key], LinkedList):
            bucket = self.map[hashed_key]
            for i in bucket:
                if i[0] == key:
                    return True
        else:
            if self.map[hashed_key] and self.map[hashed_key][0] == key:
                return True
        return False

    def keys(self):
        array = []

        if self.map is None:
          return []
        
        for bucket in self.map:
            if bucket is not None:
                if isinstance(bucket, LinkedList):
                    current = bucket.head
                    while current:
                        array.append(current.data[0])
                        current = current.next
                else:
                    key = bucket[0]
                    array.append(key)
        return array
        
