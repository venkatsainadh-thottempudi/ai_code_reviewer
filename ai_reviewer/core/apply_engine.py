from ai_reviewer.utils.file_scanner import scan_python_files
from ai_reviewer.core.parser import CodeParser
from ai_reviewer.core.docstring_generator import generate_docstring
from ai_reviewer.core.autofix import insert_docstring_into_source


def run_apply(directory, style="google"):
    files = scan_python_files(directory, exclude=["venv", "__pycache__"])

    for file in files:
        parser = CodeParser(file)
        parser.parse()

        functions = parser.extract_functions()

        updated_source = parser.source_code
        modified = False

        for func in reversed(functions):
            if not func["docstring"]:
                generated = generate_docstring(func, style=style)
                updated_source = insert_docstring_into_source(
                    updated_source,
                    func,
                    generated
                )
                modified = True

        if modified:
            with open(file, "w", encoding="utf-8") as f:
                f.write(updated_source)

            print(f"✔ Updated: {file}")
        else:
            print(f"✓ No changes needed: {file}")