def test_specific():  # noqa: AAA01
    assert 1 + 1 == 2


def test_multi_line_args_specific(  # noqa: AAA01
    math_fixture,
    *args,
    **kwargs
):
    assert 1 + 1 == 2
