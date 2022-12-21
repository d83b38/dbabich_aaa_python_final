import urllib.request
from unittest.mock import patch
import io
import pytest
from what_is_year_now import what_is_year_now


def test_current_year():
    """ check """
    actual = what_is_year_now()
    expected = 2022
    assert actual == expected


def test_ymd_mock():
    """ check ymd format """
    with patch.object(urllib.request,
                      'urlopen',
                      return_value=io.StringIO('{"currentDateTime": "2022-11-19T19:32Z"}')):
        actual = what_is_year_now()
    expected = 2022
    assert actual == expected


def test_dmy_mock():
    """ check dmy format """
    with patch.object(urllib.request,
                      'urlopen',
                      return_value=io.StringIO('{"currentDateTime": "19.11.2022T19:32Z"}')):
        actual = what_is_year_now()
    expected = 2022
    assert actual == expected


def test_invalid_format_error():
    """ check stange format ValueError """
    with patch.object(urllib.request,
                      'urlopen',
                      return_value=io.StringIO('{"currentDateTime": "2022/11/19T19:32Z"}')):
        with pytest.raises(ValueError) as ctx:
            what_is_year_now()
        assert isinstance(ctx.value, ValueError)
