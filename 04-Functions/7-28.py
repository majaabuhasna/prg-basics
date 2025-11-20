def f(dice):
    max_streak_char = dice[0]
    max_streak_length = 1

    current_char = dice[0]
    current_streak_length = 1

    for i in range(1, len(dice)):
        if dice[i] == current_char:
            current_streak_length += 1
        else:
            if current_streak_length > max_streak_length:
                max_streak_length = current_streak_length
                max_streak_char = current_char

            current_char = dice[i]
            current_streak_length = 1

    if current_streak_length > max_streak_length:
        max_streak_char = current_char

    return int(max_streak_char)

print(f("5233165554211"), f("2133"), sep='\n')