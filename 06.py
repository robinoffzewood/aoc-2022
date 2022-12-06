
class Part1:
    result: list[int] = []
    _lines: list[str] = []

    def __init__(self, file: str, width: int):
        self.result = []
        self._lines = []
        self._w = width
        with open(f'{file}', mode='r', encoding='utf-8') as f:
            for line in f.readlines():
                self._lines.append(line.rstrip())

    def compute(self):
        for line in self._lines:
            self.result.append(self._nb_char(line))

    def _nb_char(self, line: str) -> int:
        for i in range(0, len(line) - self._w):
            if self._is_sop(line[i:i + self._w]):
                return i + self._w
        raise Exception

    @staticmethod
    def _is_sop(chars: str) -> bool:
        dico = []
        for c in chars:
            if c in dico:
                return False
            dico.append(c)
        return True


class Part2(Part1):
    pass


if __name__ == '__main__':
    for input_dir in ['test-files', 'input-files']:
        part_1 = Part1(f'{input_dir}/06.txt', 4)
        part_1.compute()
        if input_dir == 'test-files':
            assert part_1.result[0] == 7
            assert part_1.result[1] == 5
            assert part_1.result[2] == 6
            assert part_1.result[3] == 10
            assert part_1.result[4] == 11
        else:
            print(part_1.result[0])

        part_2 = Part2(f'{input_dir}/06.txt', 14)
        part_2.compute()
        if input_dir == 'test-files':
            assert part_2.result[0] == 19
            assert part_2.result[1] == 23
            assert part_2.result[2] == 23
            assert part_2.result[3] == 29
            assert part_2.result[4] == 26
        else:
            print(part_2.result[0])
