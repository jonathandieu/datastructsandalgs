def min_rooms(intervals: list):

    # create sorted lists of start and end times
    starts = sorted([interval[0] for interval in intervals])
    ends = sorted([interval[1] for interval in intervals])

    max_conference_rooms = 0 # global
    conference_rooms = 0 # current

    # two pointers to compare starts to ends
    s = 0
    e = 0

    while s < len(intervals):
        # If the start time is < end time, we know we need a new room; process our next start time
        if starts[s] < ends[e]:
            conference_rooms += 1
            s += 1
        else:
            conference_rooms -= 1
            e += 1
        max_conference_rooms = max(conference_rooms, max_conference_rooms)
    return max_conference_rooms



print(min_rooms([[13,15],[1,13],[6,9]]))