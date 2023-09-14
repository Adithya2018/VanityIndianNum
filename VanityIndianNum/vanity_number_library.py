import pandas as pd

from vanity_indian_no import VanityIndianNo

if __name__ == '__main__':
    
    # Taking the rule book for Vanity Check as input
    vanity_check_level_cost_df = pd.read_excel("../Data/Vanity_Check_bsnl_cost.xlsx", sheet_name='Sheet1')

    # Taking phone numbers as input from workbook
    input_phone_nos_df = pd.read_excel("../Data/vanity check.xlsx", sheet_name='Input_Sheet')
    
    for input_phone_no in input_phone_nos_df['External_id']:

        vn = VanityIndianNo(str(input_phone_no), vanity_check_level_cost_df)

        if vn.is_valid_no(vn.phone_no):
            level, rate = vn.pattern_check()
            print(f'Level = {level}; Rate = ₹{rate}')
            break
        else:
            print("Enter a valid Number")
