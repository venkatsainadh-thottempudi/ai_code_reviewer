import ast


class CodeParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = None
        self.source_code = None

    def parse(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            self.source_code = f.read()

        self.tree = ast.parse(self.source_code)
        return self.tree

    def extract_functions(self):
        functions = []

        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                function_info = {
                    "name": node.name,
                    "args": [arg.arg for arg in node.args.args],
                    "docstring": ast.get_docstring(node),
                    "line_number": node.lineno,
                }
                functions.append(function_info)

        return functions

    def extract_classes(self):
        classes = []

        for node in ast.walk(self.tree):
            if isinstance(node, ast.ClassDef):
                class_info = {
                    "name": node.name,
                    "docstring": ast.get_docstring(node),
                    "line_number": node.lineno,
                }
                classes.append(class_info)

        return classes