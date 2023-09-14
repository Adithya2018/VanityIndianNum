import pandas as pd

def clean_vanity_rule_book(vanity_rule_df):

    vanity_rule_df.rename(columns=lambda x: x.strip(), inplace=True)
    
    # to sort by proposed rate
    sorted_df = vanity_rule_df.sort_values(by=['Proposed new rate'],
                                                            ascending=False)
    
    return sorted_df
    