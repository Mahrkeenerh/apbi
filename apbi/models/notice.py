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
        top_count: int,
        topped_until: str,
        views: int
    ) -> None:
        """Initialize details instance.

        Args:
            full_description: full description of the notice.
            city: city of the notice.
            postal_code: postal code of the notice.
            seller_name: name of seller of the notice.
            phone_number: phone number of the seller, or `None` if not verified.
            top_count: number of times the notice has been topped.
            topped_until: the date the notice will be topped until. Format 'YYYY-MM-DD'
                or `None` if not topped.
            views: number of times the notice has been viewed.
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

        self.top_count = top_count
        """top_count: Number of times the notice has been topped."""

        self.topped_until = topped_until
        """topped_until: The date the notice will be topped until. Format 'YYYY-MM-DD'
            or `None` if not topped."""

        self.views = views
        """views: Number of times the notice has been viewed."""


class Notice:
    """Single notice class."""

    def __init__(
        self,
        notice_id: str,
        title: str,
        link: str,
        thumbnail: str,
        published_date: str,
        published_time: str,
        description: str,
        price: str
    ) -> None:
        """Initialize notice instance.

        Args:
            notice_id: ID of the notice.
            title: title of the notice.
            link: full link to the notice.
            thumbnail: link to thumbnail of the notice.
            published_date: date of publication. Format 'YYYY-MM-DD'.
            published_time: time of publication. Format 'hh:mm:ss timezone'.
            description: short description of the notice.
            price: display price of the notice.
        """

        self.notice_id = notice_id
        """notice_id: ID of the notice."""

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
