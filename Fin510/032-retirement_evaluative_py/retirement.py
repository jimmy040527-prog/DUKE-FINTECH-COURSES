import sys


def validate_arguments(start_date, end_date):
    try:
        # split the start date into year and month
        start_year, start_month = start_date.split('.')
        # check the date format
        if len(start_month) != 2 or len(start_year) != 4:
            raise ValueError("Wrong date format")
        # convert into integers
        start_year = int(start_year)
        start_month = int(start_month)
    except ValueError:
        raise ValueError('Your start date format is not correct')
    try:
        end_year, end_month = end_date.split('.')
        if len(end_month) != 2 or len(end_year) != 4:
            raise ValueError("Wrong date format")
        end_year = int(end_year)
        end_month = int(end_month)
    except ValueError:
        raise ValueError('Your end date format is not correct')
    # validate the end date and start date
    if start_month < 1 or start_month > 12:
        raise ValueError('start month is not correct')
    if end_month < 1 or end_month > 12:
        raise ValueError('end month is not correct')
    if end_year < start_year:
        raise ValueError('end date can not be earlier than start date')
    if end_year == start_year and end_month < start_month:
        raise ValueError('end date can not be earlier than start date')
    
    
def read_sp_data(filename):
    # # create a dictionary to store sp data
    sp_data = {}

    try:
        with open(filename, 'r') as file:
            # skip the header
            next(file)

            for line in file:
                # split each row into three fields
                sp = line.strip().split(",", 2)
                if len(sp) != 3:
                    raise ValueError('sp_data got sth wrong')
                try:
                    date = sp[0]
                    # convert index level and dividend to numbers
                    index_level = float(sp[1])
                    dividend = float(sp[2])
                except ValueError:
                    raise ValueError("sp_data has error")
                sp_data[date] = [index_level, dividend]
    except FileNotFoundError:
        raise ValueError('File can not be found')

    return sp_data    


def read_bond_data(filename):
    # create a dict to store bond data
    bond_data = {}

    try:
        with open(filename, 'r') as file:
            # skip the header
            next(file)

            for line in file:
                bond = line.strip().split(",", 1)
                if len(bond) != 2:
                    raise ValueError('bond_data got sth wrong')
                try:
                    date = bond[0]
                    # convert the bond rate to a number
                    bondrate = float(bond[1])
                except ValueError:
                    raise ValueError("bond_data has error")
                bond_data[date] = bondrate
    except FileNotFoundError:
        raise ValueError('File can not be found')
    return bond_data  


def calculate_ror(date, sp_data, bond_data):
    # process date
    year, month = date.split(".")
    year = int(year)
    month = int(month)
    if month == 1:
        prev_month = 12
        prev_year = year - 1
    else:
        prev_month = month - 1
        prev_year = year
    prev = f"{prev_year}.{prev_month:02d}"

    # prepare data we need
    cur_index_level = sp_data[date][0]
    cur_dividend = sp_data[date][1]
    cur_bond_rate = bond_data[date]
    prev_index_level = sp_data[prev][0]

    # calculating stock_ror
    sp_ror = cur_index_level / prev_index_level - 1
    dividend_ror = (cur_dividend / 12) / cur_index_level
    stock_ror = sp_ror + dividend_ror

    # calculating bond ror
    bond_ror = cur_bond_rate / 12 / 100

    return stock_ror, bond_ror


def strategy1(start_date, end_date, sp_data, bond_data):
    balance = 0
    deposit = 100
    cur_date = start_date
    year, month = cur_date.split(".")
    year = int(year)
    month = int(month)
    end_year, end_month = end_date.split(".")
    end_year = int(end_year)
    end_month = int(end_month)
    balance_record = {}

    while (year, month) <= (end_year, end_month):
        # get cur_stock_ror
        stock_ror = calculate_ror(cur_date, sp_data, bond_data)[0]
        balance = balance * (1 + stock_ror) + deposit
        balance_record[cur_date] = balance
        # iterate the cur_date
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
        cur_date = f"{year}.{month:02d}"
        if month == 1:
            # update deposit if January
            deposit *= 1.025
    return balance_record


def strategy2(start_date, end_date, sp_data, bond_data):
    balance = 0
    deposit = 100
    cur_date = start_date
    year, month = cur_date.split(".")
    year = int(year)
    month = int(month)
    end_year, end_month = end_date.split(".")
    end_year = int(end_year)
    end_month = int(end_month)
    balance_record = {}

    while (year, month) <= (end_year, end_month):
        bond_ror = calculate_ror(cur_date, sp_data, bond_data)[1]
        balance = balance * (1 + bond_ror) + deposit
        balance_record[cur_date] = balance
        # update cur_date
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
        cur_date = f"{year}.{month:02d}"
        if month == 1:
            # update deposit if Jan
            deposit *= 1.025
    return balance_record


def strategy3(start_date, end_date, sp_data, bond_data):
    balance = 0
    deposit = 100
    allocation = 1.00
    cur_date = start_date
    year, month = cur_date.split(".")
    year = int(year)
    month = int(month)
    end_year, end_month = end_date.split(".")
    end_year = int(end_year)
    end_month = int(end_month)
    balance_record = {}

    while (year, month) <= (end_year, end_month):
        pack = calculate_ror(cur_date, sp_data, bond_data)
        stock_ror = pack[0] 
        bond_ror = pack[1]
        balance = allocation * balance * (1 + stock_ror) + (1 - allocation) * balance * (1 + bond_ror) + deposit
        balance_record[cur_date] = balance
        # update cur_date
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
        cur_date = f"{year}.{month:02d}"
        # update deposit and allocation
        if month == 1:
            deposit *= 1.025
            allocation -= 0.02
    return balance_record


def write_output(strategy1_record, strategy2_record, strategy3_record):
    # write portfolio.csv 
    with open('portfolio.csv', "w") as file:
        # header
        file.write('Date,StrategyOne,StrategyTwo,StrategyThree\n')
        # get value from strategies
        for date in strategy1_record:
            balance1 = strategy1_record[date]
            balance2 = strategy2_record[date]
            balance3 = strategy3_record[date]
            row = f'{date},{balance1:.2f},{balance2:.2f},{balance3:.2f}\n'
            file.write(row)


if __name__ == "__main__":
    # verify 5 arg
    if len(sys.argv) != 5:
        sys.exit(10)
    sp_filename = sys.argv[1]
    bond_filename = sys.argv[2]
    start_date = sys.argv[3]
    end_date = sys.argv[4]
    # verify date
    try:
        validate_arguments(start_date, end_date)
    except ValueError:
        sys.exit(10)
    # verify read sp data
    try:
        sp_data = read_sp_data(sp_filename)
    except ValueError:
        sys.exit(20)
    # verify read bond data
    try:
        bond_data = read_bond_data(bond_filename)
    except ValueError:
        sys.exit(30)
    # calculate balance for all 3 strategies
    record1 = strategy1(start_date, end_date, sp_data, bond_data)
    record2 = strategy2(start_date, end_date, sp_data, bond_data)
    record3 = strategy3(start_date, end_date, sp_data, bond_data)

    write_output(record1, record2, record3)



    



