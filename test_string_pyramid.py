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
    assert watch_pyramid_from_above(None) is None


def test_watch_from_the_side_empty():
    """Test that watch from the_side on empty works."""
    assert watch_pyramid_from_the_side('') == ''


def test_watch_from_the_side_none():
    """Test that watch from the_side on none works."""
    assert watch_pyramid_from_above(None) is None


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


def test_count_visible_two():
    """Test that count visible characters with two characters works."""
    assert count_visible_characters_of_the_pyramid('*#') == 9


def test_count_all_two():
    """Test that count all characters with two characters works."""
    assert count_all_characters_of_the_pyramid('*#') == 10


def test_print_side_two():
    """Test that print from the side works on two characters."""
    assert watch_pyramid_from_the_side('*#') == '''\
 # 
***'''


def test_print_above_two():
    """Test that print from the above works on two characters."""
    assert watch_pyramid_from_above('*#') == '''\
***
*#*
***'''


def test_count_visible_three():
    """Test that count visible characters with two characters works."""
    assert count_visible_characters_of_the_pyramid('abc') == 25


def test_count_all_three():
    """Test that count all characters with two characters works."""
    assert count_all_characters_of_the_pyramid('abc') == 35


def test_print_side_three():
    """Test that print from the side works on three characters."""
    assert watch_pyramid_from_the_side('abc') == '''\
  c  
 bbb 
aaaaa'''


def test_print_above_three():
    """Test that print from the above works on three characters."""
    assert watch_pyramid_from_above('abc') == '''\
aaaaa
abbba
abcba
abbba
aaaaa'''


def test_count_visible_three_same():
    """Test that count visible characters with three same characters works."""
    assert count_visible_characters_of_the_pyramid('aaa') == 25


def test_count_all_three_same():
    """Test that count all characters with three same characters works."""
    assert count_all_characters_of_the_pyramid('aaa') == 35


def test_print_side_three_same():
    """Test that print from the side works on three same characters."""
    assert watch_pyramid_from_the_side('aaa') == '''\
  a  
 aaa 
aaaaa'''


def test_print_above_three_same():
    """Test that print from the above works on three same characters."""
    assert watch_pyramid_from_above('aaa') == '''\
aaaaa
aaaaa
aaaaa
aaaaa
aaaaa'''


def test_count_visible_five_descending():
    """Test that count visible characters with five descending characters works."""
    assert count_visible_characters_of_the_pyramid('54321') == 81


def test_count_all_five_descending():
    """Test that count all characters with five descending characters works."""
    assert count_all_characters_of_the_pyramid('54321') == 165


def test_print_side_five_descending():
    """Test that print from the side works on five descending characters."""
    assert watch_pyramid_from_the_side('54321') == '''\
    1    
   222   
  33333  
 4444444 
555555555'''


def test_print_above_five_descending():
    """Test that print from the above works on five descending characters."""
    assert watch_pyramid_from_above('54321') == '''\
555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555'''