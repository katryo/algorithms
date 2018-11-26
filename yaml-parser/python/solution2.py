class MyYamlParser:
    def __init__(self):
        self.table = {}

    def _parse_line(self, line):
        key, value = line.split(':')
        value = value.strip()
        i = 0
        while key[i] == ' ':
            i += 1
        return i, key[i:], value

    def _pop_insert_stack(self, stack):
        p_space, p_key, p_value = stack.pop()
        if stack:
            stack[-1][2][p_key] = p_value
        else:
            self.table[p_key] = p_value

    def parse(self, filename):
        with open(filename, 'r') as f:
            stack = []
            for line in iter(f.readline, ''):
                space, key, value = self._parse_line(line)
                while stack and stack[-1][0] >= space:
                    self._pop_insert_stack(stack)
                if value == '':
                    stack.append([space, key, {}])
                else:
                    if stack:
                        stack[-1][2][key] = value
                    else:
                        self.table[key] = value
            while stack:
                self._pop_insert_stack(stack)

    def query(self, query_string):
        queries = query_string.split('.')
        cur = self.table
        for query in queries:
            cur = cur[query]
            if not cur:
                raise Exception('No value found for the query')
        return cur


yaml = MyYamlParser()
yaml.parse('input.yaml')
print(yaml.query('k2'))
print(yaml.query('k2.k4'))
print(yaml.query('k8'))
print(yaml.query('k8.k9'))
print(yaml.query('k8.k9.k11'))
