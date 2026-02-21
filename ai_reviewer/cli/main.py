import typer
import sys
from ai_reviewer.core.scan_engine import run_scan
from ai_reviewer.core.apply_engine import run_apply 
from ai_reviewer.reports.html_exporter import generate_html_report

app = typer.Typer()


@app.command()
def scan(
    path: str,
    min_coverage: float = typer.Option(
        0,
        help="Minimum required docstring coverage percentage"
    )
):
    results, overall = run_scan(path)

    for result in results:
        print(f"\nFile: {result['file']}")
        print(f"Functions: {result['functions']}")
        print(f"Coverage: {result['coverage']}%")

        print("\nIssues:")
        for issue in result["issues"]:
            print(
                f"  {issue['function']} | "
                f"Complexity: {issue['complexity']} | "
                f"Docstring: {issue['docstring']} | "
                f"Severity: {issue['severity']}"
            )
            print("\nPEP 257 Style Issues:")
            if result["style_issues"]:
                for issue in result["style_issues"]:
                    print(f"  {issue}")
            else:
                print("  ✓ No style issues")

    print("\n----------------------------")
    print(f"Overall Coverage: {overall}%")

    # 🔥 Quality Gate Enforcement
    if overall < min_coverage:
        print(
            f"\n❌ Coverage below required threshold ({min_coverage}%)."
        )
        sys.exit(1)
    else:
        print("\n✅ Coverage requirement satisfied.")
        from ai_reviewer.core.apply_engine import run_apply


@app.command()
def apply(
    path: str,
    style: str = typer.Option(
        "google",
        help="Docstring style: google | numpy | rest"
    )
):
    """
    Auto-generate and insert missing docstrings.
    """
    run_apply(path, style=style)

@app.command()
def report(path: str):
    """
    Generate HTML report for code analysis.
    """
    results, overall = run_scan(path)
    generate_html_report(results, overall)


if __name__ == "__main__":
    app()