"""All sections and categories from bazos."""

# pylint: disable=C0103
# pylint: disable=C0302


class Category:
    """Base category class."""

    section_name: str = None
    section_rss: str = None
    category_name: str = None
    category_rss: str = None

    search: str = None
    postal_code: str = None
    vicinity: int = None
    price_min: int = None
    price_max: int = None

    def __init__(
        self,
        search: str = None,
        postal_code: str = None,
        vicinity: int = None,
        price_min: int = None,
        price_max: int = None,
    ):
        self.search = search
        self.postal_code = postal_code
        self.vicinity = vicinity
        self.price_min = price_min
        self.price_max = price_max


class SECTION_ALL(Category):
    """SECTION_ALL."""

    section_name = ""
    section_rss = ""
