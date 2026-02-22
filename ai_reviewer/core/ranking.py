def determine_severity(function, complexity_value):
    """
    Determine_severity function.

    Args:
        function (type): Description of function.
        complexity_value (type): Description of complexity_value.

    Returns:
        type: Description of return value.
    """
    if not function["docstring"]:
        return "WARNING"

    if complexity_value > 10:
        return "CRITICAL"
    elif complexity_value > 5:
        return "WARNING"
    else:
        return "INFO"