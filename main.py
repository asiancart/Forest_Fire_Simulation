import sys

print("Water Bucket by asiancart")

Goal = 4
steps = 0

waterInBucket = {"8":0,"5":0,"3":0}

while True:
    print()
    print("Try to get "+str(Goal)+ "L of water into one of these")
    print("buckets:")

    waterDisplay = []
    for i in range(1,9):
        if waterInBucket["8"] < i:
            waterDisplay.append("      ")
        else:
            waterDisplay.append("WWWWWW")

    for i in range(1,6):
        if waterInBucket["5"] <i:
            waterDisplay.append("      ")
        else:
            waterDisplay.append("WWWWWW")

    for i in range(1,4):
        if waterInBucket["3"] < i:
            waterDisplay.append("      ")
        else:
            waterDisplay.append("WWWWWW")

    print("""
    8|{7}|
    7|{6}|
    6|{5}|
    5|{4}| 5|{12}|
    4|{3}| 4|{11}|
    3|{2}| 3|{10}| 3|{15}|
    2|{1}| 2|{9}| 2|{14}|
    1|{0}| 1|{8}| 1|{13}|
     +------+ +------+ +------+
        8L       5L       3L          
    """.format(*waterDisplay))

    for waterAmount in waterInBucket.values():
        if waterAmount == Goal:
            print("Good job! You solved it in",steps, "steps!")
            sys.exit()

    print("You can:")
    print("  (F)ill the bucket")
    print("  (E)mpty the bucket")
    print("  (P)our one bucket into another")
    print("  (Q)uit")

    while True:
        move = input("> ").upper()
        if move == "QUIT" or move == "Q":
            print("Thanks for playing!")
            sys.exit()

        if move in ("F","E","P"):
            break
        print("Enter F,E,P or Q")

    while True:
        print("Select a bucket 8,5,3 or QUIT")
        srcBucket = input("> ").upper()

        if srcBucket == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if srcBucket in ("8","5","3"):
            break

    if move == "F":
        srcBucketSize = int(srcBucket)
        waterInBucket[srcBucket] = srcBucketSize
        steps += 1

    elif move == "E":
        waterInBucket[srcBucket] = 0
        steps +=1

    elif move == "P":
        while True:
            print("Select a bucket to pour into: 8,5 or 3")
            dstBucket = input("> ").upper()
            if dstBucket in ("8","5","3"):
                break

        dstBucketSize = int(dstBucket)
        emptySpaceInDstBucket = dstBucketSize - waterInBucket[dstBucket]
        waterInSrcBucket = waterInBucket[srcBucket]
        amountToPour = min(emptySpaceInDstBucket,waterInSrcBucket)

        waterInBucket[srcBucket] -= amountToPour

        waterInBucket[dstBucket] += amountToPour
        steps += 1

    elif move == "C":
        pass