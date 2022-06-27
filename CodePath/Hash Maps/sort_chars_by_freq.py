class Solution:
    def frequencySort(self, s: str) -> str:
        my_dict = {} # Where key is the character and value is count
        
        for char in s:
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
        print(my_dict.items())
        
        # Return list sorted by FREQUENCY
        my_list = list(my_dict.items())
        print(my_list)
        
        return_tuple = sorted(my_list, key= lambda x: x[1], reverse=True)
        print(return_tuple)
        
        return_string = ""
        for char, count in return_tuple:
            return_string += char*count
        return return_string
