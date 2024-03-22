#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    mkey = list(a_dictionary.keys)[0]
    mvalue = a_dictionary[mkey]
    for k, v in a_dictionary.items():
        if v > mvalue:
            mkey = k
            mvalue = v
    return mkey
