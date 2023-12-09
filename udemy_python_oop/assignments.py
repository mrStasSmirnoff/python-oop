class MaxSizeList(object):

    def __init__(self, max_length):
        self.max_length_list = max_length
        self.result_list = []

    def push(self, value):
        self.result_list.append(value)

        if len(self.result_list) > self.max_length_list:
            self.result_list.pop(0)

    def get_list(self):
        return self.result_list

    
    