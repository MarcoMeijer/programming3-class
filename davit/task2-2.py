import re

def sum_game_ids():
    gid_sum = 0
    max_r = 12
    max_g = 13
    max_b = 14
    with open("./txt/games.txt", "r") as file:
        gid_pattern = "(\\d+(?=:))"
        sets_pattern = "(?<=:)(.*)"
        r_pattern = "(\\d+)(?=\\sred)"
        g_pattern = "(\\d+)(?=\\sgreen)"
        b_pattern = "(\\d+)(?=\\sblue)"

        for line in file:
            is_valid = True
            gid = int(re.search(gid_pattern, line).group(0))
            sets = re.search(sets_pattern, line).group(0)
            sets = re.split(";", sets)
            for s in sets:
                r_count = re.search(r_pattern, s)
                if r_count:
                    r_count = int(r_count.group(0))
                    if r_count > max_r: is_valid = False

                g_count = re.search(g_pattern, s)
                
                if g_count:
                    g_count = int(g_count.group(0))
                    if g_count > max_g: is_valid = False

                b_count = re.search(b_pattern, s)
                if b_count:
                    b_count = int(b_count.group(0))
                    if b_count > max_b: is_valid = False
                    
            if is_valid: gid_sum += gid

    print(gid_sum)


def sum_powers():
    power_sum = 0
    with open("./txt/games.txt", "r") as file:
        sets_pattern = "(?<=:)(.*)"
        r_pattern = "(\\d+)(?=\\sred)"
        g_pattern = "(\\d+)(?=\\sgreen)"
        b_pattern = "(\\d+)(?=\\sblue)"

        for line in file:
            r_max = g_max = b_max = 0
            sets = re.search(sets_pattern, line).group(0)
            sets = re.split(";", sets)
            
            for s in sets:
                r_val = re.search(r_pattern, s)
                if r_val:
                    r_val = int(r_val.group(0))
                    if r_val > r_max: r_max = r_val

                g_val = re.search(g_pattern, s)
                if g_val:
                    g_val = int(g_val.group(0))
                    if g_val > g_max: g_max = g_val

                b_val = re.search(b_pattern, s)
                if b_val:
                    b_val = int(b_val.group(0))
                    if b_val > b_max: b_max = b_val
                    
            power = r_max * g_max * b_max
            power_sum += power

    print(power_sum)

sum_game_ids()
sum_powers()
