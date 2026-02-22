def generate_html_report(results, overall):
    """
    Generate_html_report function.

    Args:
        results (type): Description of results.
        overall (type): Description of overall.

    Returns:
        type: Description of return value.
    """
    html = f"""
    <html>
    <head>
        <title>AI Code Review Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1 {{ color: #2c3e50; }}
            h2 {{ color: #34495e; }}
            table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; }}
            th {{ background-color: #f4f4f4; }}
            .critical {{ color: red; font-weight: bold; }}
            .warning {{ color: orange; font-weight: bold; }}
            .info {{ color: green; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>AI Code Review Report</h1>
        <h2>Overall Coverage: {overall}%</h2>
    """

    for result in results:
        html += f"<h3>File: {result['file']}</h3>"
        html += f"<p>Functions: {result['functions']}</p>"
        html += f"<p>Coverage: {result['coverage']}%</p>"

        html += """
        <table>
            <tr>
                <th>Function</th>
                <th>Complexity</th>
                <th>Docstring</th>
                <th>Severity</th>
            </tr>
        """

        for issue in result["issues"]:
            severity_class = issue["severity"].lower()

            html += f"""
            <tr>
                <td>{issue['function']}</td>
                <td>{issue['complexity']}</td>
                <td>{issue['docstring']}</td>
                <td class="{severity_class}">{issue['severity']}</td>
            </tr>
            """

        html += "</table>"

        if result["style_issues"]:
            html += "<h4>Style Issues:</h4><ul>"
            for style_issue in result["style_issues"]:
                html += f"<li>{style_issue}</li>"
            html += "</ul>"

    html += "</body></html>"

    return html