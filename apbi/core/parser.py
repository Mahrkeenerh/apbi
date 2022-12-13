"""Parse webpages."""

from typing import List
import re
from datetime import datetime
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from apbi.models import Notice, Details


def parse_page(full_text: str, link: str) -> List[int]:
    """Parse full text into a list of notice ids.

    Args:
        full_text: Full text of the page.
        link: Link to the page.

    Returns:
        List of ids.
    """

    soup = BeautifulSoup(full_text, "html.parser")
    notices_soup = soup.find_all("div", {"class": "inzeraty inzeratyflex"})

    notice_ids = []

    for notice_soup in notices_soup:
        url = urlparse(link)

        if url.netloc == "www.bazos.sk":
            full_link = notice_soup.find("a").get("href")
        else:
            full_link = f"{url.scheme}://{url.netloc}" + notice_soup.find("a").get("href")

        notice_ids.append(re.search(r"inzerat/([0-9]+)/", full_link).group(1))

    return notice_ids


def parse_rss(full_text: str) -> List[Notice]:
    """Parse rss full text into a list of notices.

    Args:
        full_text: Full text of the page.

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
        publish_date = f"{date.year}-{date.month:02d}-{date.day:02d}"
        publish_time = f"{date.hour:02d}:{date.minute:02d}:{date.second:02d}"

        notice = Notice(
            notice_id=re.search(r"inzerat/([0-9]+)/", notice_soup.find("link").text).group(1),
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


def preload_notice(notice: Notice, full_text: str) -> None:
    """Preload notice details.

    Args:
        notice: Notice to preload into.
        full_text: Full text of the page.
    """

    soup = BeautifulSoup(full_text, "html.parser")
    table_items = soup.find("td").find_all("tr")
    locations = table_items[2].find_all("a")

    top_tag = soup.find("span", {"class": "ztop"})

    if top_tag is None:
        top_count = 0
        topped_until = None

    else:
        top = re.search(r"(\d+)x[^\d]*(\d+)[^\d]*(\d+)[^\d]*(\d+)", top_tag.get("title"))
        top_count = int(top.group(1))
        topped_until = f"{top.group(4)}-{int(top.group(3)):02d}-{int(top.group(2)):02d}"

    views_text = table_items[3].find_all("td")[1].text

    details = Details(
        full_description=soup.find("div", {"class": "popisdetail"}).text,
        city=locations[1].text,
        postal_code=locations[0].text,
        seller_name=table_items[0].find_all("td")[1].text,
        phone_number=table_items[1].find_all("td")[1].text,
        top_count=top_count,
        topped_until=topped_until,
        views=int(re.search(r"(\d+)", views_text).group(1))
    )

    notice.details = details


def parse_meta(full_text: str) -> dict:
    """Parse meta data from the page.

    Args:
        full_text: Full text of the page.

    Returns:
        Dictionary of meta data.
    """

    soup = BeautifulSoup(full_text, "html.parser")

    header_text = soup.find("div", {"class": "inzeratynadpis"}).text.replace(" ", "")
    footer = soup.find_all("b")[-2:]

    meta = {
        "header_total": int(re.search(r"z(\d+)", header_text).group(1)),
        "footer_total": int(footer[0].text),
        "footer_daily": int(footer[1].text),
    }

    return meta
