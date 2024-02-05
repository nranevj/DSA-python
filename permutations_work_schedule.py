"""
    This is a permutation problem, 
    where we want to find the possible permutations of work schedule hours possible 
    considering the current restriction of 4 hours of daily work at maximum (day_hours), and weekly maximum hours
    one can work (work_hours).
    "08??840"

    Output:
    [
    "0840840",
    "0831840",
    "0822840",
    "0813840",
    "0804840"
    ]
"""


def find_schedule(work_hours, day_hours, pattern):
    num_of_slots = 0
    rem_hours = work_hours
    for p in pattern:
        if p == "?":
            num_of_slots += 1
        else:
            rem_hours -= int(p)
    result = []
    temp_result = []
    find_schedule_helper(
        rem_hours, num_of_slots, pattern, day_hours, temp_result, result
    )
    return result


def find_schedule_helper(
    rem_hours, num_of_slots, pattern, day_hours, temp_result, result
):
    # print(f"slots {num_of_slots} rem_hours {rem_hours} temp res {temp_result}")
    if num_of_slots == 0 and rem_hours == 0:
        # add to result

        index = 0
        temp = []
        for p in pattern:
            if p == "?":
                temp.append(str(temp_result[index]))
                index += 1
            else:
                temp.append(p)
        result.append("".join(temp))
    elif num_of_slots > 0 and rem_hours >= 0:
        # choose hours
        hours = min(day_hours, rem_hours)
        while hours >= 0:
            temp_result.append(hours)
            find_schedule_helper(
                rem_hours - hours,
                num_of_slots - 1,
                pattern,
                day_hours,
                temp_result,
                result,
            )
            temp_result.pop()
            hours -= 1


pattern = "08??840"

print(find_schedule(24, 4, pattern))
