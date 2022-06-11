"Main Bazos class."

import asyncio


class Bazos:
    """Bazos class allows for easy access to the Bazos website as a wrapper."""

    event_loop: asyncio.AbstractEventLoop = None
    """event_loop: Active event loop."""

    search_pool: int = 98
    """search_pool: Number of available search requests."""

    rss_pool: int = 50
    """rss_pool: Number of available RSS requests."""

    def __init__(self, ) -> None:
        ...

    def start(self, event_loop: asyncio.AbstractEventLoop = None) -> None:
        """Start event loop.

        Args:
            event_loop: event loop to use, if None, use default event loop.
        """

        if event_loop is None:
            self.event_loop = asyncio.get_event_loop()
        else:
            self.event_loop = event_loop

        self.event_loop.run_forever()
