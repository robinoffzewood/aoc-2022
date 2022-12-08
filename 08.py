class Part1:
    result: int
    w: int
    h: int
    forest: list[list[int]]

    def __init__(self, file: str):
        self.result = 0
        self.w = 0
        self.h = 0
        self.forest = []
        with open(f'{file}', mode='r', encoding='utf-8') as f:
            row_idx = 0
            for line in f.readlines():
                self.forest.append([])
                line = line.rstrip()
                for col_idx, tree in enumerate(line):
                    self.forest[row_idx].append(int(tree))
                row_idx += 1
            self.h = len(self.forest)
            self.w = len(self.forest[0])

    def compute(self):
        self.result = 2 * (self.w + self.h - 2)
        for i in range(1, self.w - 1):
            for j in range(1, self.h - 1):
                if self.is_visible(i, j):
                    self.result += 1

    def is_visible(self, cur_row: int, cur_col: int) -> bool:
        cur_h = self.forest[cur_row][cur_col]
        if cur_h > self._get_highest_in_this_direction(cur_row, cur_col, 'U'):
            return True
        if cur_h > self._get_highest_in_this_direction(cur_row, cur_col, 'L'):
            return True
        if cur_h > self._get_highest_in_this_direction(cur_row, cur_col, 'R'):
            return True
        if cur_h > self._get_highest_in_this_direction(cur_row, cur_col, 'D'):
            return True

        return False

    def _get_highest_in_this_direction(self, cur_row: int, cur_col: int, direction: str) -> int:
        sweep = self._get_sweep(cur_col, cur_row, direction)
        highest = 0
        for i in sweep:
            if direction == 'L' or direction == 'R':
                highest = max(highest, self.forest[cur_row][i])
            else:
                highest = max(highest, self.forest[i][cur_col])
        return highest

    def _get_sweep(self, cur_col, cur_row, direction):
        if direction == 'L':
            sweep = range(cur_col - 1, -1, -1)
        if direction == 'R':
            sweep = range(cur_col + 1, self.w)
        if direction == 'D':
            sweep = range(cur_row + 1, self.h)
        if direction == 'U':
            sweep = range(cur_row - 1, -1, -1)
        return sweep


class Part2(Part1):
    def compute(self):
        for i in range(1, self.w - 1):
            for j in range(1, self.h - 1):
                self.result = max(self._scenic_score(i, j), self.result)

    def _scenic_score(self, cur_row: int, cur_col: int) -> int:
        score = 1
        cur_h = self.forest[cur_row][cur_col]
        score *= self._get_viewing_distance(cur_col, cur_h, cur_row, 'U')
        score *= self._get_viewing_distance(cur_col, cur_h, cur_row, 'L')
        score *= self._get_viewing_distance(cur_col, cur_h, cur_row, 'R')
        score *= self._get_viewing_distance(cur_col, cur_h, cur_row, 'D')
        return score

    def _get_viewing_distance(self, cur_col, cur_h, cur_row, direction: str):
        viewing_distance = 0
        sweep = self._get_sweep(cur_col, cur_row, direction)
        for i in sweep:
            if direction == 'L' or direction == 'R':
                height = self.forest[cur_row][i]
            else:
                height = self.forest[i][cur_col]
            viewing_distance += 1
            if height >= cur_h:
                break
        return viewing_distance


if __name__ == '__main__':
    for input_dir in ['test-files', 'input-files']:
        part_1 = Part1(f'{input_dir}/08.txt')
        part_1.compute()
        if input_dir == 'test-files':
            assert part_1.result == 21
        else:
            assert part_1.result == 1796
            print(part_1.result)

        part_2 = Part2(f'{input_dir}/08.txt')
        part_2.compute()
        if input_dir == 'test-files':
            assert part_2.result == 8
        else:
            print(part_2.result)
