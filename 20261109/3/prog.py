class Maze:
    def __init__(self, n):
        self.n = n
        self.maze = [['█'] * (2 * n  + 1) for _ in range(2 * n + 1)]
        for y in range(n):
            for x in range(n):
                self.maze[2 * y + 1][2 * x + 1] = '·'

    def __setitem__(self, key, value):
        x0, sl, y1 = key
        y0, x1 = sl.start, sl.stop
        if x0 != x1 and y0 != y1:
            return

        dx = (x1 > x0) - (x1 < x0)
        dy = (y1 > y0) - (y1 < y0)
        x, y = x0, y0
        while (x, y) != (x1, y1):
            self.maze[2 * y + 1 + dy][2 * x + 1 + dx] = value
            x, y = x + dx, y + dy

    def __getitem__(self, key):
        x0, sl, y1 = key
        y0, x1 = sl.start, sl.stop
        start, finish = (x0, y0), (x1, y1)

        tosee, seen = [start], {start}
        while tosee:
            x, y = tosee.pop()
            if (x, y) == finish:
                return True

            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.n and 0 <= ny < self.n and (nx, ny) not in seen and self.maze[2 * y + 1 + dy][2 * x + 1 + dx] == '·':
                    tosee.append((nx, ny))
                    seen.add((nx, ny))
        return False

    def __str__(self):
        return '\n'.join(''.join(line) for line in self.maze)

import sys
exec(sys.stdin.read())
