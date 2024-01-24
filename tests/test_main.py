from datetime import datetime

from pynavernews.main import (
    string_date_range,
    construct_index_page_urls,
    fetch_and_store_news_raw_data,
)


def test_string_date_range() -> None:
    assert list(string_date_range(datetime(2020, 1, 1), datetime(2020, 1, 5), 1)) == [
        '20200101', '20200102', '20200103', '20200104'
    ]
    assert list(string_date_range(datetime(2020, 1, 1), datetime(2020, 1, 5), 2)) == [
        '20200101', '20200103'
    ]
    assert list(string_date_range(datetime(2020, 1, 5), datetime(2020, 1, 1), 1)) == []


def test_construct_index_page_urls() -> None:
    assert set(construct_index_page_urls([100, 101], ['20200101', '20200103', '20200105'], 5)) == {
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=100&date=20200101&page=1',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=100&date=20200101&page=2',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=100&date=20200101&page=3',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=100&date=20200101&page=4',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=100&date=20200101&page=5',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=101&date=20200101&page=1',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=101&date=20200101&page=2',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=101&date=20200101&page=3',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=101&date=20200101&page=4',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=101&date=20200101&page=5',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=100&date=20200103&page=1',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=100&date=20200103&page=2',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=100&date=20200103&page=3',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=100&date=20200103&page=4',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=100&date=20200103&page=5',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=101&date=20200103&page=1',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=101&date=20200103&page=2',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=101&date=20200103&page=3',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=101&date=20200103&page=4',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=101&date=20200103&page=5',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=100&date=20200105&page=1',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=100&date=20200105&page=2',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=100&date=20200105&page=3',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=100&date=20200105&page=4',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=100&date=20200105&page=5',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=101&date=20200105&page=1',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=101&date=20200105&page=2',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=101&date=20200105&page=3',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=101&date=20200105&page=4',
        'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=101&date=20200105&page=5'
    }
