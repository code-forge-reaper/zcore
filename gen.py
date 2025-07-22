#!/usr/bin/env python3
"""
gen.py — generate a Markdown API reference for your modules.
"""

import sys
import argparse
import inspect
import importlib,os
from pathlib import Path

def find_modules(src_dir: Path):
    """Yield (module_name, filepath) for every .py under src_dir, skipping __init__.py."""
    for path in sorted(src_dir.rglob("*.py")):
        if path.name == "__init__.py":
            continue
        # derive module path: src/foo/bar.py → foo.bar
        rel = path.relative_to(src_dir).with_suffix("")
        yield ".".join(rel.parts), path

def safe_import(module_name):
    """Import a module, adding src_dir to sys.path if needed."""
    try:
        return importlib.import_module(f"{module_name}")
    except ImportError:
        # fallback: assume src_dir is top-level package 'src'
        return importlib.import_module(f"src.{module_name}")

def render_signature(obj):
    return f"```python\n{obj.__name__}{inspect.signature(obj)}\n```"

def document_function(func):
    sig = render_signature(func)
    doc = inspect.getdoc(func) or "_no docstring_"
    if doc == "_no docstring_":
        print(f"function `{func.__name__}` has no docstring")
    return f"{sig}\n\n{doc}\n"

def document_class(cls):
    out = [f"### class `{cls.__name__}`\n"]
    class_doc = inspect.getdoc(cls) or "_no docstring_"
    out.append(f"{class_doc}\n")
    # methods
    for name, meth in inspect.getmembers(cls, inspect.isfunction):
        if meth.__qualname__.split('.')[0] != cls.__name__:
            continue
        if name.startswith("_"):
            continue
        d = f"{inspect.getdoc(meth) or '_no docstring_'}\n"
        if d == "_no docstring_\n":
            print(f"method `{name}` has no docstring")
        out.append(f"#### `{name}{inspect.signature(meth)}`\n\n"+d)
    return "\n".join(out)

def main():
    p = argparse.ArgumentParser(description=f"Generate {os.path.basename(os.getcwd())} API_REFERENCE.md")
    p.add_argument("-s", "--src", default="src", help="source directory")
    p.add_argument("-o", "--out", default="API_REFERENCE.md", help="output file")
    p.add_argument("--include-private", action="store_true",
                   help="include names starting with '_'")
    args = p.parse_args()

    src_dir = Path(args.src)
    modules = list(find_modules(src_dir))

    toc = ["## Table of Contents\n"]
    body = [f"# {os.path.basename(os.getcwd())} API Reference\n"]

    for mod_name, path in modules:
        # import module
        try:
            mod = safe_import(mod_name)
        except Exception as e:
            print(f"⚠️  Failed to import {mod_name}: {e}", file=sys.stderr)
            continue

        # TOC entry
        anchor = mod_name.replace(".", "")
        toc.append(f"- [{mod_name}](#{anchor})")

        # Module header
        body.append(f"## `{mod_name}`\n")
        mod_doc = inspect.getdoc(mod) or "_no module docstring_"
        if mod_doc == "_no module docstring_":
            print(f"module `{mod_name}` has no docstring")
        body.append(f"{mod_doc}\n")

        # Functions
        funcs = [
            f for _, f in inspect.getmembers(mod, inspect.isfunction)
            if f.__module__ == mod.__name__
            and (args.include_private or not f.__name__.startswith("_"))
        ]
        if funcs:
            body.append("### Functions\n")
            for func in funcs:
                body.append(document_function(func))

        # Classes
        classes = [
            c for _, c in inspect.getmembers(mod, inspect.isclass)
            if c.__module__ == mod.__name__
            and (args.include_private or not c.__name__.startswith("_"))
        ]
        if classes:
            body.append("### Classes\n")
            for cls in classes:
                body.append(document_class(cls))

    # assemble and write
    output = "\n\n".join(toc) + "\n\n" + "\n\n".join(body)
    Path(args.out).write_text(output, encoding="utf-8")
    print(f"Wrote {args.out}")

if __name__ == "__main__":
    main()
