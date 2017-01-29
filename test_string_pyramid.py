"""Test string pyramid functions."""

from string_pyramid import (
    watch_pyramid_from_the_side,
    watch_pyramid_from_above,
    count_visible_characters_of_the_pyramid,
    count_all_characters_of_the_pyramid)


def test_watch_from_above_empty():
    """Test that watch from above on empty works."""
    assert watch_pyramid_from_above('') == ''


def test_watch_from_above_none():
    """Test that watch from above on none works."""
    assert watch_pyramid_from_above(None) == None


def test_watch_from_the_side_empty():
    """Test that watch from the_side on empty works."""
    assert watch_pyramid_from_the_side('') == ''


def test_watch_from_the_side_none():
    """Test that watch from the_side on none works."""
    assert watch_pyramid_from_above(None) == None


def test_count_all_empty():
    """Test that count all characters works on empty string."""
    assert count_all_characters_of_the_pyramid('') == -1


def test_count_visible_empty():
    """Test that count visible characters works on empty string."""
    assert count_visible_characters_of_the_pyramid('') == -1


def test_count_all_none():
    """Test that count all characters works on none."""
    assert count_all_characters_of_the_pyramid('') == -1


def test_count_visible_none():
    """Test that count visible characters works on none."""
    assert count_visible_characters_of_the_pyramid('') == -1