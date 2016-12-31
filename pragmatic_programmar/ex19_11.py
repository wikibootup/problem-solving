class enumOperator(object):

    def __init__(self):
        self.name_filename = 'name.txt'

    def read_name_file(self):
        with open(self.name_filename, 'r') as f:
            return f.read()
