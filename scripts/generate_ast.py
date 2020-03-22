#!/usr/local/bin/python3
import sys
from typing import List
from tyfile import tyfile

TAB_SIZE = 4
# T is Tab but since it's use so often keep it short
T = " " * TAB_SIZE


def define_ast(output_dir: str, base_name: str, types: List[str]):
    path = f"{output_dir}/{base_name}.java"
    writer = tyfile(path, mode="w+", encoding="utf-8")

    writer.writeln("package com.tykowale.lox;")
    writer.writeln()
    writer.writeln("import java.util.List;")
    writer.writeln()
    writer.writeln(f"public abstract class {base_name} {{")

    # the ast classes
    for type in types:
        class_name = type.split(":")[0].strip()
        fields = type.split(":")[1].strip()
        define_type(writer, base_name, class_name, fields)

    writer.writeln("}")
    writer.close()


def define_type(writer: tyfile, base_name: str, class_name: str, field_list: str):
    writer.writeln(f"{T}static class {class_name} extends {base_name} {{")

    # constructor
    writer.writeln(f"{T}{T}{class_name}({field_list}) {{")

    # store parameters in fields
    fields = field_list.split(", ")
    for field in fields:
        # (variable class, variable name)
        (_, name) = field.split(" ")
        writer.writeln(f"{T}{T}{T}this.{name} = {name};")

    writer.writeln(f"{T}{T}}}")

    # Fields
    writer.writeln()
    for field in fields:
        writer.writeln(f"{T}{T}final {field};")

    writer.writeln(f"{T}}}")


def main():
    if len(sys.argv) != 2:
        print(sys.argv)
        print("Usage: python generate_ast.py <output_directory>")
        sys.exit(1)

    output_dir = sys.argv[1]

    define_ast(output_dir, "Expr", [
        "Binary   : Expr left, Token operator, Expr right",
        "Grouping : Expr expression",
        "Literal  : Object value",
        "Unary    : Token operator, Expr right",
    ])


if __name__ == "__main__":
    main()
