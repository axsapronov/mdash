#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

import base64
import json
import os
import re
import sys
import types
import six

BASE_FOLDER = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        os.path.pardir
    )
)
try:
    from EMT import EMTypograph
except (ImportError, ModuleNotFoundError):
    module_path = os.path.join(BASE_FOLDER, "src-py")
    sys.path.append(module_path)
    from EMT import EMTypograph


def main():
    file_path = os.path.join(
        BASE_FOLDER,
        "tests/tests.json"
    )

    if not os.path.isfile(file_path):
        print("Not found test file by path - {}".format(
            file_path
        ))
        return -1

    # read test
    with open(file_path, "r") as fio:
        tests = json.loads(fio.read())

    verbose = False
    total = 0
    passed = 0

    for test in tests:
        EMT = EMTypograph()
        if verbose:
            EMT.debug_enabled = True
            EMT.logging = True

        if test["title"] == "Минус в диапозоне чисел":
            x = 1

        if "params" in test:
            EMT.setup(test["params"])

        if test.get("safetags"):
            x = test.get("safetags")

            if isinstance(x, six.string_types):
                x = [x]

            for s in x:
                EMT.add_safe_tag(s)

        EMT.set_text(test["text"])

        passx = 0
        result = EMT.apply()

        if result == test["result"]:
            r = "OK     "
            passx += 1
        else:
            r = "FAIL   "

        print(r + test["title"])

        if result != test["result"]:
            print("    GOT:   " + result)
            print("    NEED:  " + test["result"])

        del EMT

        total += 1
        if passx >= 1:
            passed += 1

    print("Total tests : " + str(total))
    print("Passed tests: " + str(passed))
    print("Failed tests: " + str(total-passed))


if __name__ == "__main__":
    main()
