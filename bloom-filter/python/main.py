class BloomFilter:
    def __init__(self, size, k):
        self.size = size
        self.k = k
        self.array = [0] * self.size

    def add(self, string):
        hashed = hash(string)
        for i in range(self.k):
            val = i + hashed
            idx = val % self.size
            self.array[idx] = 1

    def has(self, string):
        hashed = hash(string)
        for i in range(self.k):
            val = i + hashed
            idx = val % self.size
            if self.array[idx] == 0:
                return False
        return True


if __name__ == '__main__':
    b_filter = BloomFilter(20, 3)
    b_filter.add('Doraemon')
    b_filter.add('Nobita')

    print(b_filter.has('Doraemon'))
    print(b_filter.has('Shizuka'))
    print(b_filter.has('Nobita'))
    print(b_filter.has('Gian'))
