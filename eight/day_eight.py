from pprint import pprint
from copy import deepcopy

def day_one():
    with open("eight/day_eight_input.txt") as f:
        data = f.readlines()
        tree_grid = []
        for line in data:
            tree_grid.append(list(map(int, (list(line.rstrip())))))
        #pprint(tree_grid)
        visibility_mask = [[0 for i in range(len(tree_grid[0]))] for j in range(len(tree_grid))]

        grid_x = len(tree_grid[0])
        grid_y = len(tree_grid)

        current_max = 0
        # left to right
        for i in range(grid_y):
            current_max = -1
            for j in range(grid_x):
                CUR_TREEEEE = tree_grid[i][j]
                if tree_grid[i][j] > current_max:
                    current_max = tree_grid[i][j]
                    visibility_mask[i][j] = 1

    
        # right to left
        for i in range(grid_y):
            current_max = -1
            for j in range(grid_x-1, -1, -1):
                CUR_TREEEEE = tree_grid[i][j]
                if tree_grid[i][j] > current_max:
                    current_max = tree_grid[i][j]
                    visibility_mask[i][j] = 1

        
        # top to bot
        for j in range(grid_x):
            current_max = -1
            for i in range (grid_y):
                CUR_TREEEEE = tree_grid[i][j]
                if tree_grid[i][j] > current_max:
                    current_max = tree_grid[i][j]
                    visibility_mask[i][j] = 1

        
        # bot to top
        for j in range(grid_x):
            current_max = -1
            CUR_TREEEEE = tree_grid[i][j]
            for i in range (grid_y-1, -1, -1):
                if tree_grid[i][j] > current_max:
                    current_max = tree_grid[i][j]
                    visibility_mask[i][j] = 1

        visibility_count = 0
        for i in range(grid_y):
            visibility_count += sum(visibility_mask[i])

def day_two():
    with open("eight/day_eight_input.txt") as f:
        data = f.readlines()
        tree_grid = []
        for line in data:
            tree_grid.append(list(map(int, (list(line.rstrip())))))
        #pprint(tree_grid)
        score_mask = [[0 for i in range(len(tree_grid[0]))] for j in range(len(tree_grid))]

        grid_x = len(tree_grid[0])
        grid_y = len(tree_grid)

        scores = []

        for y in range(grid_y):
            for x in range(grid_x):
                tree_height = tree_grid[y][x]

                trees_left = tree_grid[y][0:x][::-1]
                trees_right = tree_grid[y][x+1:grid_x]
                tree_col = []
                for col, val in enumerate(tree_grid[y]):
                    tree_col.append(tree_grid[col][x])
                trees_top = tree_col[0:y][::-1]
                trees_bot = tree_col[y+1:grid_y]

                left_score = 0
                right_score = 0
                up_score = 0
                down_score = 0

                max_height = 20000
                for i in range(len(trees_left)):
                    if trees_left[i] >= tree_height:
                        left_score += 1
                        break
                    if trees_left[i] < tree_height:
                        left_score += 1
                        max_height = tree_grid[y][x-i]
                    else:
                        break
                
                max_height = 20000
                for i in range(len(trees_right)):
                    if trees_right[i] >= tree_height:
                        right_score += 1
                        break
                    if trees_right[i] < tree_height:
                        right_score += 1
                        max_height = tree_grid[y][x+i+1]
                    else:
                        break
                
                max_height = 20000
                for i in range(len(trees_top)):
                    if trees_top[i] >= tree_height:
                        up_score += 1
                        break
                    if trees_top[i] < tree_height:
                        up_score += 1
                        max_height = tree_grid[y-i][x]
                    else:
                        break
            
                max_height = 20000
                for i in range(len(trees_bot)):
                    if trees_bot[i] >= tree_height:
                        down_score += 1
                        break
                    if trees_bot[i] < tree_height:
                        down_score += 1
                        max_height = tree_grid[y+i+1][x]
                    else:
                        break
                
                # print(f'Location: {x}, {y}')
                # print(f'Left: {left_score}')
                # print(f'Right: {right_score}')
                # print(f'Up: {up_score}')
                # print(f'Down: {down_score}')


                dir_scores = filter(lambda x: x != 0, [left_score, right_score, up_score, down_score])
                total_tree_score = 1
                for i in dir_scores:
                    total_tree_score *= i

                print(total_tree_score)

                scores.append(total_tree_score)
                score_mask[y][x] = total_tree_score

    pprint(max(scores))
day_two()