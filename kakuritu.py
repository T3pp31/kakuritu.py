import numpy

def cointoss(try_count, length):
    x=0
    prev_ret = None
    for _ in range(try_count):

        ret = numpy.random.randint(0,2)
        if prev_ret == ret:
            x+=1
            if x>= length:
                return True

        else:
            prev_ret =ret
            x=1
    return False

def monte_carlo(try_count):
    x = 0.0
    y = 0.0
    for _ in range(try_count):
        if cointoss(100,10):
            x+=1
        y+=1
    return 100.0 * x/y

print("100:{0}%".format(monte_carlo(100)))
print("1000:{0}%".format(monte_carlo(1000)))
print("10000:{0}%".format(monte_carlo(10000)))
print("100000:{0}%".format(monte_carlo(100000)))
print("10000000000:{0}%".format(monte_carlo(10000000000)))

open_file = open("kakuritu.txt", "a")
open_file.write("100:{0}%\n".format(monte_carlo(100)))
open_file.write("1000:{0}%\n".format(monte_carlo(1000)))
open_file.write("10000:{0}%\n".format(monte_carlo(10000)))
open_file.write("100000:{0}%\n".format(monte_carlo(100000)))
open_file.write("10000000000:{0}%\n".format(monte_carlo(10000000000)))
open_file.close()
