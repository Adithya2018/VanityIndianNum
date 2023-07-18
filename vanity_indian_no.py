from typing import Tuple
import pandas as pd
import numpy as np
import re

class VanityIndianNo:
    """
        Vanity Numbers for Indian Mobile Numbers
    """
    
    def __init__(self, phone_no, vanity_check_level_cost_df):
        self.level = 'Normal'
        self.rate = 0
        self.phone_no = phone_no
        self.vanity_check_level_cost_df = vanity_check_level_cost_df

    def is_valid_no(self) -> bool:
        """
            checks if no is valid
            :returns: boolean, based on valid or invalid
        """
        if len(self.phone_no) == 10:
            return True
        else:
            return False
        
    def pattern_check(self) -> Tuple[str, int]:
        """
            Checks if phone no matches a specific pattern
            and returns the level and rate of the vanity phone number
            :returns: level and rate of phone number
        """
        print(self.vanity_check_level_cost_df)



        return self.level, self.rate