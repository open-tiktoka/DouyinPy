import pytest
from douyinapipy.api import DouyinAPI
from douyinapipy.async_api import AsyncDouyinAPI


@pytest.mark.skip("Deprecated test")
async def test_init_error():
    with pytest.raises(ValueError):
        AsyncDouyinAPI(scroll_down_time=10, headless=True)

    with pytest.raises(ValueError):
        DouyinAPI(scroll_down_time=10, headless=True)
