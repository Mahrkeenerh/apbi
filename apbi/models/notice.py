"""Single notice class."""


class Display:
    """Display class containing displayed information."""

    def __init__(
        self,
        title: str,
        top_count: int,
        thumbnail: str,
        published: str,
        description: str,
        price: str,
        views: int
    ) -> None:
        """Initialize display instance.

        Args:
            title: Title of the notice.
            top_count: Number of notice tops.
            thumbnail: Thumbnail link for the notice.
            published: Date of publication. Format 'DD-MM-YYYY'.
            description: Short display description of the notice.
            price: Display price of the notice.
            views: Number of views of the notice.
        """

        self.title = title
        """title: Title of the notice."""

        self.top_count = top_count
        """top_count: Number of notice tops."""

        self.thumbnail = thumbnail
        """thumbnail: Thumbnail link for the notice."""

        self.published = published
        """published: Date of publication. Format 'DD-MM-YYYY'."""

        self.description = description
        """description: Short display description of the notice."""

        self.price = price
        """price: Display price of the notice."""

        self.views = views
        """views: Number of views of the notice."""


class Notice:
    """Single notice class."""

    def __init__(
        self,
        notice_id: int,
        link: str,
        seller_name: str,
        phone_number: str,
        display: Display,
        city: str,
        postal_code: str,
        description: str,
        published: str,
        price: int,
    ) -> None:
        """Initialize notice instance.

        Args:
            notice_id: ID of the notice.
            link: Full link to the notice.
            seller_name: Name of the seller.
            phone_number: Phone number of the seller, or `None` if not verified.
            display: Display class containing all displayed information.
            city: City of the notice.
            postal_code: Postal code of the notice.
            description: Full description of the notice.
            published: Date of publication. Format 'Day, DD Month YYYY hh:mm:ss timezone'.
            price: Price of the notice.
        """

        self.notice_id = notice_id
        """notice_id: ID of the notice."""

        self.link = link
        """link: Full link to the notice."""

        self.name = seller_name
        """seller_name: Name of the seller."""

        self.phone = phone_number
        """phone_number: Phone number of the seller, or `None` if not verified."""

        self.display = display
        """display: Display class containing all displayed information."""

        self.city = city
        """city: City of the notice."""

        self.postal_code = postal_code
        """postal_code: Postal code of the notice."""

        self.description = description
        """description: Full description of the notice."""

        self.published = published
        """published: Date of publication. Format 'Day, DD Month YYYY hh:mm:ss timezone'."""

        self.price = price
        """price: Price of the notice."""
