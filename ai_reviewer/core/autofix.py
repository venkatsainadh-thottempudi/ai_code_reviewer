def insert_docstring_into_source(source_code, function_info, docstring):
    lines = source_code.split("\n")

    # Insert after function definition line
    insert_index = function_info["line_number"]

    # Detect indentation level from function definition
    def_line = lines[function_info["line_number"] - 1]
    indent_level = len(def_line) - len(def_line.lstrip())
    indent = " " * (indent_level + 4)

    indented_docstring = "\n".join(
        indent + line if line else "" for line in docstring.split("\n")
    )

    lines.insert(insert_index, indented_docstring)

    return "\n".join(lines)