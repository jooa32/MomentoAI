#!/usr/bin/env python3
import argparse
import sys

__arg_parser = argparse.ArgumentParser(
    prog="PrintHello",
    description="python CLI"
)

# __arg_parser.add_argument("-v", "--version", action="store_true")
__arg_parser.add_argument("-u", "--username", default="")

__argv = __arg_parser.parse_args(sys.argv[1:])

username: str = __argv.username
# show_version: bool = __argv.version

hello: str = f"hi{f', {username}' if username else ''}"
# version: str = f" - python version : {sys.version_info.major}.{sys.version_info.minor}" if show_version else ""

print(f"{hello}")