import unittest
import datetime
import thxtime


class TestThxTime(unittest.TestCase):
    def test_that_thx_works_as_advertised(self):
        times = [
            datetime.time(11, 38),
            datetime.time(23, 38)
        ]
        for t in times:
            self.assertEqual(thxtime.thx_time(t), "THX")

    def test_brute_force_inverse_case_yes_this_is_silly(self):
        for h in range(0, 23):
            for m in range(0, 59):
                if (h, m) not in [(11, 38), (23, 38)]:
                    t = datetime.time(h, m)
                    self.assertNotEqual(thxtime.thx_time(t), "THX")

    def test_that_12_and_24_hour_times_work(self):
        times = [
            datetime.time(3, 14),
            datetime.time(15, 14)
        ]
        for t in times:
            self.assertEqual(thxtime.thx_time(t), "π")

if __name__ == '__main__':
    unittest.main()
