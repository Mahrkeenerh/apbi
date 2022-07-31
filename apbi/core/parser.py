"""Parse webpages."""

import re
from datetime import datetime

from bs4 import BeautifulSoup

from apbi.models import Notice


def parse_page(full_text: str, link: str) -> list:
    """Parse full text into a list of notices.

    Args:
        fulltext: Full text of the page.
        link: Link to the page.

    Returns:
        List of notices.
    """

    soup = BeautifulSoup(full_text, "html.parser")
    notices_soup = soup.find_all("div", {"class": "inzeraty inzeratyflex"})

    notices = []

    for notice_soup in notices_soup:
        full_link = link + notice_soup.find("a").get("href")
        date = re.search(r"\[(\d+)[^\d]*(\d+)[^\d]*(\d+)\]", notice_soup.find("span").text)
        top_tag = notice_soup.find("span", {"class": "ztop"})

        if top_tag is None:
            top_count = 0
            topped_until = None

        else:
            top = re.search(r"(\d+)x[^\d]*(\d+)[^\d]*(\d+)[^\d]*(\d+)", top_tag.get("title"))
            top_count = int(top.group(1))
            topped_until = f"{top.group(4)}-{top.group(3):02}-{top.group(2):02}"

        views_text = notice_soup.find("div", {"class": "inzeratyview"}).text
        views = int(re.search(r"(\d+)", views_text).group(1))

        notice = Notice(
            notice_id=re.search(r"inzerat/([0-9]+)/", full_link).group(1),
            rss=False,
            title=notice_soup.find("h2").text,
            link=full_link,
            thumbnail=notice_soup.find("img").get("src"),
            published_date=f"{date.group(3)}-{date.group(2):02}-{date.group(1):02}",
            published_time=None,
            description=notice_soup.find("div", {"class": "popis"}).text,
            price=notice_soup.find("b").text.strip(),
            top_count=top_count,
            topped_until=topped_until,
            views=views,
            details=None
        )

        notices.append(notice)

    return notices


def parse_rss(full_text: str) -> list:
    """Parse rss full text into a list of notices.

    Args:
        fulltext: Full text of the page.

    Returns:
        List of notices.
    """

    soup = BeautifulSoup(full_text, features="xml")
    notices_soup = soup.find_all("item")

    notices = []

    for notice_soup in notices_soup:
        title_match = re.search(r"(.*) - (.*)$", notice_soup.find("title").text)
        description_text = notice_soup.find("description").text

        if "<img src=" in description_text:
            thumbnail = re.search(r"\<img src=\"(.*)\".*class.*\/>", description_text).group(1)
            description = re.search(r"\<img src=.*\/>(.*)", description_text).group(1)
        else:
            thumbnail = "https://www.bazos.sk/obrazky/empty.gif"
            description = description_text

        date = datetime.strptime(notice_soup.find("pubDate").text, "%a, %d %b %Y %H:%M:%S %z")
        publish_date = f"{date.year}-{date.month:02}-{date.day:02}"
        publish_time = f"{date.hour:02}:{date.minute:02}:{date.second:02}"

        notice = Notice(
            notice_id=re.search(r"inzerat/([0-9]+)/", notice_soup.find("link").text).group(1),
            rss=True,
            title=title_match.group(1),
            link=notice_soup.find("link").text,
            thumbnail=thumbnail,
            published_date=publish_date,
            published_time=publish_time,
            description=description,
            price=title_match.group(2).strip()
        )

        notices.append(notice)

    return notices

# def parse_notice()

# def parse_meta()
