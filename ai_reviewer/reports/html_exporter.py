from datetime import datetime


def generate_html_report(results, overall_coverage, output_file="ai_review_report.html"):
    html_content = f"""
    <html>
    <head>
        <title>AI Code Review Report</title>
        <style>
            body {{ font-family: Arial; padding: 20px; }}
            h1 {{ color: #2c3e50; }}
            table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
            .CRITICAL {{ color: red; font-weight: bold; }}
            .WARNING {{ color: orange; font-weight: bold; }}
            .INFO {{ color: green; }}
        </style>
    </head>
    <body>

    <h1>AI Code Review Report</h1>
    <p><strong>Date:</strong> {datetime.now()}</p>
    <p><strong>Overall Coverage:</strong> {overall_coverage}%</p>
    """

    for result in results:
        html_content += f"""
        <h2>File: {result['file']}</h2>
        <p>Functions: {result['functions']}</p>
        <p>Coverage: {result['coverage']}%</p>

        <table>
            <tr>
                <th>Function</th>
                <th>Complexity</th>
                <th>Docstring</th>
                <th>Severity</th>
            </tr>
        """

        for issue in result["issues"]:
            html_content += f"""
            <tr>
                <td>{issue['function']}</td>
                <td>{issue['complexity']}</td>
                <td>{issue['docstring']}</td>
                <td class="{issue['severity']}">{issue['severity']}</td>
            </tr>
            """

        html_content += "</table>"

    html_content += """
    </body>
    </html>
    """

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✔ HTML report generated: {output_file}")