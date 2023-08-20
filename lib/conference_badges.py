def badge_maker(name):
    message = f"Hello, my name is {name}."
    return message

def batch_badge_creator(names):
    badge_list = [f'Hello, my name is {name}.' for name in names]
    return badge_list

def assign_rooms(names):
    assigned_rooms = []
    room=1
    for name in names:
        assigned_rooms.append(f'Hello, {name}! You\'ll be assigned to room {room}!')
        room+=1
    return assigned_rooms

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for assignment in assign_rooms(names):
        print(assignment)