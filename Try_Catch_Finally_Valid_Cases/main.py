import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CASES = [
    "try_except",
    "try_except_except",
    "try_except_else",
    "try_except_finally",
    "try_except_else_finally",
    "try_finally",
]


if __name__ == "__main__":
    print("Try-Except-Finally: All Valid Cases")
    print("Example: User Registration Service\n")

    for case in CASES:
        case_path = os.path.join(BASE_DIR, "valid_cases", f"{case}.py")
        os.system(f"{sys.executable} {case_path}")
        print()

