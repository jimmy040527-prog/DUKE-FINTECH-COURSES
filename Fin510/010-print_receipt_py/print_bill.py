def print_receipt(subtotal, tax_rate, tip_rate):
    '''
    A function to print your receipt
    '''
    tax = tax_rate * subtotal
    tip = tip_rate * subtotal
    total = subtotal + tax + tip
    print(f'Subtotal: ${subtotal:10.2f}\n'
          f'     Tax: ${tax:10.2f}\n'
          f'     Tip: ${tip:10.2f}\n'
          f'           ==========\n'
          f'   Total: ${total:10.2f}')