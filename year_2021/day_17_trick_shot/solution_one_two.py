

def function(target_x_min=124, target_x_max=174, target_y_min=-86, target_y_max=-123):
    height_max = 0
    good_throws = 0
    for x_speed in range(target_x_max + 1):
        for y_speed in range(target_y_max, -target_y_max):
            # Initial Position: x = 0, y = 0, y_max = 0
            x_position, y_position = 0, 0
            tmp_y_max = 0
            # Speed setting
            test_x_speed = x_speed
            test_y_speed = y_speed
            while True:
                # Target passed
                if x_position > target_x_max or y_position < target_y_max:
                    break
                # Update positions (old position plus speed)
                x_position += test_x_speed
                y_position += test_y_speed
                tmp_y_max = max(y_position, tmp_y_max)
                # Target hit
                if target_x_min <= x_position <= target_x_max and target_y_max <= y_position <= target_y_min:
                    height_max = max(height_max, tmp_y_max)
                    good_throws += 1
                    break
                # Update speed
                test_x_speed, test_y_speed = update_speed(test_x_speed, test_y_speed)
    # Returns the max height and the number of times the target is hit
    return height_max, good_throws


# Helper function =====================================================================================================

def update_speed(x_speed, y_speed):
    # The vertical speed is always decreased by 1
    y_speed -= 1
    # If the horizontal speed is positive it is decreased by 1
    if x_speed > 0:
        x_speed -= 1
    # If the horizontal speed is negative it is increased by 1
    elif x_speed < 0:
        x_speed += 1
    return x_speed, y_speed

# =====================================================================================================================
