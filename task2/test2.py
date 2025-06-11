import pytest
from unittest.mock import patch, Mock
from bs4 import BeautifulSoup

from solution2 import search_page


MOCK_HTML = '''
<div class="mw-category-group"><ul><li><a>Аист</a></li><li><a>Антилопа</a></li></ul></div>
<div class="mw-category-group"><ul><li><a>Бобр</a></li><li><a>Бабуин</a></li></ul></div>
<div class="mw-category-group"><ul><li><a>Волк</a></li><li><a>Воробей</a></li></ul></div>
'''


def test_search_page_success():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = MOCK_HTML

    with patch('requests.get', return_value=mock_response):
        result, last_elem = search_page("https://fake-url")
        assert isinstance(result, dict)
        assert "В" in result
        assert result["В"] == 2
        assert last_elem == "Воробей"


def test_search_page_empty():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = "<html></html>"

    with patch('requests.get', return_value=mock_response):
        result, last_elem = search_page("https://fake-url")
        assert result == {}
        assert last_elem is None


