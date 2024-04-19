Goliath        = 666*'666'
GoliathAmount = len(Goliath)
def ExpensiveGoliathCheck(i):
    Number          = (1<<i)
    ContainsGoliath = Goliath in str(Number)
    return ContainsGoliath


def f(Queue):
    while True:
        i      = Queue.get()
        Result = ExpensiveGoliathCheck(i)
        print(Result)