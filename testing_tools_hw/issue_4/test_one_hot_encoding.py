import pytest
from one_hot_encoder import fit_transform


def test_fit_transform():
    """ main logic test """
    test_list = ['cold', 'cold', 'warm', 'cold', 'hot']
    actual = fit_transform(test_list)
    expected = [('cold', [0, 0, 1]),
                ('cold', [0, 0, 1]),
                ('warm', [0, 1, 0]),
                ('cold', [0, 0, 1]),
                ('hot', [1, 0, 0])]
    assert actual == expected


def test_not_in():
    """ test wrong calcaulation  """
    test_list = ['a', 'b', 'c', 'a', 'b']
    not_expected = ('b', [1, 0, 0])
    actual = fit_transform(test_list)
    assert not_expected not in actual


def test_error_empty():
    """ check empty throws TypeError """
    with pytest.raises(TypeError) as ctx:
        fit_transform()
    assert isinstance(ctx.value, TypeError)


def test_single_string():
    """ test single string """
    test_string = 'single'
    actual = fit_transform(test_string)
    expected = [('single', [1])]
    assert actual == expected
