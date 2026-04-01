def grade(env):
    health = env.crop_health
    water = env.water

    if health > 80 and water > 80:
        return 1.0
    elif health > 60:
        return 0.7
    elif health > 40:
        return 0.4
    else:
        return 0.1