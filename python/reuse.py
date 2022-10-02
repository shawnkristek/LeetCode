import os, re

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def values(self):
        values = [self.val]
        next = self.next
        while next:
            values.append(next.val)
            next = next.next

        return values

    def __repr__(self):
        return str(self.values())

    def build(self, values: list[int]) -> 'ListNode':
        '''
        Given an array of ints,
        Return a linked-list 
        [n1, n2, n3] -> n1->n2->n3
        '''
        next = None
        for v in reversed(values):
            next = ListNode(v, next)

        return next

def rename():
    for file in os.listdir('.'):
        if file.endswith('.py'):
            if file.find('-') > -1:
                new = file.replace('-','_')
                os.rename(file, new)

def alphaFiles():
    titles = []
    for file in os.listdir('.'):
        if file.endswith('.py'):
            number = file.split('_',1)[0]
            name = re.sub("\d+_","", file)
            name = re.sub("_"," ", name)
            name = re.sub(".py","", name)
            name = name.title()
            titles.append((name,number))
    titles.sort()
    for title in titles:
        spaces = ' ' * (5 - len(title[1]))
        print(f'{title[1]}{spaces}{title[0]}')

if __name__ == '__main__':
    alphaFiles()