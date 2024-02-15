class Stone:
    def __init__(self, Power, Color, Job):
        self.Power = Power
        self.Color = Color
        self.Job = Job


Stones_list = [
    Stone("space", "Blue", "Controlling the objects"),
    Stone("mind", "Yellow", "Controlling others"),
    Stone("reality", "Red", "Making an illusion of something"),
    Stone("power", "Purple", "Undefeatable"),
    Stone("time", "Green", "Doesn't need explaining"),
    Stone("soul", "Orange", "I've no idea what the hell this is")
]


def show_stone(name):
    for stone in Stones_list:
        if name == stone.Power:
            print(f"Name: {stone.Power}, Color: {stone.Color}, Job: {stone.Job}")


print("HELLO BABE")
for stone in Stones_list:
    print(f"{stone.Power} Stone")
    max_length = max(len(stone.Power) for stone in Stones_list) + 7  # Adjusted to consider the extra characters
    print("-" * max_length)

choice = input("So tell me: -->")


if choice in [stone.Power for stone in Stones_list]:
    show_stone(choice)
else:
    print("Really?")
