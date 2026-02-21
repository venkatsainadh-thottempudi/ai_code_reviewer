def determine_severity(function, complexity_value):
    if not function["docstring"]:
        return "WARNING"

    if complexity_value > 10:
        return "CRITICAL"
    elif complexity_value > 5:
        return "WARNING"
    else:
        return "INFO"