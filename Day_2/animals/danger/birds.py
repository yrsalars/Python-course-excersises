
  #%%
class Birds:
    def __init__(self):
        '''Constructor for this class'''
        #Create some member animals
        self.members = ['eagle','dragon']

    def printMembers(self):
        print('Printing member of the Bird class')
        for member in self.members:
            print('\t%s ' % member)



# %%
