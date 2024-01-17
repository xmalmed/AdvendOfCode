import math

from utils.puzzle import Puzzle
from parse import parse

#
# def next_minute(status, time):
#     if time < 24: ##
#         tt = time + 1
#         st = status.copy()
#         st["ore"] = st["ore"]
#         st["clay"] += st["clay_bot"]
#         st["ob"] += st["ob_bot"]
#         st["geode"] += st["geode_bot"]
#         # NOP
#         next_minute(st, tt)
#
#         if status["ore"] >= ORE:
#             st1 = st.copy()
#             st1["ore"] -= ORE
#             st1["ore_bot"] += 1
#             next_minute(st1, tt)
        # if ...



def next_bot(status, time):
    if time > 28 and status["geode_bot"] == 0:
        return
    # ore bot
    if status["ore_bot"] < 4:
        t = math.ceil(max(ORE - status["ore"], 0) / status["ore_bot"]) + 1
        if t + time < T:
            st = status.copy()
            st["ore"] += t*status["ore_bot"] - ORE
            st["clay"] += t*st["clay_bot"]
            st["ob"] += t*st["ob_bot"]
            st["geode"] += t*st["geode_bot"]
            st["ore_bot"] += 1
            next_bot(st, time + t)

    # clay bot
    if status["clay_bot"] < 10:
        t = math.ceil(max(CLAY - status["ore"], 0) / status["ore_bot"]) + 1
        if t + time < T:
            st = status.copy()
            st["ore"] += t*status["ore_bot"] - CLAY
            st["clay"] += t*st["clay_bot"]
            st["ob"] += t*st["ob_bot"]
            st["geode"] += t*st["geode_bot"]
            st["clay_bot"] += 1
            next_bot(st, time + t)

    # ob bot
    if status["clay_bot"] > 0 and status["ob_bot"] < 8:
        t1 = math.ceil(max(0, OB_ORE - status["ore"]) / status["ore_bot"])
        t2 = math.ceil(max(0, OB_CLAY - status["clay"]) / status["clay_bot"])
        t = max(t1, t2) + 1
        if t + time < T:
            st = status.copy()
            st["ore"] += t*status["ore_bot"] - OB_ORE
            st["clay"] += t*st["clay_bot"] - OB_CLAY
            st["ob"] += t*st["ob_bot"]
            st["geode"] += t*st["geode_bot"]
            st["ob_bot"] += 1
            next_bot(st, time + t)

    # geode bot
    if status["ob_bot"] > 0:
        t1 = math.ceil(max(0, GEODE_ORE - status["ore"]) / status["ore_bot"])
        t2 = math.ceil(max(0, GEODE_OB - status["ob"]) / status["ob_bot"])
        t = max(t1, t2) + 1
        if t + time < T:
            st = status.copy()
            st["ore"] += t*status["ore_bot"] - GEODE_ORE
            st["clay"] += t*st["clay_bot"]
            st["ob"] += t*st["ob_bot"] - GEODE_OB
            st["geode"] += t*st["geode_bot"]
            st["geode_bot"] += 1
            next_bot(st, time + t)

    # rest of the time production
    t = T - time
    geodes = status["geode"] + status["geode_bot"] * t

    global MAX_GEODE
    if geodes > MAX_GEODE:
        MAX_GEODE = geodes
        # print(MAX_GEODE)
    return


if __name__ == "__main__":
    p = Puzzle()
    # data = p.load_input()
    data = p.load_input('input_part2.txt')
    # data = p.load_input('input_test.txt')
    T = 32
    # T = 24
    STATUS = {"ore": 0,
              "clay": 0,
              "ob": 0,
              "geode": 0,
              "ore_bot": 1,
              "clay_bot": 0,
              "ob_bot": 0,
              "geode_bot": 0,
              }
    Q = 0
    TOTAL = []

    for blueprint in data:
        BP, ORE, CLAY, OB_ORE, OB_CLAY, GEODE_ORE, GEODE_OB = parse("Blueprint {:d}: Each ore robot costs {:d} ore. Each clay robot costs {:d} ore. Each obsidian robot costs {:d} ore and {:d} clay. Each geode robot costs {:d} ore and {:d} obsidian.", blueprint)
        MAX_GEODE = 0
        next_bot(STATUS.copy(), 0)
        print(BP, MAX_GEODE)
        Q += BP * MAX_GEODE
        TOTAL.append(MAX_GEODE)

    print()
    print(Q)
    print(TOTAL)
    print(math.prod(TOTAL))

# {"location": [{"chromosome": "chr21", "starting_position": "40000000", "ending_position": "41000000"}], "allele": {"variant_type": ["SNP", "INS"]}}