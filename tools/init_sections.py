"""Create __init__.py file for sections."""

import json
from unidecode import unidecode

from format_sections import clean


def init_sections() -> None:
    """Import all categories."""

    sections = json.load(open("assets/raw_sections.json", "r", encoding="utf-8"))

    with open("apbi/models/sections/__init__.py", "w", encoding="utf-8") as init_file:
        print('"""sections models."""', file=init_file)
        print(file=init_file)
        print("from sections import Category", file=init_file)

        for section in sections:
            section_class_name = clean(f"{section['name'].upper()}")

            print(
                f"from sections import SECTION_{section_class_name} as {section_class_name}",
                file=init_file
            )
    
    with open("apbi/models/sections/__init__.py", "r", encoding="utf-8") as infile:
        contents = unidecode("".join(infile.readlines())[:-1])
    
    with open("apbi/models/sections/__init__.py", "w", encoding="utf-8") as outfile:
        print(contents, file=outfile)


if __name__ == "__main__":
    init_sections()
