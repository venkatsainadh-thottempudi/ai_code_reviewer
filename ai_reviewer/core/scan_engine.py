from concurrent.futures import ThreadPoolExecutor
from ai_reviewer.utils.file_scanner import scan_python_files
from ai_reviewer.config.config_loader import load_config
from ai_reviewer.core.validator import run_pydocstyle
from ai_reviewer.core.complexity import analyze_complexity
from ai_reviewer.core.ranking import determine_severity
from ai_reviewer.core.parser import CodeParser
from ai_reviewer.core.metrics import calculate_docstring_coverage
import time
from ai_reviewer.core.cache import (
    calculate_file_hash,
    load_cache,
    save_cache
)


# 🔹 Process a single file
def process_file(file):
    """
    Process_file function.

    Args:
        file (type): Description of file.

    Returns:
        type: Description of return value.
    """
    parser = CodeParser(file)
    parser.parse()

    functions = parser.extract_functions()
    complexity_data = analyze_complexity(parser.source_code)
    style_issues = run_pydocstyle(file)

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

    coverage = calculate_docstring_coverage(functions)

    return {
        "file": file,
        "functions": len(functions),
        "coverage": coverage,
        "issues": file_issues,
        "style_issues": style_issues,
        "documented": sum(1 for f in functions if f["docstring"]),
        "total": len(functions)
    }


# 🔹 Main scan function
def run_scan(directory):
    """
    Run_scan function.

    Args:
        directory (type): Description of directory.

    Returns:
        type: Description of return value.
    """
    start_time = time.time()

    config = load_config()
    exclude_dirs = config.get("exclude", ["venv", "__pycache__"])

    files = scan_python_files(directory, exclude=exclude_dirs)

    cache = load_cache()
    new_cache = {}

    results = []
    total_functions = 0
    documented_functions = 0
    file_results = []

    cache_hits = 0
    processed_files = 0

    with ThreadPoolExecutor() as executor:
        futures = []

        for file in files:
            file_hash = calculate_file_hash(file)

            if file in cache and cache[file]["hash"] == file_hash:
                file_results.append(cache[file]["result"])
                new_cache[file] = cache[file]
                cache_hits += 1
            else:
                futures.append((file, file_hash))

        processed = list(
            executor.map(
                lambda x: (x[0], x[1], process_file(x[0])),
                futures
            )
        )

        for file, file_hash, result in processed:
            file_results.append(result)
            new_cache[file] = {
                "hash": file_hash,
                "result": result
            }
            processed_files += 1

    save_cache(new_cache)

    for result in file_results:
        results.append({
            "file": result["file"],
            "functions": result["functions"],
            "coverage": result["coverage"],
            "issues": result["issues"],
            "style_issues": result["style_issues"]
        })

        total_functions += result["total"]
        documented_functions += result["documented"]

    overall_coverage = 0
    if total_functions > 0:
        overall_coverage = round(
            (documented_functions / total_functions) * 100,
            2
        )

    duration = round(time.time() - start_time, 2)

    print(f"\n Scan Summary:")
    print(f"   Total Files: {len(files)}")
    print(f"   Processed Files: {processed_files}")
    print(f"   Cache Hits: {cache_hits}")
    print(f"   Scan Time: {duration} seconds")

    return results, overall_coverage