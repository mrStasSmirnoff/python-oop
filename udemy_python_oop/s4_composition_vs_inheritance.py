import abc 

# abstract class, serves as a constructor for child classes
class GetSetParent(object):

    __metaclass__ = abc.ABCMeta 

    def __init__(self, value):
        self.val = 0

    def set_val(self, value):
        self.val = value 

    def get_val(self):
        return self.val 

    @abc.abstractclassmethod
    def showdoc(self):
        return

# first child class
class GetSetInt(GetSetParent):

    def set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super(GetSetInt, self).set_val(value) # "call the parent"

    def showdoc(self):
        print('GetSetInt object ({0}), only accepts'
        'integer values'.format(id(self)))

x = GetSetInt(3) 
print(x.get_val()) # will print 0 since we initiated with 0 
x.set_val(5)
print(x.get_val()) # will print 5 since we set value 5
x.showdoc()

class GetSetList(GetSetParent):

    def __init__(self, value=0):
        self.vallist = [value]

    def get_val(self):
        return self.vallist[-1]

    def get_vals(self):
        return self.vallist

    def set_val(self, value):
        self.vallist.append(value)

    def showdoc(self):
        print('GetSetList object len {0}, stores '
        'history of values set'.format(len(self.vallist)))

print('Adding GetSEtList class')
gls = GetSetList(5)
gls.set_val(10)
gls.set_val(20)
print(gls.get_val())
print(gls.get_vals())
gls.showdoc()
