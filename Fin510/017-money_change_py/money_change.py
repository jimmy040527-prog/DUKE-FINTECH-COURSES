def make_change(amount):
    '''
    The possible denominations are 100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00,
    0.25, 0.10, 0.05, and 0.01.
    '''
    res = {}
    # for integer
    int_deno = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00]
    for id in int_deno:
        count = amount // id
        if count > 0:
            res[id] = int(count)       
        amount = amount % id

    # for decimals
    dec_deno = [0.25, 0.10, 0.05, 0.01]
    amount = round(amount * 100)
    for dd in dec_deno:
        count = amount // (dd * 100)
        if count > 0:
            res[dd] = int(count)
        amount = amount % (dd * 100)

    return res


def print_change(change):
    '''
    Print each denomination and its count.
    '''
    for key, value in change.items():
        print(f"${key:.2f}: {value}")

