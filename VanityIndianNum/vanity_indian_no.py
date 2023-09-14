from typing import Tuple

import numpy as np
from  data_cleaning import clean_vanity_rule_book


class VanityIndianNo:
    """
        Vanity Numbers for Indian Mobile Numbers
    """

    def __init__(self, phone_no, vanity_check_level_cost_df):
        self.level = 'Normal'
        self.rate = 0
        self.phone_no = phone_no
        self.vanity_check_level_cost_df = vanity_check_level_cost_df

    @staticmethod
    def is_valid_no(phone_no) -> bool:
        """
            checks if number is valid
            :returns: boolean, based on valid or invalid
        """
        if len(phone_no) == 10:
            return True
        else:
            return False
        
    @staticmethod
    def last_n_digits_identical(is_odd: bool):
        """

        :param is_odd:
        :return:
        """

        pass

    def pattern_check(self) -> Tuple[str, int]:
        """
            Checks if phone no matches a specific pattern
            and returns the level and rate of the vanity phone number
            :returns: level and rate of phone number
        """

        cleaned_df = clean_vanity_rule_book(self.vanity_check_level_cost_df)

        for index, check in enumerate(cleaned_df['Function Name']):
            if check is not np.NAN:
                if check == 'last_n_digits_identical':

                    if cleaned_df['Odd/Even Selection'][index] == 'Odd':
                        self.last_n_digits_identical(True)
                    
                    elif cleaned_df['Odd/Even Selection'][index] == 'Even':
                        self.last_n_digits_identical(False)

        return self.level, self.rate

    