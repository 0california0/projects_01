# collions detection player 1
    # width
    if player_1_pos.x >= screen.get_width():
        player_1_pos.x = screen.get_width()
    if player_1_pos.x <= screen.get_width() - screen.get_width():
        player_1_pos.x = screen.get_width() - screen.get_width()
    # height
    if player_1_pos.y >= screen.get_height():
        player_1_pos.y = screen.get_height()
    if player_1_pos.y <= screen.get_height() - screen.get_height():
        player_1_pos.y = screen.get_height() - screen.get_height()