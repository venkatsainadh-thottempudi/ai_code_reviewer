def insert_docstring_into_source(source_code, function_info, docstring):
    """
    Insert_docstring_into_source function.

    Args:
        source_code (type): Description of source_code.
        function_info (type): Description of function_info.
        docstring (type): Description of docstring.

    Returns:
        type: Description of return value.
    """
    lines = source_code.split("\n")

    # Function definition starts here
    def_line_index = function_info["line_number"] - 1

    # Find where the function header actually ends (where ":" is)
    header_end_index = def_line_index
    while header_end_index < len(lines):
        if lines[header_end_index].strip().endswith(":"):
            break
        header_end_index += 1

    # Determine indentation level
    def_line = lines[def_line_index]
    indent_level = len(def_line) - len(def_line.lstrip())
    indent = " " * (indent_level + 4)

    # Properly indent docstring
    indented_docstring = "\n".join(
        indent + line if line else "" for line in docstring.split("\n")
    )

    # Insert AFTER header end
    insert_index = header_end_index + 1
    lines.insert(insert_index, indented_docstring)

    return "\n".join(lines)