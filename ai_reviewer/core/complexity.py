from radon.complexity import cc_visit


def analyze_complexity(source_code):
    """
    Analyze_complexity function.

    Args:
        source_code (type): Description of source_code.

    Returns:
        type: Description of return value.
    """
    results = cc_visit(source_code)

    complexity_data = []

    for item in results:
        complexity_data.append({
            "name": item.name,
            "complexity": item.complexity,
            "line_number": item.lineno,
        })

    return complexity_data