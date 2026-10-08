def retirement(start_age, initial_savings, working_info, retired_info):
    """
    Prints the current status of an individual's retirement account.
    The dictionaries both have these fields: 
       "months","contribution","rate_of_return"

    Args:
       start_age (int): At what age (in months) does the individual start
       initial_savings (float): initial savings in dollars
       working_info (dict): information about working
       retired_into (dict): information about retirement

    Returns:
    None
    """
    def money(info, savings):
        rate = info["rate_of_return"]
        return info["contribution"] + savings * (1 + rate)
    savings = initial_savings
   
    for month in range(start_age, start_age + working_info["months"] + retired_info["months"]):
        age = month // 12
        last = month % 12
        print(f"Age {age:3d} month {last:2d} you have ${savings:,.2f}")
        if month < working_info["months"] + start_age:
            savings = money(working_info, savings)
        else:
            savings = money(retired_info, savings)  
            

if __name__ == "__main__":
    working_info = {
        "months": 489,
        "contribution": 1000,
        "rate_of_return": 0.045 / 12
    }

    retired_info = {
        "months": 384,
        "contribution": -4000,
        "rate_of_return": 0.01 / 12
    }

    retirement(327, 21345, working_info, retired_info)

       




   
   
   
   
   
    




