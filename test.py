from unittest import TestCase, main
from whiteboard import solution


class MatchTestCase(TestCase):
    def test_twocakes(self):
        self.assertEqual(solution({"flour": 500, "sugar": 200, "eggs": 1},
                                {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}), 2)
    def test_missing_ingredients(self):
        self.assertEqual(solution({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, 
                               {"sugar": 500, "flour": 2000, "milk": 2000}),0)
    def test_no_ingredients(self):
        self.assertEqual(solution({"apples": 3, "flour": 400, "sugar": 500}, {}),0)
    def test_just_one(self):
        self.assertEqual(solution({"cream": 1,"flour": 3, "sugar": 1,"milk": 1, "oil": 1, "eggs": 1,},
                               {"sugar": 1,"milk": 1, "cream": 1,"flour": 3, "oil": 1, "eggs": 1,}),1)
    def test_not_enough(self):
        self.assertEqual(solution({"apples": 1, "cream": 1,"flour":3,"sugar":1,},{"sugar":1, "flour":2,"apples":3, "cream":1}),0)