def calculate_docstring_coverage(functions):
    """
    Calculate_docstring_coverage function.

    Args:
        functions (type): Description of functions.

    Returns:
        type: Description of return value.
    """
    if not functions:
        return 100.0

    documented = sum(1 for f in functions if f["docstring"])
    total = len(functions)

    coverage = (documented / total) * 100
    return round(coverage, 2)