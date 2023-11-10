class Map:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Map, cls).__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        self.load_map(1)

    def load_map(self, map_num):
        map_filename = f"map-{map_num}.txt"
        with open(map_filename, "r") as file:
            self.map = [list(line.strip()) for line in file]
        self.revealed = [[False] * len(self.map[0]) for _ in range(len(self.map))]

    def __getitem__(self, row):
        return self.map[row]

    def __len__(self):
        return len(self.map)

    def show_map(self, loc):
        result = ""
        hero_row, hero_col = loc

        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                if self.revealed[r][c] or (r == hero_row and c == hero_col):
                    if r == hero_row and c == hero_col:
                        result += "*"
                    else:
                        result += self.map[r][c]
                else:
                    result += "x"
            result += "\n"
        return result

    def reveal(self, loc):
        self.revealed[loc[0]][loc[1]] = True

    def remove_at_loc(self, loc):
        self.map[loc[0]][loc[1]] = "n"
