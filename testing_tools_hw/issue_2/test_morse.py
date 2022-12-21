import pytest
from morse import decode


@pytest.mark.parametrize(
    'string, exp',
    [
        ('HI-MARK', '.... .. -....- -- .- .-. -.-'),
        ('88005553535', '---.. ---.. ----- ----- ..... ..... ..... ...-- ..... ...-- .....'),
        ('SOS', '... --- ...')
    ]
)
def test_decode(string, exp):
    """ test for decoding"""
    assert string == decode(exp)
