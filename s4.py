class InstanceCounter(object):
    count = 0

    def __init__(self, val, intval):
        self.val = val
        self.intval = self.filterint(intval)
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval 

    def get_val(self):
        return self.val 

    @classmethod
    def get_count(cls):
        return cls.count 

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            return 0
        else:
            return value


a = InstanceCounter(5, 5)
b = InstanceCounter(13, 13)
c = InstanceCounter(17, 17)

for obj in (a,b,c):
    print(f"val of object: {obj.get_val()}")
    print(f"count: {obj.get_count()}")

print(a.intval)
print(b.intval)
print(c.intval)