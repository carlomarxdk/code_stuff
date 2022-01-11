def sum_nested(lst):
    return sum(sum_nested(i) if isinstance(i, list) else i for i in lst)