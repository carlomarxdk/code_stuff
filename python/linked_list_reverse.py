class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    data = [None]
    temp = head
    while temp:
        data.append(temp.data)
        temp = temp.next
    for i in range(len(data)):
        try:
            head.data = data[len(data)-i]
            head = head.next
        except:
            pass