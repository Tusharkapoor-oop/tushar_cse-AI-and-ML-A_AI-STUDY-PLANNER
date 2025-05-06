import random

def generate_schedule(topics, days=5):
    # look, I’m just trying to split this stuff across the week
    if not topics:
        return {}

    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"][:days]

    sched = {}
    for d in weekdays:
        sched[d] = []

    j = 0
    for t in topics:
        day = weekdays[j % days]
        sched[day].append(t)
        j += 1

    # I don’t wanna leave days empty, let them at least do something
    for d in weekdays:
        if len(sched[d]) == 0:
            sched[d].append("Enjoy your free day or work on your hobby!")

    return sched




