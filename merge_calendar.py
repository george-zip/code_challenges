import pytest
from typing import List

"""
Two approaches to problem of merging calendar entries
Entries are tuples of integers with the format (start_time, end_time) where there may be overlap between entries
"""


def meetings_overlap(meeting1: (int, int), meeting2: (int, int)) -> bool:
    """
    Return true if meetings overlap. Order of arguments does not matter
    :param meeting1: First meeting
    :param meeting2: Second meeting
    :return: True if meetings overlap, False otherwise
    """
    return meeting2[0] <= meeting1[0] <= meeting2[1] or meeting1[0] <= meeting2[0] <= meeting1[1]


def merge_meetings(meeting1: (int, int), meeting2: (int, int)) -> (int, int):
    """
    Merge two overlapping meeting and return result
    :param meeting1: First meeting
    :param meeting2: Second meeting
    :return: Merged meeting
    """
    if not meetings_overlap(meeting1, meeting2):
        raise Exception(f"Meetings do not overlap {meeting1} - {meeting2}")
    return min(meeting1[0], meeting2[0]), max(meeting1[1], meeting2[1])


def merge_calendars(meetings: List[(int, int)]) -> List[(int, int)]:
    """
    Approach 1: Sort meetings by start date then iterate through sorted meetings merging with previous if it overlaps
    Worst case performance O(n log n)
    :param meetings: List of meetings to merge
    :return: Merged calendar
    """
    if len(meetings) < 2:
        return meetings
    meetings = sorted(meetings)
    merged_calendar = []
    for meeting in meetings:
        if merged_calendar and meetings_overlap(meeting, merged_calendar[-1]):
            merged_calendar[-1] = merge_meetings(meeting, merged_calendar[-1])
        else:
            merged_calendar.append(meeting)
    return merged_calendar


def merge_calendars_bin_search(meetings: List[(int, int)]) -> List[(int, int)]:
    """
    Approach 2: For each meeting in meetings, use a binary search by meeting start time to find where it sits in
    the merged calendar. Merge with adjacent meetings if there is overlap.
    Worst case performance is O(n log n)
    Code is more muddled than necessary
    :param meetings: List of meetings to merge
    :return: Merged calendar
    """
    if len(meetings) < 2:
        return meetings
    merged_calendar = [meetings.pop()]
    for meeting in meetings:
        lo, hi = -1, len(merged_calendar)
        midpoint = lo + (hi - lo) // 2
        guess = merged_calendar[midpoint]
        while lo + 1 < hi:
            midpoint = lo + (hi - lo) // 2
            guess = merged_calendar[midpoint]
            if guess[0] == meeting[0]:
                break
            if guess[0] > meeting[0]:
                hi = midpoint
            else:
                lo = midpoint
        midpoint = midpoint + 1 if guess[0] < meeting[0] else midpoint
        merged_calendar.insert(midpoint, meeting)
        if midpoint > 0 and meetings_overlap(merged_calendar[midpoint], merged_calendar[midpoint - 1]):
            merged_calendar[midpoint] = merge_meetings(merged_calendar[midpoint], merged_calendar[midpoint - 1])
            del merged_calendar[midpoint - 1]
        if midpoint < len(merged_calendar) - 1 and \
                meetings_overlap(merged_calendar[midpoint], merged_calendar[midpoint + 1]):
            merged_calendar[midpoint] = merge_meetings(merged_calendar[midpoint], merged_calendar[midpoint + 1])
            del merged_calendar[midpoint + 1]
    return merged_calendar


"""
Test cases
"""


def test_no_overlap():
    m1 = (0, 1)
    m2 = (3, 5)
    assert not meetings_overlap(m1, m2)


def test_overlap():
    m1 = (0, 3)
    m2 = (3, 5)
    assert meetings_overlap(m1, m2)


def test_overlap_order_not_important():
    m1 = (0, 3)
    m2 = (3, 5)
    assert meetings_overlap(m2, m1)


def test_merge_meetings():
    m1 = (0, 4)
    m2 = (3, 5)
    assert merge_meetings(m1, m2) == (0, 5)


def test_merge_calendars_nothing():
    meetings = [(0, 1)]
    assert merge_calendars(meetings) == [(0, 1)]


def test_merge_calendars_two():
    assert merge_calendars([(3, 5), (4, 8)]) == [(3, 8)]


def test_merge_calendars_five():
    assert merge_calendars([(10, 12), (0, 1), (4, 8), (9, 10), (3, 5)]) == [(0, 1), (3, 8), (9, 12)]


def test_not_exactly_overlap():
    assert merge_calendars([(1, 2), (2, 3)]) == [(1, 3)]


def test_subsumed_meeting():
    assert merge_calendars([(1, 5), (2, 3)]) == [(1, 5)]


def test_merge_all():
    assert merge_calendars([(1, 10), (2, 6), (3, 5), (7, 9)]) == [(1, 10)]
