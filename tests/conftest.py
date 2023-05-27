import pytest
from douyinapipy.api import DouyinAPI
from douyinapipy.async_api import AsyncDouyinAPI


@pytest.fixture(scope="session")
def navigation_timeout():
    return 10


@pytest.fixture(scope="session")
def navigation_retries():
    return 2


@pytest.fixture(scope="session")
def headless_browsing():
    return True


@pytest.fixture(scope="function")
async def async_api(
    navigation_timeout, navigation_retries, headless_browsing
) -> AsyncDouyinAPI:
    async with AsyncDouyinAPI(
        navigation_timeout=navigation_timeout,
        navigation_retries=navigation_retries,
        headless=headless_browsing,
    ) as api:
        yield api


@pytest.fixture(scope="function")
def sync_api(navigation_timeout, navigation_retries, headless_browsing) -> DouyinAPI:
    with DouyinAPI(
        navigation_timeout=navigation_timeout,
        navigation_retries=navigation_retries,
        headless=headless_browsing,
    ) as api:
        yield api


@pytest.fixture(scope="function")
async def async_api_mobile(
    navigation_timeout, navigation_retries, headless_browsing
) -> AsyncDouyinAPI:
    async with AsyncDouyinAPI(
        emulate_mobile=True,
        navigation_timeout=navigation_timeout,
        navigation_retries=navigation_retries,
        headless=headless_browsing,
    ) as api:
        yield api


@pytest.fixture(scope="function")
def sync_api_mobile(
    navigation_timeout, navigation_retries, headless_browsing
) -> DouyinAPI:
    with DouyinAPI(
        emulate_mobile=True,
        navigation_timeout=navigation_timeout,
        navigation_retries=navigation_retries,
        headless=headless_browsing,
    ) as api:
        yield api


@pytest.fixture(scope="session")
def video_id():
    return 6914948781100338440


@pytest.fixture(scope="session")
def slideshow_id():
    return 6914948781100338440


@pytest.fixture(scope="session")
def user_name():
    return "h12121122"


@pytest.fixture(scope="session")
def user_secuid():
    return "MS4wLjABAAAAbkpBheGBN_h62a0ZP5eGTaLg0zl6TtnF6yNf8HUWJko"


@pytest.fixture(scope="session")
def user_nickname():
    return "不叫猫先生"


@pytest.fixture(scope="session")
def user_uniqueid():
    return "7231176569393776168"


@pytest.fixture(scope="session")
def user_userid():
    return "4488643020068816"


@pytest.fixture(scope="session")
def challenge_name():
    return "1597726178104324"


# https://www.douyin.com/user/MS4wLjABAAAAbkpBheGBN_h62a0ZP5eGTaLg0zl6TtnF6yNf8HUWJko?vid=7228374577766829372
# 不叫猫先生
# 关注
# 69
# 粉丝
# 2262
# 获赞
# 27.3万
# 抖音号：h12121122
# IP属地：浙江
# 好好生活好好爱自己

# url decode result
#  {
# 		"1": {
# 			"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51",
# 			"isClient": false,
# 			"osInfo": {
# 				"os": "Mac",
# 				"version": "",
# 				"isMas": false
# 			},
# 			"isSpider": false,
# 			"pathname": "/user/MS4wLjABAAAAbkpBheGBN_h62a0ZP5eGTaLg0zl6TtnF6yNf8HUWJko",
# 			"envService": "prod",
# 			"odin": {
# 				"user_id": "4488643020068816",
# 				"user_type": 12,
# 				"user_is_auth": 0,
# 				"user_unique_id": "7231176569393776168"
# 			},
# 			"tccConfig": {
# 				"LiveSmallWindow": {
# 					"restrictTime": 10,
# 					"durationTime": 10,
# 					"ratio": 2,
# 					"showTime1": 5,
# 					"showTime2": 10
# 				},
# 				"LoginGuideConfig": {
# 					"hideLoginGuideStartTime": 1643608800000,
# 					"hideLoginGuideEndTime": 1643648400000,
# 					"hideLoginGuide": true
# 				},
# 				"ScanCodeEntrance": {
# 					"location": 1
# 				},
# 				"activity_task_modal": [{
# 					"name": "five",
# 					"localStorageName": "in_five_list",
# 					"open": false,
# 					"taskId": {
# 						"web": "aweme_pc_open",
# 						"client": ""
# 					},
# 					"actionName": {
# 						"web": "five.aweme_pc_open.action",
# 						"client": ""
# 					},
# 					"group": "five",
# 					"backgroundImg": "https://p-pc-weboff.byteimg.com/tos-cn-i-9r5gewecjs/20221223-140814.png"
# 				}],
# 				"ad_config": {
# 					"openInSidebarCondition": {
# 						"siteTypes": [1, 10],
# 						"externalActions": []
# 					}
# 				},
# 				"backback_group_match_time": {
# 					"start_time": 1667890372000,
# 					"end_time": 1670013000000
# 				},
# 				"backpack_broadcast": [{
# 					"id": "22",
# 					"color": "linear-gradient(#388DA8, #4056CB)"
# 				}, {
# 					"id": "23",
# 					"color": "linear-gradient(#AE3E59, #8D2C72)"
# 				}, {
# 					"id": "27",
# 					"color": "linear-gradient(#2D8369, #235E78)"
# 				}, {
# 					"id": "26",
# 					"color": "linear-gradient(#388DA8, #4056CB)"
# 				}, {
# 					"id": "25",
# 					"color": "linear-gradient(#54732C, #325C31)"
# 				}, {
# 					"id": "18",
# 					"color": "linear-gradient(#354993, #442D86)"
# 				}, {
# 					"id": "24",
# 					"color": "linear-gradient(#2D8369, #235E78)"
# 				}, {
# 					"id": "36",
# 					"color": "linear-gradient(#388DA8, #4056CB)"
# 				}],
# 				"backpack_download_guide_time": {
# 					"delay_time": 2000,
# 					"stay_time": 10000
# 				},
# 				"backpack_entry_filter": {
# 					"tab_entry": 0,
# 					"login_btn": 0,
# 					"client_download_guide": 0,
# 					"collection_guide": 0
# 				},
# 				"backpack_header_text": [{
# 					"text": "小组赛今日收官 最后两个晋级席位产生",
# 					"start_time": 1669928400000,
# 					"end_time": 1670014800000
# 				}, {
# 					"text": "1/8决赛开打 阿根廷再迎硬仗",
# 					"start_time": 1670014800000,
# 					"end_time": 1670101200000
# 				}, {
# 					"text": "淘汰赛厮杀继续 英法遇强敌",
# 					"start_time": 1670101200000,
# 					"end_time": 1670187600000
# 				}, {
# 					"text": "目标世界杯八强 蓝武士对格子军团 ",
# 					"start_time": 1670187600000,
# 					"end_time": 1670274000000
# 				}, {
# 					"text": "斗牛士战北非劲旅 葡萄牙欲拔瑞士军刀",
# 					"start_time": 1670274000000,
# 					"end_time": 1670360400000
# 				}, {
# 					"text": "八强出炉 各队休整两日",
# 					"start_time": 1670360400000,
# 					"end_time": 1670446800000
# 				}, {
# 					"text": "1/4决赛明日开打 豪强蓄势待发",
# 					"start_time": 1670446800000,
# 					"end_time": 1670533200000
# 				}, {
# 					"text": "桑巴军团鏖战克罗地亚 阿根廷人战郁金香",
# 					"start_time": 1670533200000,
# 					"end_time": 1670619600000
# 				}, {
# 					"text": "北非黑马阻击葡萄牙 英法大战火力碰撞",
# 					"start_time": 1670619600000,
# 					"end_time": 1670706000000
# 				}, {
# 					"text": "四强出炉 三天后冲击决赛席位",
# 					"start_time": 1670706000000,
# 					"end_time": 1670792400000
# 				}, {
# 					"text": "四强对阵出炉 半决赛一触即发",
# 					"start_time": 1670792400000,
# 					"end_time": 1670878800000
# 				}, {
# 					"text": "胜者进决赛 阿根廷鏖战克罗地亚",
# 					"start_time": 1670878800000,
# 					"end_time": 1670965200000
# 				}, {
# 					"text": "破防战 卫冕冠军对北非黑马",
# 					"start_time": 1670965200000,
# 					"end_time": 1671051600000
# 				}, {
# 					"text": "法国终结摩洛哥黑马之旅 决赛梅西大战姆巴佩",
# 					"start_time": 1671051600000,
# 					"end_time": 1671138000000
# 				}, {
# 					"text": "明日将迎季军赛 摩洛哥与克罗地亚再度交手",
# 					"start_time": 1671138000000,
# 					"end_time": 1671224400000
# 				}, {
# 					"text": "莫德里奇最后一舞 铁血大战谁更强硬",
# 					"start_time": 1671224400000,
# 					"end_time": 1671310800000
# 				}, {
# 					"text": "蓝白不改 阿根廷时隔36年再夺冠",
# 					"start_time": 1671310800000,
# 					"end_time": 1671397200000
# 				}, {
# 					"text": "蓝白不改 阿根廷时隔36年再夺冠",
# 					"start_time": 1671397200000,
# 					"end_time": 1702501200000
# 				}],
# 				"backpack_introduction": {
# 					"text": [{
# 						"start_time": 1661961600000,
# 						"end_time": 1665417600000,
# 						"text": "大力神杯足球世界杯的奖杯，是足球界的最高荣誉的象征。整个奖杯看上去就像两个大力士托起了地球，被称为“大力神金杯”。线条从底座跃出，盘旋而上，到顶端承接着一个地球，在这个充满动态的，紧凑的杯体上，雕刻出两个胜利后激动的运动员的形象。"
# 					}, {
# 						"start_time": 1662566400000,
# 						"end_time": 1664294400000,
# 						"text": "2022年卡塔尔世界杯是历史上首次在卡塔尔和中东国家境内举行、也是第二次在亚洲举行的世界杯足球赛，还是首次在北半球冬季举办的世界杯足球赛。"
# 					}],
# 					"button": [{
# 						"text": "卡塔尔介绍",
# 						"url": "https://www.baike.com/wiki/%E5%8D%A1%E5%A1%94%E5%B0%94/253861?view_id=23l1xgyw4qhs00"
# 					}, {
# 						"text": "赛事规则",
# 						"url": "https://www.baike.com/wikiid/2604623042938290350?prd=mobile&view_id=1smkp9cd6uf400"
# 					}, {
# 						"text": "世界杯历史",
# 						"url": "https://www.baike.com/wiki/%E5%9B%BD%E9%99%85%E8%B6%B3%E8%81%94%E4%B8%96%E7%95%8C%E6%9D%AF/3220499"
# 					}]
# 				},
# 				"backpack_live_entry": {
# 					"start_time": 1668943800000,
# 					"end_time": 1672044028000
# 				},
# 				"backpack_status": {
# 					"status": 0,
# 					"fifa_main_status": 1,
# 					"introduce_status": 0,
# 					"second_screen_status": 1
# 				},
# 				"backpack_timeline": [{
# 					"status": 0,
# 					"start_time": 1667898563000,
# 					"end_time": 1668790800000
# 				}, {
# 					"status": 1,
# 					"start_time": 1668790800000,
# 					"end_time": 1671314400000
# 				}, {
# 					"status": 2,
# 					"start_time": 1671314400000,
# 					"end_time": 1672178400000
# 				}],
# 				"backpack_use_filter"…
