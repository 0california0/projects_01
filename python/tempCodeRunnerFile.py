t = 1 - math.exp(-turn_rate * dt)
    velocity_x_player_1 += (target_velocity_x - velocity_x_player_1) * t
    velocity_y_player_1 += (target_velocity_y - velocity_y_player_1) * t