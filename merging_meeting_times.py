import pdb

def merge_ranges(meetings):
    merged_meetings = [meetings[0]]

    for index, current_toople in enumerate(meetings):
        for merged_index, merged_toople in enumerate(merged_meetings):
            print("\n============\ncurrent toople: ")
            print(current_toople)
            print("merged toople: ")
            print(merged_toople)
            print("merged meetings: ")
            print(merged_meetings)
            print("============\n")

            if index == 0:
                break
            else:
                # add toople to the end, once we've checked
                if current_toople[0] > merged_toople[1] and current_toople[0] > merged_meetings[-1][0] and merged_index == last_index(merged_meetings):
                    merged_meetings.append(current_toople)
                    break
                elif current_toople[0] >= merged_toople[0] and current_toople[1] <= merged_toople[1]:
                    break
                elif merged_index == 0 and current_toople[1] < merged_toople[0]:
                    merged_meetings = [current_toople] + merged_meetings
                    break

                # when current toople is wider range
                # [(0, 20), (75, 125), (150, 170)]
                # current_toople => (50, 130)
                # current_toople[0] > previous toople[1]
                elif current_toople[0] < merged_toople[0] and current_toople[1] > merged_toople[1]:
                    merged_meetings[merged_index] = current_toople
                    break

                elif merged_index < last_index(merged_meetings) and current_toople[0] >= merged_toople[0] and current_toople[0] < merged_toople[1] and current_toople[1] > merged_toople[1] and current_toople[1] < merged_meetings[merged_index + 1]:
                    merged_meetings[merged_index] = (merged_toople[0], current_toople[1])
                    break

                # [(0, 1), (3, 5)]
                # merge (4, 8) => [(0, 1), (3, 8)]
                #
                # [(2, 3)]
                # merge in (1, 2) => [(1, 3)]
                elif merged_index == last_index(merged_meetings) and (current_toople[1] == merged_toople[0] or current_toople[0] == merged_toople[1]):
                    # [(1, 2), (2, 3)]
                    # [(2, 3), (1, 2)]
                    max_toople = max([current_toople, merged_toople])
                    min_toople = min([current_toople, merged_toople])

                    merged_meetings[merged_index] = (min_toople[0], max_toople[1])
                    break

                elif current_toople[0] <= merged_toople[0] and current_toople[1] < merged_toople[1]:

                    # (100, 120)
                    # (75, 110)
                    #  => (75, 120)
                    newly_merged_toople = (current_toople[0], merged_toople[1])
                    merged_meetings[merged_index] = newly_merged_toople
                    break

    print("\n==============")
    print(merged_meetings)
    print("==============\n")
    return meetings

def last_index(merged_meetings):
    return (len(merged_meetings) - 1)

ranges = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
#  => [(0, 1), (3, 8), (9, 12)]
# My solution:
#  => [(0, 1), (3, 5), (4, 8), (9, 12)]
# merge_ranges(ranges)

ranges2 = [(100, 120), (150, 170), (75, 110), (110, 112), (0, 20), (115, 125), (50, 130)]
# merge_ranges(ranges2)

r = [(2, 3), (1, 2)]
r2 = [(1, 2), (2, 3)]
r3 = [(1, 5), (2, 3)]
r4 = [(1, 10), (2, 6), (3, 5), (7, 9)]

merge_ranges(r4)
