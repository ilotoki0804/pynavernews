from datetime import datetime
import os

import hxsoup

from pynavernews.extractor import (
    FieldMissingError,
    Extractor,
    FullExtractor,
    Normalizer,
)


def _get_resource(name) -> str:
    res_path = os.path.join(os.path.dirname(__file__), "resources", name)
    with open(res_path, "r", encoding="utf-8") as fp:
        return fp.read()


async def test_Extractor():
    index_page = _get_resource("index_page.html")

    class StaticExtractor(Extractor):
        def reformat_date(self, raw_date: str, standard_time: datetime | None = None):
            return super().reformat_date(raw_date, datetime(2000, 1, 1))

    extractor = StaticExtractor()
    assert [i async for i in extractor.extract_from_string(index_page)] == [
        {'image_url': 'https://imgnews.pstatic.net/image/origin/082/2024/01/22/1252309.jpg?type=nf106_72',
         'article_url': 'https://n.news.naver.com/mnews/article/082/0001252309?sid=101',
         'title': '“올바른 전기사용으로 안전한 겨울 보내세요”',
         'summary': '한국전기안전공사(사장 박지현)는 전열기구 사용 부주의로 인한 화재 증가에 대응하고자 ‘겨울철 전열기구 안전사용 요령’을 22일  …',
         'publisher': '부산일보',
         'date_string': '1999-12-31T00:00:00'},
        {'image_url': 'https://imgnews.pstatic.net/image/origin/422/2024/01/22/640951.jpg?type=nf106_72',
         'article_url': 'https://n.news.naver.com/mnews/article/422/0000640951?sid=101',
         'title': '대중교통비 지원 늘린다…수도권 교통카드 연이어 출시',
         'summary': '국토교통부와 서울시, 경기도, 인천시가 대중교통비 지원 사업에 대한 합동설명회를 열었습니다. 이번달 서울시의 기후동행카드를 시작 …',
         'publisher': '연합뉴스TV',
         'date_string': '1999-12-31T00:00:00'},
        {'image_url': 'https://imgnews.pstatic.net/image/origin/052/2024/01/22/1988628.jpg?type=nf106_72',
         'article_url': 'https://n.news.naver.com/mnews/article/052/0001988628?sid=101',
         'title': '"예고된 악몽"...홍콩H지수 ELS 손실률 최고 56%',
         'summary': '홍콩 H지수 급락으로 지난해부터 금융가에 엄습했던 불안이 현실이 됐습니다. 올해 들어 불과 십여 일 만에 홍콩H지수에 기초한 주 …',
         'publisher': 'YTN',
         'date_string': '1999-12-31T00:00:00'},
        {'image_url': 'https://imgnews.pstatic.net/image/origin/052/2024/01/22/1988627.jpg?type=nf106_72',
         'article_url': 'https://n.news.naver.com/mnews/article/052/0001988627?sid=101',
         'title': '정부, 대형마트 공휴일 의무 휴업·단통법 등 폐지',
         'summary': '정부가 대형 마트에 적용하는 공휴일 의무 휴업 규제를 없애고 단말기 유통법도 전면 폐지하기로 했습니다. 국무조정실은 오늘(22일 …',
         'publisher': 'YTN',
         'date_string': '1999-12-31T00:00:00'},
        {'image_url': 'https://imgnews.pstatic.net/image/origin/243/2024/01/22/55501.jpg?type=nf106_72',
         'article_url': 'https://n.news.naver.com/mnews/article/243/0000055501?sid=101',
         'title': '尹, 법무장관에 박성재 전 서울고검장 내정…대구 좌천 때 ‘한솥밥’',
         'summary': '윤석열 대통령이 22일 신임 법무부 장관에 박성재 전 서울고검장(61·사법연수원 17기)을 내정한 것으로 알려졌다. 대통령실은  …',
         'publisher': '이코노미스트',
         'date_string': '1999-12-31T00:00:00'},
        {'image_url': 'https://imgnews.pstatic.net/image/origin/082/2024/01/22/1252308.jpg?type=nf106_72',
         'article_url': 'https://n.news.naver.com/mnews/article/082/0001252308?sid=101',
         'title': '[에너지 소식] 석유관리원, 수소유통전담기관으로 지정外',
         'summary': '◆석유관리원, 수소유통전담기관으로 지정 한국석유관리원은 지난 19일 산업통상자원부로부터 ‘수소경제 및 수소 안전관리 등에 관한  …',
         'publisher': '부산일보',
         'date_string': '1999-12-31T00:00:00'},
        {'image_url': 'https://imgnews.pstatic.net/image/origin/003/2024/01/22/12333062.jpg?type=nf106_72',
         'article_url': 'https://n.news.naver.com/mnews/article/003/0012333062?sid=101',
         'title': '[올댓차이나] 작년 12월 대만 수출수주 16%↓…“반년만에 최대 감소”',
         'summary': '대만 2023년 12월 수출 수주액은 전년 동월 대비 16.0% 줄어든 438억1000만 달러(약 58조7054억원)를 기록했다 …',
         'publisher': '뉴시스',
         'date_string': '1999-12-31T00:00:00'},
        {'image_url': 'https://imgnews.pstatic.net/image/origin/119/2024/01/22/2792043.jpg?type=nf106_72',
         'article_url': 'https://n.news.naver.com/mnews/article/119/0002792043?sid=101',
         'title': '공정위, ‘중점조사팀’ 신설…국민 관심 큰 사건 조사 속도 높인다',
         'summary': '공정거래위원회가 ‘중점조사팀’을 신설해 국민적 관심사가 큰 사건 조사에 속도를 내기로 했다. 공정거래위원회는 22일 이같은 내용 …',
         'publisher': '데일리안',
         'date_string': '1999-12-31T00:00:00'},
        {'image_url': 'https://imgnews.pstatic.net/image/origin/374/2024/01/22/367597.jpg?type=nf106_72',
         'article_url': 'https://n.news.naver.com/mnews/article/374/0000367597?sid=101',
         'title': '서초 재건축 현장서 하청 근로자 숨져…고용부 "중처법 조사"',
         'summary': '포스코이엔씨가 시공하는 주택 재건축 공사 현장에서 하청 근로자가 철골구조물에 깔려 사망하는 사고가 발생했습니다. 22일 고용노동 …',
         'publisher': 'SBS Biz',
         'date_string': '1999-12-31T00:00:00'},
        {'image_url': 'https://imgnews.pstatic.net/image/origin/082/2024/01/22/1252307.jpg?type=nf106_72',
         'article_url': 'https://n.news.naver.com/mnews/article/082/0001252307?sid=101',
         'title': '[해양수산 소식] 해수부, 2024년 해양안전대책 협력방안 논의外',
         'summary': '◆해수부, 2024년 해양안전대책 협력방안 논의 강도형 해양수산부 장관은 22일 세종청사에서 해양경찰청, 광역시·도, 지방해양수 …',
         'publisher': '부산일보',
         'date_string': '1999-12-31T00:00:00'}
    ]


async def test_FullExtractor(mocker):
    mocker.patch("hxsoup.AsyncClient.get", return_value=hxsoup.SoupTools(_get_resource("article.html")))

    async with hxsoup.AsyncClient(follow_redirects=True) as client:
        result = await FullExtractor(client).fetch_and_extract_article(
            "https://n.news.naver.com/mnews/article/082/0001252309?sid=101")
    assert result == {
        'reporter_name': '송현수 기자(songh@busan.com)',
        'content':
            '전기안전공사, ‘겨울철 전열기구 안전사용 요령’ 발표\n전기장판 올바른 사용법. '
            '전기안전공사 제공\n한국전기안전공사(사장 박지현)는 전열기구 사용 부주의로 '
            '인한 화재 증가에 대응하고자 ‘겨울철 전열기구 안전사용 요령’을 22일 발표했다.\n'
            '전기안전공사에 따르면 최근 3년간 전열기구(전기장판·방석 등) 화재 건수는 '
            '2021년 179건, 2022년 242건, 2023년 257건으로 지속 증가 추세로, 올해 1월 사망자가 '
            '발생한 남원 화재 사고 또한 전기장판에서 발생한 화재다.\n전기장판, 전기방석 등 화재 '
            '위험성이 높은 전열기구는 올바른 사용법을 숙지하여 안전하게 사용해야 한다.\n우선, '
            '전열기구 구입 전 반드시 안전인증(KC마크) 확인해야한다.\n전기제품 사용 시에는 손상된 '
            '부분과 전선의 파손 등을 점검해야 한다. 전기제품 사용 전 온도조절기, 스위치 등의 등 '
            '파손 여부를 확인하고, 수리 또는 교체해 사용하는 것이 안전하다.\n전기장판 사용 시, '
            '라텍스 재질의 침구류와 함께 사용하지 않아야 한다. 장시간 사용할 경우 라텍스에 열이 '
            '축적되어 화재로 이어질 수 있기 때문이다.\n보관 시 무거운 물건 적치를 금하고, 습기를 '
            '피하고 꺾이지 않은 상태로 보관해야 한다.\n전기안전 관리에 관한 상담을 원하는 국민은 '
            '전기안전공사 콜센터(1588-7500)로 전화하면 상담 받을 수 있다.'
    }


def test_normalize():
    ratio = Normalizer().hangeul_ratio(
        "위키백과(Wiki百科, IPA: [ɥikçibɛ̝k̚k͈wa̠], [ykçibɛ̝k̚k͈wa̠] ( 듣기)) 또는 "
        "위키피디아(영어: Wikipedia, IPA: [ˌwɪkɪˈpiːdɪə] ( 듣기))는 누구나 "
        "자유롭게 쓸 수 있는 다언어판 인터넷 백과사전이다.[1] 2001년 1월 15일 지미 "
        "웨일스와 래리 생어가 시작하였으며[2], 대표적인 집단 지성의 사례로 평가받고 "
        "있다.[3]"
    )
    assert 0.44 < ratio and ratio < 0.45

    ratio = Normalizer().hangeul_ratio(
        "Wikipedia (/ˌwɪkɪˈpiːdiə/ (About this soundlisten) wik-ih-PEE-dee-ə "
        "or /ˌwɪkiˈpiːdiə/ (About this soundlisten) wik-ee-PEE-dee-ə; "
        "abbreviated as WP) is a multilingual online encyclopedia created and "
        "maintained as an open collaboration project[4] by a community of "
        "volunteer editors using a wiki-based editing system.[5] It is the "
        "largest and most popular general reference work on the World Wide "
        "Web.[6][7][8] It is also one of the 15 most popular websites as "
        "ranked by Alexa, as of August 2020.[9] It features exclusively free "
        "content and has no advertising. It is hosted[10] by the Wikimedia "
        "Foundation, an American non-profit organization funded primarily "
        "through donations.[11][12][13][14]"
    )
    assert ratio == 0


def test_normal_characters():
    assert Normalizer.is_normal_character("하")
    assert Normalizer.is_normal_character("1")
    assert Normalizer.is_normal_character("a")
    assert Normalizer.is_normal_character("Z")

    assert not Normalizer.is_normal_character("ㄴ")
    assert not Normalizer.is_normal_character("(")
    assert not Normalizer.is_normal_character(".")
    assert not Normalizer.is_normal_character("'")
