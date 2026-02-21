from ai_reviewer.core.parser import CodeParser
from ai_reviewer.core.docstring_generator import generate_google_docstring
from ai_reviewer.core.autofix import insert_docstring_into_source

file_path = "examples/sample.py"

parser = CodeParser(file_path)
parser.parse()

functions = parser.extract_functions()

updated_source = parser.source_code

for func in functions:
    if not func["docstring"]:
        generated = generate_google_docstring(func)
        updated_source = insert_docstring_into_source(updated_source, func, generated)

print("\nUpdated Source Code:\n")
print(updated_source)