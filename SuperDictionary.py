class _:
    @classmethod
    def __set_dic(cls):
        cls.__dic = {}

    def __init__(self, **dic): 
        self.__set_dic()       
        for key, value in dic.items():
            self.__dic[key] = value
    def __str__(self):
        return repr(self.__dic)
    
    def __getattr__(self, key):
        if key in self.__dic:
            return self.__dic[key]
        else:
            raise KeyError("No such a key in the dictionary") 

    def __setattr__(self, key, value):
        if key not in self.__dic:            
            if not "__i" in key:
                self.__dic[key] = value
            if "__i" in key:
                self.__dict__[key] = value
        else:
            raise KeyError("Such a key already is in the dictionary") 

    def __delattr__(self, key):
        if key in self.__dic:
            del self.__dic[key]
            delattr(self, key)
    
    def __getitem__(self, key):
        if key in self.__dic:
            return self.__dic[key]
        else:
            raise KeyError("No such a key in the dictionary")
    def __setitem__(self, key, value):
        if key not in self.__dic.keys():
            self.__dic[key] = value

    def __delitem__(self, key):
        if key in self.__dic.keys():
            del self.__dic[key]
    
    def __contains__(self, item):
        is_key = item in self.__dic.keys()
        is_value = item in self.__dic.values() 
        return is_key or is_value   
  
    def __len__(self):
        return len(self.__dic)

    def __iter__(self):
        self.__i = 0
        return self

    def __next__(self):
        if self.__i > self.__len__() - 1:
            raise StopIteration
        else:            
            key_list = list(self.__dic.keys())            
            key = key_list[self.__i]            
            value = self.__dic[key]
            self.__i += 1           
            return (key, value)

if __name__ == "__main__":
    d = _(
        name = "Victor",
        age = 31, 
        sex = "male")
    d.func = lambda x, y : x + y
    print(31 in d) # True
    for k, v in d:
        print(k, v) # name Victor 
    print(d.func(10, 90)) # 100
    print(d["func"](10, 80)) #90