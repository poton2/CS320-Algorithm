from sys import argv, exit


# provided
#
# Read integers from the given filename.
#
# Return value: list of integers
def read_array(filename):
    try:
        with open(filename) as f:
            return [int(n) for n in f.read().split()]
    except:
        exit("Couldn’t read numbers from file \"" + filename + "\"")


# implement
#
# Return the number of inversions in the given list, by doing a merge
# sort and counting the inversions.
#
# Return value: number of inversions
def count_inversions(in_list):
    if len(in_list) == 1:
        return 0
    # divide list into two halves A and B
    length = len(in_list)
    middle_index = length / 2
    A = in_list[:int(middle_index)]
    B = in_list[int(middle_index):]
    r_A = count_inversions(A)
    r_B = count_inversions(B)
    merge = merge_i(A, B, in_list)
    return r_A + r_B + merge


# implement
#
# Merge the left & right lists into in_list.  in_list already contains
# values--replace those with the merged values.
#
# Return value: inversion count
def merge_i(L, R, in_list):
    count = 0
    i = 0
    j = 0
    k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            in_list[k] = L[i]
            k += 1
            i += 1
        else:
            in_list[k] = R[j]
            count += len(L) - i
            k += 1
            j += 1

    while i < len(L):
        in_list[k] = L[i]
        k += 1
        i += 1

    while j < len(R):
        in_list[k] = R[j]
        k += 1
        j += 1

    return count


# provided
if __name__ == '__main__':
    if len(argv) != 2:
        exit("usage: python3 " + argv[0] + " datafile")
    in_list = read_array(argv[1])
    print(count_inversions(in_list))
