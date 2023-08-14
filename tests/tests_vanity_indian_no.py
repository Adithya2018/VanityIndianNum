import pytest

from VanityIndianNum.vanity_indian_no import VanityIndianNo as vin


def test_is_valid_no():
    """ Checks if the no is valid """
    expected_answers = [False, True]
    actual_answers = [vin.is_valid_no('2342343242323543'), vin.is_valid_no('9447231411')]
    assert expected_answers == actual_answers
