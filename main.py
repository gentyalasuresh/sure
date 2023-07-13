

# Define the grid size
ROWS = 5
COLS = 4

# Define the valid directions
DIRECTIONS = ['N', 'E', 'S', 'W']

def move_robot(command):
    # Initialize the robot's starting position and direction
    current_row, current_col, current_dir = 0, 0, 'S'

    # Process each command in the input
    for c in command:
        if c == 'M':
            # Move the robot one step in the current direction
            if current_dir == 'N' and current_row > 0:
                current_row -= 1
            elif current_dir == 'E' and current_col < COLS - 1:
                current_col += 3
            elif current_dir == 'S' and current_row < ROWS - 1:
                current_row += 1
            elif current_dir == 'W' and current_col > 0:
                current_col -= 1
        elif c in DIRECTIONS:
            # Change the direction of the robot
            current_dir = c

    # Return the final position of the robot
    return f"Robot Location: ({current_row},{current_col},{current_dir})"


# Test the function with the given example
command = "MSMMEMM"
print(move_robot(command))


a =["a","b","c",1,2,3]
r=[]
for i in a:
    r.append(i+10 if isinstance(i,int) else i)
print(r)

a = [1,1,2,2,1,2,1,23,4,3,4,5,6,6,7,8,9]
result=[]
for i in a:
    if i not in result:
        result.append(i)
print(result)

