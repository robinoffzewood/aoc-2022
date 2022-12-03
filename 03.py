class Part1:
    result = 0
    _histogram = [{}, {}]

    def __init__(self, file: str):
        with open(f'{file}', mode='r', encoding='utf-8') as f:
            self._input = f.readlines()

    def compute(self):
        for line in self._input:
            self._histogram[0].clear()
            self._histogram[1].clear()
            compart_1, compart_2 = self._split_line(line)
            self._count_this_rucksack([compart_1, compart_2])
            for item_left in self._histogram[0]:
                if item_left in self._histogram[1]:
                    if item_left.isupper():
                        self.result += ord(item_left) - ord('A') + 27
                    else:
                        self.result += ord(item_left) - ord('a') + 1

    def _count_this_rucksack(self, comparts: list[str]):
        for i, compart in enumerate(comparts):
            for c in compart:
                self._update_histogram(c, self._histogram[i])

    @staticmethod
    def _split_line(line: str) -> (str, str):
        line = line.rstrip()
        half_line = len(line) >> 1
        assert len(line) % 2 == 0
        left = line[:half_line]
        right = line[half_line:]
        return left, right

    @staticmethod
    def _update_histogram(c, histogram):
        if c not in histogram:
            histogram[c] = True


class Part2(Part1):
    _histogram = [{}, {}, {}]

    def compute(self):
        item_found = False
        for i, line in enumerate(self._input):
            line = line.rstrip()
            for c in line:
                self._update_histogram(c, self._histogram[i % 3])
            if (i + 1) % 3 == 0:
                for j in range(0, 3):
                    for item_j in self._histogram[j]:
                        if item_j in self._histogram[(j + 1) % 3] and item_j in self._histogram[(j + 2) % 3]:
                            if item_j.isupper():
                                self.result += ord(item_j) - ord('A') + 27
                            else:
                                self.result += ord(item_j) - ord('a') + 1
                            item_found = True
                            break
                    if item_found:
                        item_found = False
                        break
                for j in range(0, 3):
                    self._histogram[j].clear()


if __name__ == '__main__':
    for input_dir in ['test-files', 'input-files']:
        part_1 = Part1(f'{input_dir}/03.txt')
        part_1.compute()
        if input_dir == 'test-files':
            assert part_1.result == 157
        else:
            print(part_1.result)

        part_2 = Part2(f'{input_dir}/03.txt')
        part_2.compute()
        if input_dir == 'test-files':
            assert part_2.result == 70
        else:
            print(part_2.result)
