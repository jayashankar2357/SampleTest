def find_path(pyramid, target):
    def dfs(row, col, path, product):
        if row == len(pyramid):
            if product == target:
                return path
            return None
        
        left_path = dfs(row + 1, col, path + "L", product * pyramid[row][col])
        right_path = dfs(row + 1, col + 1, path + "R", product * pyramid[row][col])
        print(f"row is {row}, row-col value is {pyramid[row][col]} and product is {product},"+
               f"left_path is {left_path}, right_path is {right_path} and path is {path}")
        if left_path:
            return left_path
        if right_path:
            return right_path
        return None
    
    path = dfs(0, 0, "", 1)
    return path

# Example given in instructions
pyramid = [
    [2],
    [4, 3],
    [3, 2, 6],
    [2, 9, 5, 2],
    [10, 5, 2, 15, 5]
]

target = 720

result = find_path(pyramid, target)
if result:
    print("Path Found:", result[:-1])
else:
    print("No path found.")
