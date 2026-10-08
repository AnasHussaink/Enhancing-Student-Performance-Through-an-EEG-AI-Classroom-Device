"""Reproduce the historical parser defect without importing the GUI application.

Exit 0: the fixture decodes correctly.
Exit 1: the known mismatch remains (expected for the packaged historical source).
This single fixture is not a comprehensive protocol conformance test.
"""
import ast
from pathlib import Path


def main():
    source = Path(__file__).resolve().parents[1] / 'software' / 'tgam_dashboard.py'
    tree = ast.parse(source.read_text(encoding='utf-8'))
    parser = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'parse_payload')
    isolated = ast.Module(body=[parser], type_ignores=[])
    namespace = {}
    exec(compile(ast.fix_missing_locations(isolated), str(source), 'exec'), namespace)
    bands = [101, 202, 303, 404, 505, 606, 707, 808]
    payload = bytes([0x04, 60, 0x83, 24]) + b''.join(v.to_bytes(3, 'big') for v in bands)
    expected = (60, 404, 606, 808)
    actual = namespace['parse_payload'](payload)
    print('Fields:   (attention, high_alpha, high_beta, mid_gamma)')
    print('Expected:', expected)
    print('Actual:  ', actual)
    if actual != expected:
        print('KNOWN DEFECT reproduced. See docs/KNOWN_ISSUES.md; do not trust current band-power decoding.')
        return 1
    print('Fixture passed. Additional protocol and hardware verification is still required.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
