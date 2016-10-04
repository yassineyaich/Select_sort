def sort(arr):
    l = len(arr)
    for j in range(l):
        min = arr[j]
        print "outside loop is: ", j
        for i in range(j,l):
            print "inside loop is: ", i
            if arr[i] < min:
                min = arr[i]
                minindex = i
                ##print "minimum number is ", min, " and arr[", minindex, "] needs to be swapped"
        if arr[i] < arr[j]:
            temp = arr[j]
            arr[j], arr[minindex]= arr[minindex], temp
            print arr

    return arr

alo = [4,5,8,1,7,6,-2,9,1,3]

print sort(alo)
