"""Scrape Bazos for all sections and categories."""

import json

from bs4 import BeautifulSoup
import requests


def scrape_sections() -> None:
    """Scrape sections and categories from Bazos."""

    url = "https://www.bazos.sk/"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")

    sections_soup = soup.find_all("span", {"class": "nadpisnahlavni"})
    sections_raw = [section.a for section in sections_soup]
    sections = [{"name": section.text, "link": section["href"][:-1]} for section in sections_raw]

    for section in sections:
        print(section)

        section_soup = BeautifulSoup(requests.get(section["link"]).text, "html.parser")
        rss_element = section_soup.find(lambda tag: tag.name == "a" and tag.text == "RSS")
        section["section_rss"] = rss_element["href"]

        categories_soups = section_soup.find_all("div", {"class": "barvaleva"})
        categories_raw = [
            category for element in categories_soups
            for category in element.find_all("a")
        ]
        categories = [{
            "name": category.text,
            "link": category["href"]
        } for category in categories_raw]
        section["categories"] = categories

        for category in categories:
            if "https" not in category["link"]:
                link = section["link"] + category["link"]
            else:
                link = category["link"]

            category_soup = BeautifulSoup(requests.get(link).text, "html.parser")
            rss_element = category_soup.find(lambda tag: tag.name == "a" and tag.text == "RSS")
            category["category_rss"] = rss_element["href"]

    with open("assets/raw_sections.json", "w", encoding="utf-8") as out_file:
        json.dump(sections, out_file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    scrape_sections()
