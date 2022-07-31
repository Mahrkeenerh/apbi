"""Single notice class."""


class Details:
    """Details class containing notice information."""

    def __init__(
        self,
        full_description: str,
        city: str,
        postal_code: str,
        seller_name: str,
        phone_number: str,
    ) -> None:
        """Initialize details instance.

        Args:
            full_description: full description of the notice.
            city: city of the notice.
            postal_code: postal code of the notice.
            seller_name: name of seller of the notice.
            phone_number: phone number of the seller, or `None` if not verified.
        """

        self.description = full_description
        """description: Full description of the notice."""

        self.city = city
        """city: City of the notice."""

        self.postal_code = postal_code
        """postal_code: Postal code of the notice."""

        self.name = seller_name
        """seller_name: Name of seller of the notice."""

        self.phone = phone_number
        """phone_number: Phone number of the seller, or `None` if not verified."""


class Notice:
    """Single notice class."""

    def __init__(
        self,
        notice_id: str,
        rss: bool,
        title: str,
        link: str,
        thumbnail: str,
        published_date: str,
        published_time: str,
        description: str,
        price: str,
        top_count: int = None,
        topped_until: str = None,
        views: int = None
    ) -> None:
        """Initialize notice instance.

        Args:
            notice_id: ID of the notice.
            rss: whether the notice is from RSS or not.
            title: title of the notice.
            link: full link to the notice.
            thumbnail: link to thumbnail of the notice.
            published_date: date of publication. Format 'YYYY-MM-DD'.
            published_time: time of publication. Format 'hh:mm:ss timezone'
                or `None` if not `rss`.
            description: short description of the notice.
            price: display price of the notice.
            top_count: number of times the notice has been topped (not preloaded if `rss`).
            topped_until: the date the notice will be topped until. Format 'YYYY-MM-DD'
                or `None` if not topped (not preloaded if `rss`).
            views: number of times the notice has been viewed (not preloaded if `rss`).
        """

        self.notice_id = notice_id
        """notice_id: ID of the notice."""

        self.rss = rss
        """rss: Whether the notice is from RSS or not."""

        self.title = title
        """title: Title of the notice."""

        self.link = link
        """link: Full link to the notice."""

        self.thumbnail = thumbnail
        """thumbnail: Link to thumbnail of the notice."""

        self.published_date = published_date
        """published: Date of publication. Format 'YYYY-MM-DD'."""

        self.published_time = published_time
        """published_time: Time of publication. Format 'hh:mm:ss timezone'
        or `None` if not `rss`."""

        self.description = description
        """description: Short display description of the notice."""

        self.price = price
        """price: Display price of the notice."""

        self.top_count = top_count
        """top_count: Number of times the notice has been topped (not preloaded if `rss`)."""

        self.topped_until = topped_until
        """topped_until: The date the notice will be topped until. Format 'YYYY-MM-DD'
        or `None` if not topped (not preloaded if `rss`)."""

        self.views = views
        """views: Number of times the notice has been viewed (not preloaded if `rss`)."""

        self.details = None
        """details: Details of the notice (not preloaded)."""

        self._preloaded = False
        """_preloaded: Whether the notice has been preloaded or not."""

    async def preload(self) -> None:
        """Preload details of the notice."""

        if self._preloaded:
            return

        # self.details = await self.get_details()
        # TODO CALL paraser preload
        self._preloaded = True
