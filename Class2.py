class Table():
 
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.table = [[0] * cols for _ in range(rows)]
 
    def get_value(self, row, col):
        return (self.table[row][col] if 0 <= row < self.rows and 0 <= col < self.cols
                else None)
 
    def set_value(self, row, col, value):
        self.table[row][col] = value
 
    def n_rows(self):
        return self.rows
 
    def n_cols(self):
        return self.cols
 
    def delete_row(self, row):
        self.table.pop(row)
        self.rows -= 1
 
    def delete_col(self, col):
        for row in range(self.rows):
            self.table[row].pop(col)
        self.cols -= 1
 
    def add_row(self, row):
        self.table.insert(row, [0] * self.cols)
        self.rows += 1
 
    def add_col(self, col):
        for row in range(self.rows):
            self.table[row].insert(col, 0)
        self.cols += 1

tab = Table(5, 6)
tab.set_value(0, 1, 1)
tab.set_value(1, 2, 2)
tab.set_value(2, 3, 3)
tab.set_value(3, 4, 4)
tab.set_value(4, 5, 5)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()