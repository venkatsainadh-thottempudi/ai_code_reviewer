def generate_docstring(function_info, style="google"):
    """
    Generate_docstring function.

    Args:
        function_info (type): Description of function_info.
        style (type): Description of style.

    Returns:
        type: Description of return value.
    """
    name = function_info["name"]
    args = function_info["args"]

    if style == "google":
        return generate_google(name, args)
    elif style == "numpy":
        return generate_numpy(name, args)
    elif style == "rest":
        return generate_rest(name, args)
    else:
        return generate_google(name, args)


def generate_google(name, args):
    """
    Generate_google function.

    Args:
        name (type): Description of name.
        args (type): Description of args.

    Returns:
        type: Description of return value.
    """
    doc = '"""\n'
    doc += f"{name.capitalize()} function.\n\n"

    if args:
        doc += "Args:\n"
        for arg in args:
            doc += f"    {arg} (type): Description of {arg}.\n"
        doc += "\n"

    doc += "Returns:\n"
    doc += "    type: Description of return value.\n"
    doc += '"""'
    return doc


def generate_numpy(name, args):
    """
    Generate_numpy function.

    Args:
        name (type): Description of name.
        args (type): Description of args.

    Returns:
        type: Description of return value.
    """
    doc = '"""\n'
    doc += f"{name.capitalize()} function.\n\n"

    if args:
        doc += "Parameters\n"
        doc += "----------\n"
        for arg in args:
            doc += f"{arg} : type\n"
            doc += f"    Description of {arg}.\n"
        doc += "\n"

    doc += "Returns\n"
    doc += "-------\n"
    doc += "type\n"
    doc += "    Description of return value.\n"
    doc += '"""'
    return doc


def generate_rest(name, args):
    """
    Generate_rest function.

    Args:
        name (type): Description of name.
        args (type): Description of args.

    Returns:
        type: Description of return value.
    """
    doc = '"""\n'
    doc += f"{name.capitalize()} function.\n\n"

    for arg in args:
        doc += f":param {arg}: Description of {arg}\n"
        doc += f":type {arg}: type\n"

    doc += "\n:returns: Description of return value\n"
    doc += ":rtype: type\n"
    doc += '"""'
    return doc