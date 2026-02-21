from ai_reviewer.utils.file_scanner import scan_python_files
from ai_reviewer.core.parser import CodeParser
from ai_reviewer.core.metrics import calculate_docstring_coverage
from ai_reviewer.core.complexity import analyze_complexity
from ai_reviewer.core.ranking import determine_severity
from ai_reviewer.core.validator import run_pydocstyle

def run_scan(directory):
    files = scan_python_files(directory, exclude=["venv", "__pycache__"])

    total_functions = 0
    documented_functions = 0

    results = []

    for file in files:
        parser = CodeParser(file)
        style_issues = run_pydocstyle(file)
        parser.parse()

        functions = parser.extract_functions()
        complexity_data = analyze_complexity(parser.source_code)

        total_functions += len(functions)
        documented_functions += sum(1 for f in functions if f["docstring"])

        coverage = calculate_docstring_coverage(functions)

        file_issues = []

        for func in functions:
            complexity_value = next(
                (c["complexity"] for c in complexity_data if c["name"] == func["name"]),
                1
            )

            severity = determine_severity(func, complexity_value)

            file_issues.append({
                "function": func["name"],
                "complexity": complexity_value,
                "docstring": bool(func["docstring"]),
                "severity": severity
            })

        results.append({
            "file": file,
            "functions": len(functions),
            "coverage": coverage,
            "issues": file_issues,
            "style_issues": style_issues
        })

    overall_coverage = 0
    if total_functions > 0:
        overall_coverage = round((documented_functions / total_functions) * 100, 2)

    return results, overall_coverage