def first_non_repeating_letter(string:str) -> str:
    if len(string) == 0:
        return string
    char_set = set()
    for c in string.lower():
        if c not in char_set:
            if string.lower().count(c) == 1:
                indx = string.lower().index(c)
                return string[indx]
        char_set.update(c)
    return ""