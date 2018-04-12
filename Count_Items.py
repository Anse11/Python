#Counter, Counts how many times given item appears in sequence


def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count
