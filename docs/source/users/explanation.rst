************
How it Works
************

DouyinPy works without needing any login information or cookies. This is powerful for anonymity and avoiding timeouts,
but this does come with its limitations.

DouyinPy grabs information in two steps:

Grabbing Preloaded Content
==========================

When you load a Douyin page, some JavaScript performs an API call and inserts the data directly into the HTML of the
page. This data is used to insert any preloaded videos, comments, users, etc. This data is not removed from the HTML,
so DouyinPy grabs it do initialize its data models.

The data is saved in the HTML in a script tag:

.. code-block:: html

    <script id="SIGI_STATE" type="application/json">
        {
            <!-- API response packed as JSON, to be loaded into Pydantic models -->
        }
    </script>

Only certain portions of the data is actually retrieved, and some of it is post-processed for user simplicity.

Grabbing Additional API Data
============================

As more of the page is loaded, some scripts make some additional API calls to retrieve more data to display on the page.
This data is not saved anywhere in the HTML, so DouyinPy intercepts these API calls and makes them itself. It uses the
cookies and headers that would have been used by the page scripts to make the API calls. This allows DouyinPy to be
aware of and make the API calls made when you normally browse Douyin without needing any login information.

Limitations
===========

Slideshows
----------

Douyin limits slideshows to mobile viewing. In order to retrieve data from slideshows, you must emulate a mobile device:

.. tabs::

    .. code-tab:: py DouyinAPI

            from douyinapipy.api import DouyinAPI

            def get_challenge_videos_scroll_down():
                with DouyinAPI(emulate_mobile=True) as api:
                    slideshow = api.video(link_to_slideshow)
                    ...

    .. code-tab:: py AsyncDouyinAPI

            from douyinapipy.async_api import AsyncDouyinAPI

            async def get_challenge_videos_scroll_down():
                async with AsyncDouyinAPI(emulate_mobile=True) as api:
                    slideshow = await api.video(link_to_slideshow)
                    ...

See :ref:`Examples` for more.

Data Collection
---------------

By default, DouyinPy only grabs preloaded content and any API calls made during the page load. This is fairly limiting
for the amount of data you can retrieve. In order to grab more data, additional API calls will be needed to be
triggered. This can only be done by scrolling down on the page. The amount to scroll down by is determined by how long
you want DouyinPy to scroll down for:

.. tabs::

    .. code-tab:: py DouyinAPI

            from douyinapipy.api import DouyinAPI

            def get_challenge_videos_scroll_down():
                # scroll down for 2.5 seconds when making requests
                with DouyinAPI(scroll_down_time=2.5) as api:
                    challenge = api.challenge(tag_name)
                    for video in challenge.videos:
                        ...

    .. code-tab:: py AsyncDouyinAPI

            from douyinapipy.async_api import AsyncDouyinAPI

            async def get_challenge_videos_scroll_down():
                # scroll down for 2.5 seconds when making requests
                async with AsyncDouyinAPI(scroll_down_time=2.5) as api:
                    challenge = await api.challenge(tag_name)
                    async for video in challenge.videos:
                        ...

.. warning::
    This will not work with mobile emulation. In order to take advantage of slideshow scraping alongside additional
    data scraping with ``scroll_down_time``, you will need to create a second, mobile-emulating API instance. You will
    not be able to retrieve any data that isn't retrieved during page load with this second API.

.. note::
    ``scroll_down_time`` is also an available option on API calls. Specifying a value here will override the default
    value set in the API constructor.

Navigation Retries and Headless Browsing
----------------------------------------

Occasionally, navigation will take a very long time. This can be circumvented by attempting navigation again.
Additionally, a navigation timeout can be specified, which will force a retry if navigation takes too long:

.. tabs::

    .. code-tab:: py DouyinAPI

            from douyinapipy.api import DouyinAPI

            def do_something():
                # retry twice (up to 3 navigation attempts), force-retry navigation after 10 seconds
                with DouyinAPI(navigation_retries=2, navigation_timeout=10) as api:
                    ...

    .. code-tab:: py AsyncDouyinAPI

            from douyinapipy.async_api import AsyncDouyinAPI

            async def do_something():
                # retry twice (up to 3 navigation attempts), force-retry navigation after 10 seconds
                async with AsyncDouyinAPI(navigation_retries=2, navigation_timeout=10) as api:
                    ...

If navigation fails after all retries are spent, a :ref:`DouyinAPIError` will be raised.

.. note::
    This normally happens when the ``wait_until`` parameter for the API is set to ``"networkidle"``. By default,
    DouyinAPI will wait for a ``load`` event to be fired before scraping data, but this could miss some of the data
    retrieved from the API during page loading.
