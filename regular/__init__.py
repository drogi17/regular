from copy import copy

class Regular_vals:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Regular:
    __name__ = "Regular"

    def __init__(self, convert=None):
        self.first = Regular_vals()
        if convert:
            try:
                num_ = 0
                while True:
                    self.add(convert[num_])
                    num_+=1;
            except IndexError:
                pass
    def add(self, *values):
        now = self.first
        while now.next != None:
            now = now.next
        for value in values:
            now.next = Regular_vals()
            now = now.next
            now.data = value
        return self

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

    def __getitem__(self, args):
        if not isinstance(args, slice):
            now = self.first
            for _ in range(args+1):
                if now.next != None:
                    now = now.next
                else: 
                    raise IndexError('Regular index out of range.')
            return now.data
        else:
            start_ = args.start
            stop_ = args.stop
            step_ = args.step
            if step_ == None: step_ = 1
            if start_ == None: start_ = 0
            if stop_ == None: stop_ = len(self)
            keys_ = Regular(range(start_, stop_, step_))
            new_regular = Regular()
            for num in keys_:
                now = self.first
                for _ in range(num+1):
                    if now.next != None:
                        now = now.next
                    else:
                        raise IndexError('Regular index out of range.')
                new_regular.add(now.data)
            return new_regular

    def __setitem__(self, key:int, value) -> bool:
        if key == None or key == '':
            self.add(value)
            return True
        now = self.first
        if not isinstance(key, slice):
            for _ in range(key+1):
                if now.next != None:
                    now = now.next
                else:
                    now.next = Regular_vals()
                    now = now.next
                    now.data = value
                    return True
            now.data = value
        else:
            start_ = key.start
            stop_ = key.stop
            step_ = key.step
            if step_ == None: step_ = 1
            if start_ == None: start_ = 0
            if stop_ == None: stop_ = len(self)
            keys_ = Regular(range(start_, stop_, step_))
            new_regular = Regular()
            for num in keys_:
                now = self.first
                for _ in range(num+1):
                    if now.next != None:
                        now = now.next
                    else:
                        now.next = Regular_vals()
                        now = now.next
                        now.data = value
                        break
                    now.data = value
        return True


    def __str__(self):
        now = self.first
        if now.next == None:
            return 'None' 
        string = '~(' + ', '.join(str(x) for x in self) + ')~'
        return string

    def __len__(self):
        len_ = 0
        now = self.first
        while now.next != None:
            now = now.next
            len_ += 1
        return len_ 

    def __rshift__(self, regul):
        new_regul = Regular()
        now_1 = self.first
        now_2 = regul.first
        while now_1.next != None or now_2.next != None:
            now_1 = now_1.next
            now_2 = now_2.next
            new_regul.add(now_1.data + now_2.data)
        return new_regul

    def __add__(self, regul):
        new_regul = Regular()
        now_1 = self.first
        now_2 = regul.first
        while now_1.next != None:
            now_1 = now_1.next
            new_regul.add(now_1.data)
        while now_2.next != None:
            now_2 = now_2.next
            new_regul.add(now_2.data)
        return new_regul