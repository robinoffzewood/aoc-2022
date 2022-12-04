class Part1:
    result = 0

    def __init__(self, file: str):
        with open(f'{file}', mode='r', encoding='utf-8') as f:
            self._input = f.readlines()

    def compute(self):
        for l in self._input:
            l = l.rstrip()
            elves_range = l.split(',')
            if self._overlap(elves_range[0], elves_range[1]) or self._overlap(elves_range[1], elves_range[0]):
                self.result += 1

    @staticmethod
    def _to_int(range_str: str) -> (int, int):
        start = int(range_str.split('-')[0])
        end = int(range_str.split('-')[1])
        return start, end

    @staticmethod
    def _overlap(a: str, b: str) -> bool:
        start_a, end_a = Part1._to_int(a)
        start_b, end_b = Part1._to_int(b)
        if start_a <= start_b and end_a >= end_b:
            return True
        else:
            return False


class Part2(Part1):
    @staticmethod
    def _overlap(a: str, b: str) -> bool:
        start_a, end_a = Part1._to_int(a)
        start_b, end_b = Part1._to_int(b)
        if (start_a <= start_b) and (end_a >= start_b):
            return True
        if (start_b <= start_a) and (end_b >= start_a):
            return True
        else:
            return False


if __name__ == '__main__':
    for input_dir in ['test-files', 'input-files']:
        part_1 = Part1(f'{input_dir}/04.txt')
        part_1.compute()
        if input_dir == 'test-files':
            assert part_1.result == 2
        else:
            print(part_1.result)

        part_2 = Part2(f'{input_dir}/04.txt')
        part_2.compute()
        if input_dir == 'test-files':
            assert part_2.result == 4
        else:
            print(part_2.result)
