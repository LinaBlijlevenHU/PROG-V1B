def read_lockers(fname = "fa_testkluizen.txt"):
    '''
    Read the file with the lockers
    :return:    list    List of lockers and passwords
    '''

    # Read the contents of the file
    with open(fname) as f:
        lines = f.readlines()

    # Strip the new line tags, split on the ; symbol and return
    # the list of lockers and passwords
    return [line.strip("\n").split(';') for line in lines]

print(read_lockers())

lijst = [1, 2, 4, 65, 3, 3, 2, 7, 8]

for getal in lijst:
    print(getal)
    if getal == 7:
        print("gevonden!")
        break

