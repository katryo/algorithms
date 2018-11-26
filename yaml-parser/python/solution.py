class MyYamlParser:
    def __init__(self):
        self.table = {}

    def _parse_line_space(self, line):
        key, value = line.rstrip('\n').split(':')
        value = value.strip()
        # key might have white spaces
        i = 0
        while key[i] == ' ':
            i += 1
        return i, key[i:], value

    def _pop_stack(self, stack):
        popped_space, popped_key, popped_val = stack.pop()
        if stack:
            stack[-1][2][popped_key] = popped_val
        else:
            self.table[popped_key] = popped_val

    def parse(self, filename):
        with open(filename, 'r') as file:
            stack = []
            for line in iter(file.readline, ''):
                space, key, value = self._parse_line_space(line)
                while stack and stack[-1][0] >= space:
                    self._pop_stack(stack)
                if value == "":
                    stack.append([space, key, {}])
                else:
                    if stack:
                        stack[-1][2][key] = value
                    else:
                        self.table[key] = value
            while stack:
                self._pop_stack(stack)

    # "k2.k21" => "v21"
    def query(self, query_string):
        keys = query_string.split('.')
        cur = self.table
        for key in keys:
            cur = cur[key]
            if not cur:
                raise Exception('No value found by the query')
        return cur


yaml = MyYamlParser()
yaml.parse('input.yaml')
print(yaml.query('k1'))
print(yaml.query('k2.k4.k6'))
print(yaml.query('k8'))
print(yaml.query('k8.k9'))
