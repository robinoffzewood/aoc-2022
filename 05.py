import re

class Part1:
    result = ''
    _stacks: dict[int, list[str]] = {}
    _procedure: str = ''

    def __init__(self, file: str):
        with open(f'{file}', mode='r', encoding='utf-8') as f:
            stacks_and_proc = f.read().split('\n\n')
            self._procedure = stacks_and_proc.pop()
            stacks = stacks_and_proc.pop().rstrip()
            n_stacks = int(stacks[len(stacks) - 1])
            for i in range(1, n_stacks + 1):
                self._stacks[i] = list()
            for line in stacks.splitlines(keepends=True):
                if line.startswith(' 1'):
                    break
                for i in range(1, n_stacks + 1):
                    crate = line[:4]
                    if crate[1:2] != ' ':
                        self._stacks[i].append(crate[1:2])
                    if crate.endswith('\n'):
                        break
                    line = line[4:]
        for i in range(1, n_stacks + 1):
            self._stacks[i].reverse()

    def compute(self):
        for line in self._procedure.splitlines():
            (crate_count, stack_from, stack_to) = self._parse_action(line)
            for _ in range(0, crate_count):
                self._stacks[stack_to].append(self._stacks[stack_from].pop())
        for stack in self._stacks.values():
            self.result += stack.pop()

    @staticmethod
    def _parse_action(line: str) -> (int, int, int):
        captures = re.search(r"move (\d+) from (\d+) to (\d+)", line.rstrip())
        assert len(captures.groups()) == 3
        return int(captures.group(1)), int(captures.group(2)), int(captures.group(3))


class Part2(Part1):
    def compute(self):
        for line in self._procedure.splitlines():
            (crate_count, stack_from, stack_to) = self._parse_action(line)
            to_move: list[str] = []
            for _ in range(0, crate_count):
                to_move.append(self._stacks[stack_from].pop())
            to_move.reverse()
            self._stacks[stack_to].extend(to_move)

        for stack in self._stacks.values():
            self.result += stack.pop()


if __name__ == '__main__':
    for input_dir in ['test-files', 'input-files']:
        part_1 = Part1(f'{input_dir}/05.txt')
        part_1.compute()
        if input_dir == 'test-files':
            assert part_1.result == 'CMZ'
        else:
            print(part_1.result)

        part_2 = Part2(f'{input_dir}/05.txt')
        part_2.compute()
        if input_dir == 'test-files':
            assert part_2.result == 'MCD'
        else:
            print(part_2.result)
