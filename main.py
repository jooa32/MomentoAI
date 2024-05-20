#!/usr/bin/env python3
import argparse
import sys

__arg_parser = argparse.ArgumentParser(
    prog="PrintHello",
    description="python CLI"
)

__arg_parser.add_argument("-u", "--username", default="")

__argv = __arg_parser.parse_args(sys.argv[1:])

username: str = __argv.username

hello: str = f"hi{f', {username}' if username else ''}"

print(f"{hello}")

