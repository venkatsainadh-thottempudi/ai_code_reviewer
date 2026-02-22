import subprocess


def run_pydocstyle(file_path):
    """
    Run_pydocstyle function.

    Args:
        file_path (type): Description of file_path.

    Returns:
        type: Description of return value.
    """
    try:
        result = subprocess.run(
            ["pydocstyle", file_path],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()

        if not output:
            return []

        return output.split("\n")

    except Exception as e:
        return [f"Error running pydocstyle: {str(e)}"]