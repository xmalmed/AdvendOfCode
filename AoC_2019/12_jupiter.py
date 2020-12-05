import numpy as np


class Moon:
    def __init__(self, position, velocity=(0, 0, 0)):
        self.position = np.array(position)
        self.velocity = np.array(velocity)

    def next_position(self):
        self.position += self.velocity

    def change_velocity_by(self, vector):
        self.velocity += vector


io = Moon((-17, 9, -5))
eu = Moon((-1, 7, 13))
ga = Moon((-19, 12, 5))
ca = Moon((-6, -6, -4))

t1 = Moon((-1, 0, 2))
t2 = Moon((2, -10, -7))
t3 = Moon((4, -8, 8))
t4 = Moon((3, 5, -1))

moons = [io, eu, ga, ca]


# moons = [t1, t2, t3, t4]

def apply_gravity():
    for m1 in moons:
        for m2 in moons:
            vel_change = np.sign(m2.position - m1.position)
            m1.change_velocity_by(vel_change)


def update_positions():
    for m in moons:
        m.next_position()


def total_energy(moon):
    pot_en = sum(abs(moon.position))
    kin_en = sum(abs(moon.velocity))
    return pot_en * kin_en


def create_checkpoint(moons):
    ch_p = []
    for m in moons:
        ch_p += [tuple(m.position), tuple(m.velocity)]
    return tuple(ch_p)


def is_cycle_found(ch_p):
    if ch_p in all_steps:
        return True
    else:
        return False


cycle = False
all_steps = {}

for i in range(1000000000):
    checkpoint = create_checkpoint(moons)
    if checkpoint in all_steps:
        print('Found')
        print(i)
        break
    else:
        all_steps[checkpoint] = i

    if i % 1000000 == 0:
        print(f'checkpoint: {checkpoint}')
        print(i)

    apply_gravity()
    update_positions()

# energy
total_en = 0
for m in moons:
    print(m.position, m.velocity)
    total_en += total_energy(m)

print(f"Total energy: {total_en}")
