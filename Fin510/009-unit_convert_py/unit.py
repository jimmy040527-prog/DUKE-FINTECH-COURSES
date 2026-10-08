def convert_mass(value, current, target):
    '''
    convert mass from a unit to another
    '''
    unit_dic = {'Kilogram': 1.0, 
                'Pound': 0.453592,
                'Stone': 6.35029, 
                'Jin': 0.5,
                'Seer': 1.25,
                'Gram': 0.001,
                'Oka': 1.2829}
    convert_value = value * unit_dic[current] / unit_dic[target]
    return convert_value

   