import pandas as pd
import numpy as np

class VanityIndianNo:
    """

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
        
    def pattern_check(self, phone_no: str) -> bool:
        """
            Checks if it matches a specific pattern 
        """

        return True