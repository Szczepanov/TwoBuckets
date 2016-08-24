from sys import stdin

# You have two buckets of x (smallBucketVolume) liters and y (bigBucketVolume) liters.
#
# How can you measure exactly z (litersToMeasure) liters ?

smallBucketVolume = 0
bigBucketVolume = 0
litersToMeasure = 0

while True:
    print('Enter volume of a small bucket in liters: ')
    smallBucketVolume = abs(int(stdin.readline()))
    print('Enter volume of a big bucket in liters: ')
    bigBucketVolume = abs(int(stdin.readline()))
    if smallBucketVolume < bigBucketVolume:
        break
    else:
        print('Small bucket needs to be larger than big bucket.')

print('Enter how many liters to measure: ')
while True:
    litersToMeasure = abs(int(stdin.readline()))
    if litersToMeasure <= bigBucketVolume:
        break
    else:
        print('Too many liters to measure.')

if litersToMeasure == bigBucketVolume | litersToMeasure == smallBucketVolume:
    print('Liters to measure equals volume of either small or big bucket.')
    exit(0)
# the logic
else:
    bigBucketVolumeFinal = 0
    stepsCount = 0
    while True:
        print('Step no:%s Volume of the big bucket:%s ' % (str(stepsCount), str(bigBucketVolumeFinal)))
        if litersToMeasure == bigBucketVolumeFinal:
            print('Measuring %s liters was done in %s steps' % (
                str(litersToMeasure), str(stepsCount)))
            exit(0)
        else:
            stepsCount += 1
            bigBucketVolumeFinal = (stepsCount * smallBucketVolume) % bigBucketVolume
    exit(0)
exit(0)
