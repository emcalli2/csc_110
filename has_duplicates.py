def has_duplicates(*values):
    control = set()
    for v in values:
        if v in control:
            return True
        control.add(v)
    return False