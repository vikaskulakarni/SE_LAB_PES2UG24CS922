from marathon_registration import entry_fee, start_wave, finisher_status
import pytest


# Entry-fee tests: normal values, discounts, add-ons, and validation branches.
def test_entry_fee_standard():
    assert entry_fee("10k", 30, False, False) == 800


def test_entry_fee_early_bird():
    assert entry_fee("10k", 30, True, False) == 600


def test_entry_fee_tshirt():
    assert entry_fee("5k", 30, False, True) == 800


def test_entry_fee_senior():
    assert entry_fee("5k", 65, False, False) == 250


def test_entry_fee_early_bird_senior_tshirt():
    assert entry_fee("10k", 65, True, True) == 600


@pytest.mark.parametrize("race", ["unknown", "marathon"])
def test_invalid_race(race):
    with pytest.raises(ValueError, match="unknown race"):
        entry_fee(race, 30, False, False)


def test_age_too_young():
    with pytest.raises(ValueError, match="too young"):
        entry_fee("5k", 11, False, False)


@pytest.mark.parametrize("race", ["half", "full"])
def test_age_too_young_for_long_race(race):
    with pytest.raises(ValueError, match="too young for this distance"):
        entry_fee(race, 17, False, False)


# Start-wave tests: no recorded time and every wave for both cutoff types.
def test_first_timer_wave():
    assert start_wave(None, "full") == "D"


def test_fast_full_wave():
    assert start_wave(180, "full") == "A"


def test_medium_full_wave():
    assert start_wave(200, "full") == "B"


def test_slow_full_wave():
    assert start_wave(241, "full") == "C"


def test_fast_other_race_wave():
    assert start_wave(90, "10k") == "A"


def test_medium_other_race_wave():
    assert start_wave(110, "10k") == "B"


def test_slow_other_race_wave():
    assert start_wave(121, "10k") == "C"


# Finisher-status tests: disqualification, time limits, and DNF paths.
def test_disqualified_runner():
    assert finisher_status(60, "5k", 1) == "DSQ"


@pytest.mark.parametrize("race, elapsed", [
    ("full", 360),
    ("half", 180),
    ("10k", 90),
])
def test_finisher_at_time_limit(race, elapsed):
    assert finisher_status(elapsed, race, 0) == "finisher"


@pytest.mark.parametrize("race, elapsed", [
    ("full", 361),
    ("half", 181),
    ("10k", 91),
])
def test_runner_exceeds_time_limit(race, elapsed):
    assert finisher_status(elapsed, race, 0) == "DNF"
