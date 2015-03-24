l=['07895462130','919875641230','9195969878']

def formatNumber(func):
    def replace (list_of_numbers):
        return func([ '+91'+x[-10:] for x in list_of_numbers])
    return replace

@formatNumber
def printnumbers(l):
    for x in l :
        print x

printnumbers(l)


