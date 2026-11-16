from hypothesis import given, strategies as st
from marathon_registration_parser import format_bib_name, parse_finish_time, average_split


@given(st.text() | st.none())
def test_format_bib_name_no_crash(s):
    try:
        result = format_bib_name(s)
    except Exception as exc:
        assert False, f"format_bib_name crashed for {s!r}: {exc}"
    assert isinstance(result, str)
    assert len(result) <= 12


@given(st.text() | st.none())
def test_parse_finish_time_no_crash(s):
    try:
        result = parse_finish_time(s)
    except Exception as exc:
        assert False, f"parse_finish_time crashed for {s!r}: {exc}"
    assert result is None or (isinstance(result, int) and result >= 0)


@given(st.text() | st.none())
def test_average_split_no_crash(s):
    try:
        result = average_split(s)
    except Exception as exc:
        assert False, f"average_split crashed for {s!r}: {exc}"
    assert result is None or (isinstance(result, (int, float)) and result >= 0)
