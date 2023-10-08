def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(badge_maker(name))
    return badges

def assign_rooms(names):
    return None

def printer(names):
    return None
