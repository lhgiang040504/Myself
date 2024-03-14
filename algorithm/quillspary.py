import sys
all_inputs = list(map(str.strip, sys.stdin.readlines()))
timeline = list(map(float, all_inputs[1].split(" ")))
initial_damage = float(all_inputs[2])
increased_damage = float(all_inputs[3])
time_expires = float(all_inputs[4])

class Thorns():
    def __init__(self, initial_damage, increased_damage, initial_time, time_expires):
        self.initial_damage = initial_damage
        self.increased_damage = increased_damage
        self.initial_time = initial_time
        self.time_expires = time_expires
    def get_damage(self, curr_time):
        if curr_time == self.initial_time:
            return initial_damage
        if curr_time - self.initial_time > self.time_expires:
            return 0
        return self.increased_damage
    def check(self, curr_time):
        if curr_time - self.initial_time > self.time_expires:
            return True

list_thorns = []
total_damage = 0
for time in timeline:
    list_thorns.append(Thorns(initial_damage, increased_damage, time, time_expires))
    for i, thorn in enumerate(list_thorns):
        total_damage += thorn.get_damage(time)
    while True:
        if list_thorns[0].check(time):
            del list_thorns[0]
        else:
            break

sys.stdout.write(str(int(total_damage)))