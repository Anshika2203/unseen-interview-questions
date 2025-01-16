from collections import deque

class UserMainCode(object):
    @classmethod
    def MonkeyVsHooman(cls, input1, input2, input3, input4):
        N = input1  # Number of trees
        H = input2  # Height of each tree
        X = input3 - 1  # Convert 1-indexed starting tree to 0-indexed
        slippery_indices = input4  # Slippery indices of the trees

        # BFS queue with (current tree index, current height, number of turns, is_jumping)
        queue = deque([(X, 0, 0, True)])  # Start on the given tree at height 0
        visited = set()  # To track visited states (tree, height, is_jumping)

        while queue:
            curr_tree, curr_height, turns, is_jumping = queue.popleft()

            # If we reach or exceed the height H, return the number of turns
            if curr_height >= H:
                return turns

            # Avoid revisiting the same state
            if (curr_tree, curr_height, is_jumping) in visited:
                continue
            visited.add((curr_tree, curr_height, is_jumping))

            # Perform the current action (jump or slide)
            if is_jumping:
                # Jump up on the current tree
                next_height = curr_height + slippery_indices[curr_tree]
                if next_height <= H:  # Only process valid heights
                    queue.append((curr_tree, next_height, turns + 1, False))
            else:
                # Slide down on the current tree
                next_height = max(0, curr_height - slippery_indices[curr_tree])
                queue.append((curr_tree, next_height, turns + 1, True))

            # Allow switching to adjacent trees
            for neighbor in [curr_tree - 1, curr_tree + 1]:
                if 0 <= neighbor < N:
                    queue.append((neighbor, curr_height, turns + 1, not is_jumping))

        # If it's impossible to reach the top of any tree, return -1
        return -1


# Test cases
# Test case 1
input1 = 6
input2 = 10
input3 = 3
input4 = [4, 3, 1, 1, 5, 2]
output1 = UserMainCode.MonkeyVsHooman(input1, input2, input3, input4)
print(output1)  # Expected output: 7

# Test case 2
input1 = 5
input2 = 10
input3 = 1
input4 = [3, 1, 2, 2, 5]
output2 = UserMainCode.MonkeyVsHooman(input1, input2, input3, input4)
print(output2)  # Expected output: 7