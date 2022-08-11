from unittest import TestCase

from utils.recipes.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_current_page_less_than_mid(self):
        # current page = 1

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        # current page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=2,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_middle_range_changes(self):
        # current page = 3
        # here range should change
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=3,
        )['pagination']
        self.assertEqual([2, 3, 4, 5], pagination)
        # current page = 6
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=6,
        )['pagination']
        self.assertEqual([5, 6, 7, 8], pagination)

        # current page =15
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=15,
        )['pagination']
        self.assertEqual([14, 15, 16, 17], pagination)

    def test_make_pagination_range_static_when_in_end(self):
        # current page =19
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=19,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)
