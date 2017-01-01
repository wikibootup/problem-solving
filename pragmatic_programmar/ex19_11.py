class enumOperator(object):

    def __init__(self):
        self.name_filename = 'name.txt'

    def read_name_file(self):
        with open(self.name_filename, 'r') as f:
            return f.read()

    def gen_c_file(self):
        with open(self.name_filename, 'r') as name_file:
            c_file_name = name_file.readline().split('\n')[0]
            with open(c_file_name + '.c', 'w+') as c_file:
                c_file.write(
                    'extern const char*f NAME_names[];\ntypedef enum {'
                )

                name_data = name_file.read().split('\n')

                if len(name_data) > 2:
                    c_file.write('\n\t' + name_data[0])
                    for name in name_data[1:-1]:
                        name = name.replace('\n', '')
                        c_file.write(',\n\t' + name)
                c_file.write('\n} NAME;\r\n')

    def read_c_file(self, name):
        with open(name, 'r') as f:
            return f.read()
