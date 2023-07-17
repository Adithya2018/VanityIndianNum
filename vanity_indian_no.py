from typing import Tuple
import pandas as pd
import numpy as np
import re

class VanityIndianNo:
    """
        Vanity Numbers for Indian Mobile Numbers
    """

    def __init__(self):
        self.phone_no = '0000000000'
    
    def __init__(self, phone_no):
        self.phone_no = phone_no

    def is_valid_no(self, phone_no: str) -> bool:
        """
            checks if no is valid
            :param phone_no: str, Phone number to check
            :returns: boolean, based on valid or invalid
        """
        if len(phone_no) == 10:
            return True
        else:
            return False
        
    def pattern_check(self, phone_no: str) -> Tuple[str, int]:
        """
            Checks if phone no matches a specific pattern
            and returns the level and rate of the vanity phone number
            :param phone_no: str, Phone number to pattern check
            :returns: level and rate of phone number
        """
        level = 'Normal'
        rate = 0



        return level, rate