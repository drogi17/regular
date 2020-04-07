from copy import copy

class Regular_vals:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Regular:
    __name__ = "Regular"

    def __init__(self, first=Regular_vals()):
        self.first = first

    def add(self, *values):
        now = self.first
        while now.next != None:
            now = now.next
        for value in values:
            now.next = Regular_vals()
            now = now.next
            now.data = value
        return Regular(first=self.first)

    def get(self, num: int):
        now = self.first
        for _ in range(num+1):
            if now.next != None:
                now = now.next
            else: 
                return None
        return now.data

    def delete(self, num: int) -> bool:
        now = self.first
        for _ in range(num):
            if now.next != None:
                now = now.next
            else:
                return False
        to_del = now.next
        now.next = now.next.next
        del to_del
        return True

    def clear(self) -> bool:
        now = self.first
        while (now.next != None):
            now = now.next
            del self.first
            self.first = now
        return True

    def sort(self) -> bool:
        now_global = self.first
        while (now_global.next != None):
            now = self.first
            while (now.next != None):
                if isinstance(now.data, int) and isinstance(now.next.data, int):
                    if (now.data != None) and now.data > now.next.data:
                        now.data, now.next.data = now.next.data, now.data
                else:
                    if (now.data != None) and ord(str(now.data)[0]) > ord(str(now.next.data)[0]):
                        now.data, now.next.data = now.next.data, now.data
                now = now.next
            now_global = now_global.next
        return True

    def insert(self, pos: int, value):
        now = self.first
        for _ in range(pos):
            if now.next != None:
                now = now.next
            else:
                now.next = Regular_vals()
                now = now.next
                now.data = value
                return True
        new_element = Regular_vals()
        new_element.data = value
        new_element.next = now.next
        now.next = new_element
        return True

    def __getitem__(self, num: int):
        now = self.first
        for _ in range(num+1):
            if now.next != None:
                now = now.next
            else: 
                raise IndexError('Regular index out of range.')
        return now.data

    def __setitem__(self, key:int, value) -> bool:
        if key == None or key == '':
            self.add(value)
            return True
        now = self.first
        for _ in range(key+1):
            if now.next != None:
                now = now.next
            else:
                now.next = Regular_vals()
                now = now.next
                now.data = value
                return True
        now.data = value
        return True


    def __str__(self):
        now = self.first
        if now.next == None:
            return 'None'
        string = '~('
        while now.next != None:
            now = now.next
            if isinstance(now.data, int):
                string += str(now.data) + ', '
            elif isinstance(now.data, str):
                string += '"' + str(now.data) + '", '
            else:
                string += str(now.data) + ', '
        string = string[:len(string)-2] + ')~'
        return string

    def __len__(self):
        len_ = 0
        now = self.first
        while now.next != None:
            now = now.next
            len_ += 1
        return len_ 
