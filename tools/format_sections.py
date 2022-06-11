"""Create sections.py in a proper format."""

from io import TextIOWrapper
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


def define_print(sections: list, out_file: TextIOWrapper) -> None:
    """Print all defining classes."""

    for section in sections:
        section_class_name = clean(f"SECTION_{str(section['name']).upper()}")
        section_name = str(section["link"]).split("//")[1].split(".")[0]
        section_rss = str(section["section_rss"]).split("rub=")[1]

        print(f"class {section_class_name}(Category):", file=out_file)
        print(f'    """{section_class_name}."""', file=out_file)
        print(file=out_file)
        print(f'    section_name = "{section_name}"', file=out_file)
        print(f'    section_rss = "{section_rss}"', file=out_file)
        print(file=out_file)

        for category in section["categories"]:
            category_class_name = clean(str(category['name']).upper())

            if "https" not in category["link"]:
                category_rss = str(category["category_rss"]).split("cat=")[1]
                rss_plaintext = category_rss.replace("&", "_").replace("=", "_")
                category_full_name = f"{category_class_name}_{rss_plaintext}"

            else:
                category_full_name = category_class_name

            print(f'    {category_class_name}: "{category_full_name}" = None', file=out_file)

        print("\n", file=out_file)

        for category in section["categories"]:
            if "https" in category["link"]:
                continue

            category_class_name = clean(str(category['name']).upper())
            category_name = category["link"][1: -1]
            category_rss = str(category["category_rss"]).split("cat=")[1]
            rss_plaintext = category_rss.replace("&", "_").replace("=", "_")
            category_full_name = f"{category_class_name}_{rss_plaintext}"

            print(f"class {category_full_name}({section_class_name}):", file=out_file)
            print(f'    """{section_class_name} -> {category_class_name}."""', file=out_file)
            print(file=out_file)
            print(f'    category_name = "{category_name}"', file=out_file)
            print(f'    category_rss = "{category_rss}"', file=out_file)
            print("\n", file=out_file)


def assign_print(sections: list, out_file: TextIOWrapper) -> None:
    """Print all class assignments."""

    for section in sections:
        section_class_name = clean(f"SECTION_{str(section['name']).upper()}")

        for category in section["categories"]:
            category_class_name = clean(str(category['name']).upper())

            try:
                category_rss = str(category["category_rss"]).split("cat=")[1]
                rss_plaintext = category_rss.replace("&", "_").replace("=", "_")
                category_full_name = f"{category_class_name}_{rss_plaintext}"

            except IndexError:
                category_full_name = category_class_name

            finally:
                print(
                    f"{section_class_name}.{category_class_name} = {category_full_name}",
                    file=out_file
                )

        print(file=out_file)


def basic_print() -> None:
    """Output sections as basic class."""

    with open("assets/raw_sections.json", encoding="utf-8") as sections_file:
        sections = json.load(sections_file)

    with open("apbi/models/sections/sections.py", "w", encoding="utf-8") as out_file:
        print('"""All sections and categories from bazos."""', file=out_file)
        print(file=out_file)
        print("# pylint: disable=C0103", file=out_file)
        print("# pylint: disable=C0302", file=out_file)
        print(file=out_file)
        print(file=out_file)
        print("class Category:", file=out_file)
        print('    """Base category class."""', file=out_file)
        print(file=out_file)
        print("    section_name: str = None", file=out_file)
        print("    section_rss: str = None", file=out_file)
        print("    category_name: str = None", file=out_file)
        print("    category_rss: str = None", file=out_file)
        print(file=out_file)
        print("    search: str = None", file=out_file)
        print("    postal_code: str = None", file=out_file)
        print("    vicinity: int = None", file=out_file)
        print("    price_min: int = None", file=out_file)
        print("    price_max: int = None", file=out_file)
        print(file=out_file)
        print("    def __init__(", file=out_file)
        print("        self,", file=out_file)
        print("        search: str = None,", file=out_file)
        print("        postal_code: str = None,", file=out_file)
        print("        vicinity: int = None,", file=out_file)
        print("        price_min: int = None,", file=out_file)
        print("        price_max: int = None,", file=out_file)
        print("    ):", file=out_file)
        print("        self.search = search", file=out_file)
        print("        self.postal_code = postal_code", file=out_file)
        print("        self.vicinity = vicinity", file=out_file)
        print("        self.price_min = price_min", file=out_file)
        print("        self.price_max = price_max", file=out_file)
        print(file=out_file)
        print(file=out_file)

        define_print(sections, out_file)
        assign_print(sections, out_file)


def fix_issues() -> None:
    """Fix issues with sections and categories."""

    with open("apbi/models/sections/sections.py", "r", encoding="utf-8") as in_file:
        contents = unidecode("".join(in_file.readlines()[:-1]))

    with open("assets/fix_mapping.json", encoding="utf-8") as map_file:
        fix_mapping = json.load(map_file)

    with open("apbi/models/sections/sections.py", "w", encoding="utf-8") as out_file:
        for fix in fix_mapping:
            contents = contents.replace(fix, fix_mapping[fix])

        out_file.write(contents)


if __name__ == "__main__":
    basic_print()
    fix_issues()
