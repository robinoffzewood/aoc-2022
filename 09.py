class Pos:
    x: int = 0
    y: int = 0

    def my_hash(self) -> int:
        return self.y * 1000 + self.x


class Part1:
    result: int
    _lines: list[str]
    head: Pos
    tail: list[Pos]
    past_pos: dict[int, bool]

    def __init__(self, file: str, tail_size: int):
        self.result = 0
        self.past_pos = {}
        self.head = Pos()
        self._tail_size = tail_size
        self.tail = []
        for _ in range(0, self._tail_size):
            self.tail.append(Pos())
        with open(f'{file}', mode='r', encoding='utf-8') as f:
            self._lines = f.readlines()

    def compute(self):
        for line in self._lines:
            line = line.rstrip()
            for action in self._extract_actions(line):
                self._move_head(action)
                self._move_tail()
                tail = self.tail[self._tail_size - 1]
                self.past_pos[tail.my_hash()] = True
        self.result = len(self.past_pos)

    @staticmethod
    def _extract_actions(line: str) -> list[str]:
        direction = line.split(' ')[0]
        assert direction in ['R', 'L', 'U', 'D']
        cnt = int(line.split(' ')[1])
        return [direction] * cnt

    def _move_head(self, action: str):
        if action == 'R':
            self.head.x += 1
        if action == 'L':
            self.head.x -= 1
        if action == 'U':
            self.head.y += 1
        if action == 'D':
            self.head.y -= 1

    def _move_tail(self):
        h = self.head
        for i in range(0, self._tail_size):
            t = self.tail[i]
            h_distance = h.x - t.x
            v_distance = h.y - t.y
            if abs(h_distance) + abs(v_distance) > 2:
                t.x += int(h_distance / abs(h_distance))
                t.y += int(v_distance / abs(v_distance))
            else:
                if abs(h_distance) > 1:
                    t.x += int(h_distance / abs(h_distance))
                if abs(v_distance) > 1:
                    t.y += int(v_distance / abs(v_distance))

            h = t


if __name__ == '__main__':
    for input_dir in ['test-files', 'input-files']:
        part_1 = Part1(f'{input_dir}/09.txt', 1)
        part_1.compute()
        if input_dir == 'test-files':
            assert part_1.result == 13
        else:
            print(part_1.result)

        if input_dir == 'test-files':
            part_2 = Part1(f'{input_dir}/09.txt', 9)
            part_2.compute()
            assert part_2.result == 1
            part_2 = Part1(f'{input_dir}/09-B.txt', 9)
            part_2.compute()
            assert part_2.result == 36
        else:
            part_2 = Part1(f'{input_dir}/09.txt', 9)
            part_2.compute()
            print(part_2.result)


def test_move_tail():
    p = Part1('test-files/09.txt', 1)
    p.head.x += 1
    p._move_tail()
    assert (p.tail.r, p.tail.c) == (0, 0)
    p.head.x += 1
    p._move_tail()
    assert (p.tail.r, p.tail.c) == (0, 1)
    p.head.x = -1
    p._move_tail()
    assert (p.tail.r, p.tail.c) == (0, 0)
    p.head.x = 0
    p.head.y = 1
    p._move_tail()
    assert (p.tail.r, p.tail.c) == (0, 0)
    p.head.y = 2
    p._move_tail()
    assert (p.tail.r, p.tail.c) == (1, 0)
    p.head.y = -1
    p._move_tail()
    assert (p.tail.r, p.tail.c) == (0, 0)
    p.head.y = -2
    p._move_tail()
    assert (p.tail.r, p.tail.c) == (-1, 0)
    p.tail.r = 0
    p.tail.c = 0
    p.head.y = 1
    p.head.x = 2
    p._move_tail()
    assert (p.tail.r, p.tail.c) == (0, 1)
