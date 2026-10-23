"""Inventory the installed public sync API. No browser required.

This is a reference index, NOT a claim that every method has an executable test.
The async API has corresponding awaitable operations; see examples/async_example.py.
"""

import inspect
from importlib.metadata import version
from pathlib import Path

import playwright.sync_api._generated as api


def generate():
    output = Path(__file__).resolve().parents[1] / "docs" / "API_CATALOG.md"
    lines = [
        "# Public Python Playwright API catalog",
        "",
        f"Generated from installed Playwright **{version('playwright')}**.",
        "",
        "Public SDK wrapper classes, methods (including inherited public methods), and properties.",
        "Signatures come from the installed SDK, not a scraped documentation snapshot.",
        "This inventories the reference surface; see COVERAGE.md for runnable examples.",
        "Parameters and overload details: follow each official class link.",
        "Python type aliases, event-name overloads and private internals are outside this index.",
        "The catalog includes discouraged/legacy APIs for discoverability, not recommendation.",
        "",
    ]
    class_count = member_count = 0
    for name, cls in sorted(vars(api).items()):
        if name.startswith("_") or not inspect.isclass(cls) or cls.__module__ != api.__name__:
            continue
        class_count += 1
        lines.extend(
            [
                f"## {name}",
                "",
                f"[Official reference](https://playwright.dev/python/docs/api/class-{name.lower()})",
                "",
            ]
        )
        for member_name, member in inspect.getmembers(cls):
            if member_name.startswith("_"):
                continue
            if isinstance(member, property):
                lines.append(f"- `{member_name}` — property")
            elif callable(member):
                try:
                    signature = str(inspect.signature(member)).replace("\n", " ")
                except (TypeError, ValueError):
                    signature = "(...)"
                lines.append(f"- `{member_name}{signature}`")
            else:
                continue
            member_count += 1
        lines.append("")
    lines[2] += (
        f" {class_count} SDK wrapper classes; {member_count} public member entries (inherited entries may repeat)."
    )
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {output.name}: {class_count} classes, {member_count} public member entries")


if __name__ == "__main__":
    generate()
