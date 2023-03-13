 #%%
class Fish:
    def __init__(self):
        '''Constructor for this class'''
        #Create some member animals
        self.members = ['Salmon','Whale','goldfish']

    def printMembers(self):
        print('Printing member of the Fish class')
        for member in self.members:
            print('\t%s ' % member)