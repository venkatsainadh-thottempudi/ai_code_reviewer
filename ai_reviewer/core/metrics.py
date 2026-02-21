def calculate_docstring_coverage(functions):
    if not functions:
        return 100.0

    documented = sum(1 for f in functions if f["docstring"])
    total = len(functions)

    coverage = (documented / total) * 100
    return round(coverage, 2)