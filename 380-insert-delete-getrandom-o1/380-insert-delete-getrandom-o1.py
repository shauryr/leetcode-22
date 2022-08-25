class RandomizedSet:
    import random
    def __init__(self):
        '''
        list will store the val
        dict will store the index and val; key:val = value:index
        '''
        self.list_idx = []
        self.dict_idx = {}

    def insert(self, val: int) -> bool:
        '''
        if item is present return False
        else: add item to the list and add to the dict
        '''
        if val in self.dict_idx:
            return False
        self.list_idx.append(val)
        self.dict_idx[val] = len(self.list_idx) - 1
        return True

    def remove(self, val: int) -> bool:
        '''
        remove the element from the list
        replace it with the last element in the list
        pop the list
        update the index of the last element with the replaced index in the dict
        del the element from the dict
        '''
        if val in self.dict_idx:
            index_val = self.dict_idx[val] # get the index of the val
            last_element = self.list_idx[-1] # get the last val in list
            self.list_idx[index_val] = last_element # copy last element to the list idx 
            self.dict_idx[last_element] = index_val # update index of the last element in the dict
            # remove from list and remove from dict
            self.list_idx.pop()
            del self.dict_idx[val]
            return True
        
        return False

    def getRandom(self) -> int:
        return random.choice(self.list_idx)

