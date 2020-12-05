class Pes:
    '''pes se pase'''

    def __init__(self, size):
        self.size = size

    def get_size(self):
        print(f"pes size: {self.size}.")


a = Pes(34)
a.get_size()
a.size = 8998
print(a.size)
