"""Create sections.py in a proper format."""

import json
from unidecode import unidecode


def clean(word: str) -> str:
    """Remove and replace all extra characters from word.
    
    Args:
        word: Word to clean.
    
    Returns:
        Cleaned word.
    """

    word = word.replace("-", "")
    word = word.replace(",", "")
    word = word.replace("/", "_")

    return "_".join(word.split())


def basic_print() -> None:
    """Output sections as basic class."""

    sections = json.load(open("assets/raw_sections.json", encoding="utf-8"))

<<<<<<< HEAD
    with open("apbi/models/sections/sections.py", "w", encoding="utf-8") as outfile:
        print('"""All sections and categories from bazos."""', file=outfile)
        print(file=outfile)
        print(file=outfile)
        print("from typing import Optional, Type", file=outfile)
        # print(file=outfile)
        # print(file=outfile)

        # for section in sections:
        #     name = clean(f"SECTION_{section['name'].upper()}")
        #     print(f'{name}: Optional[Type["{name}"]] = None', file=outfile)

=======
    with open("apbi/models/sections.py", "w", encoding="utf-8") as outfile:
        print('"""All sections and categories from bazos"""', file=outfile)
>>>>>>> master
        print(file=outfile)
        print(file=outfile)
        print("class Category:", file=outfile)
        print('    """Base category class."""', file=outfile)
        print(file=outfile)
        print("    section_name: str = None", file=outfile)
        print("    section_rss: str = None", file=outfile)
        print("    category_name: str = None", file=outfile)
        print("    category_rss: str = None", file=outfile)
        print(file=outfile)
        print("    search: str = None", file=outfile)
        print("    postal_code: str = None", file=outfile)
        print("    vicinity: int = None", file=outfile)
        print("    price_min: int = None", file=outfile)
        print("    price_max: int = None", file=outfile)
        print(file=outfile)
        print("    def __init__(", file=outfile)
        print("        self,", file=outfile)
        print("        search: str = None,", file=outfile)
        print("        postal_code: str = None,", file=outfile)
        print("        vicinity: int = None,", file=outfile)
        print("        price_min: int = None,", file=outfile)
        print("        price_max: int = None,", file=outfile)
        print("    ):", file=outfile)
        print("        self.search = search", file=outfile)
        print("        self.postal_code = postal_code", file=outfile)
        print("        self.vicinity = vicinity", file=outfile)
        print("        self.price_min = price_min", file=outfile)
        print("        self.price_max = price_max", file=outfile)
        print(file=outfile)
        print(file=outfile)

        for section in sections:
            section_class_name = clean(f"SECTION_{section['name'].upper()}")
            section_name = section["link"].split("//")[1].split(".")[0]
            section_rss = section["section_rss"].split("rub=")[1]

            print(f"class {section_class_name}(Category):", file=outfile)
            print(f'    """{section_class_name}."""', file=outfile)
            print(file=outfile)
            print(f'    section_name = "{section_name}"', file=outfile)
            print(f'    section_rss = "{section_rss}"', file=outfile)
            print(file=outfile)

            for category in section["categories"]:
                category_class_name = clean(category['name'].upper())
<<<<<<< HEAD
                print(
                    f'    {category_class_name}: Optional[Type["{category_class_name}"]] = None',
                    file=outfile
                )
=======
                print(f"    {category_class_name} = None", file=outfile)
>>>>>>> master

            print("\n", file=outfile)

            for category in section["categories"]:
                if "link" not in category:
                    continue

                category_class_name = clean(category['name'].upper())
                category_name = category["link"][1: -1]
                category_rss = category["category_rss"].split("cat=")[1]

                print(f"class {category_class_name}({section_class_name}):", file=outfile)
                print(f'    """{section_class_name} -> {category_class_name}."""', file=outfile)
                print(file=outfile)
                print(f'    category_name = "{category_name}"', file=outfile)
                print(f'    category_rss = "{category_rss}"', file=outfile)
                print("\n", file=outfile)

<<<<<<< HEAD
        # for section in sections:
        #     section_class_name = clean(f"SECTION_{section['name'].upper()}")
        #     print(f"{section_class_name} = {section_class_name}", file=outfile)

        # print(file=outfile)

=======
>>>>>>> master
        for section in sections:
            section_class_name = clean(f"SECTION_{section['name'].upper()}")

            for category in section["categories"]:
                category_class_name = clean(category['name'].upper())

                print(
                    f"{section_class_name}.{category_class_name} = {category_class_name}",
                    file=outfile
                )

            print(file=outfile)


def fix_issues() -> None:
    """Fix issues with sections and categories."""

<<<<<<< HEAD
    with open("apbi/models/sections/sections.py", "r", encoding="utf-8") as infile:
=======
    with open("apbi/models/sections.py", "r", encoding="utf-8") as infile:
>>>>>>> master
        contents = unidecode("".join(infile.readlines()[:-1]))

    fix_mapping = json.load(open("assets/fix_mapping.json", encoding="utf-8"))

<<<<<<< HEAD
    with open("apbi/models/sections/sections.py", "w", encoding="utf-8") as outfile:
=======
    with open("apbi/models/sections.py", "w", encoding="utf-8") as outfile:
>>>>>>> master
        for fix in fix_mapping:
            contents = contents.replace(fix, fix_mapping[fix])
        
        outfile.write(contents)


if __name__ == "__main__":
    basic_print()
    fix_issues()
