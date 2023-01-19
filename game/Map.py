class Map:

    grid = []

    def __init__(self, width: int, height: int, tile_size: int):
        self.width = width
        self.height = height
        self.tile_size = tile_size

        self.grid = [[0 for x in range(width)] for y in range(height)]

    def draw(self, display: Canvas):
        for tile in self.grid:
            tile.draw(display);

    def update(self):
        pass
        