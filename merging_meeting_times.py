import pdb

def merge_ranges(meetings):
    merged_meetings = [meetings[0]]
    print("\n============")
    print(merged_meetings)
    print("============\n")

    for index, current_toople in enumerate(meetings):


        for merged_index, merged_toople in enumerate(merged_meetings):
            # if current_toople == (4, 8):
            #     pdb.set_trace()
            # merged_index == [0]
            # current_toople (150, 170)
            # compare current_toople with meetings[merged_toople]
            #  => (100, 120)

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
                # toople_index_zero = current_toople[0] # 150
                # toople_index_one = current_toople[1] # 170
                # merged_toople => (100, 120)
                # current_toople => (75, 110)
                # merged_index [0, 1]

                # add toople to the end, once we've checked
                if current_toople[0] > merged_toople[1] and current_toople[0] > merged_meetings[-1][0] and merged_index == last_index(merged_meetings):
                    merged_meetings.append(current_toople)
                    # print("\ninside current_toople[0] > merged_toople[1]")
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

                # shoot, what about when current_toople is in between 2 merged tuples ?
                # will need to merge all 3 !!!
                # solve this case later
                elif merged_index < last_index(merged_meetings) and current_toople[0] >= merged_toople[0] and current_toople[0] < merged_toople[1] and current_toople[1] > merged_toople[1] and current_toople[1] < merged_meetings[merged_index + 1]:
                    merged_meetings[merged_index] = (merged_toople[0], current_toople[1])
                    break

                # [(0, 1), (3, 5)]
                # merge (4, 8) => [(0, 1), (3, 8)]
                elif merged_index == last_index(merged_meetings) and current_toople[0] >= merged_toople[0] and current_toople[0] < merged_toople[1] and current_toople[1] > merged_toople[1]:
                    merged_meetings[merged_index] = (merged_toople[0], current_toople[1])
                    break

                elif current_toople[0] <= merged_toople[0] and current_toople[1] < merged_toople[1]:
                    # print("\ninside current_toople[0] <= merged_toople[0] and current_toople[1] <= merged_toople[1]")

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
merge_ranges(ranges2)
