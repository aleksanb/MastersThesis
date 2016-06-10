optimumsP3 = [(5, 10), (10, 20), (15, 30), (15, 40), (30, 50), (30, 60), (40, 70), (50, 80), (50, 90), (55, 100)]

optimumsP5 = [(15, 30), (20, 40), (20, 50), (30, 60), (30, 70), (40, 80), (45, 90), (50, 100), (55, 110), (60, 120), (70, 130), (70, 140)]

optimumsD3 = [(2, 5), (5, 10), (5, 15), (10, 20), (10, 25), (15, 30)]
optimumsD5 = [(5, 10), (5, 15), (10, 20), (10, 25), (15, 30), (15, 35), (15, 40), (20, 45), (25, 50), (25, 55), (25, 60), (30, 65)]

def average(optimums):
    percentages = [a/b for a,b in optimums]
    return sum(percentages) / len(percentages)

#print("OptimumP3", average(optimumsP3))
#print("OptimumP5", average(optimumsP5))
#print("OptimumD3", average(optimumsD3))
#print("OptimumD5", average(optimumsD5))

#for (a,b) in optimumsP5:
#    print "% {} of {}".format(a,b)
#
#for a in map(lambda (x,y): (x/5, y), optimumsP5):
#    print a

for i in range(5, 145, 5):
    p3 = filter(lambda (x,y): y==i, optimumsP3)
    p5 = filter(lambda (x,y): y==i, optimumsP5)
    d3 = filter(lambda (x,y): y==i, optimumsD3)
    d5 = filter(lambda (x,y): y==i, optimumsD5)

    nums = [str(i)]

    for arr in [p3, p5, d3, d5]:
        if arr:
            nums.append(str(arr[0][0]))
        else:
            nums.append("-")

    print " & ".join(nums) + "\\\\"
