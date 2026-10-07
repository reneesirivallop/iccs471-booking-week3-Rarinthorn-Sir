"""Add your two tests here. Keep the supplied baseline and smoke tests intact."""
import unittest
from models import Booking
from service import move_booking

# Add a unittest.TestCase class with your two test methods.
# See IA 3.2 for the cases and the expectation you must record before using AI.

class StudentMoveTests(unittest.TestCase):
    # Given: one active booking in Room 201 from 10:00-11:00
    # When: move it in the same room to 10:30-11:30
    # Expect: the overlapping move succeeds, updates the same object, and keeps the list unchanged apart from that booking's fields.
    def test_same_room_move_may_overlap_old_interval(self):
        target = Booking(1, "Room 201", 600, 660)
        bookings = [target]

        result = move_booking(bookings, 1, "Room 201", 630, 690)

        self.assertIs(result, target)
        self.assertIs(bookings[0], target)
        self.assertEqual(target, Booking(1, "Room 201", 630, 690))
        self.assertEqual(len(bookings), 1)

    # Given: one active booking in Room 201 from 10:00-11:00
    # When: request the same room and interval again
    # Expect: the request succeeds without changing the booking or list membership
    def test_requesting_current_room_and_times_is_unchanged(self):
        target = Booking(1, "Room 201", 600, 660)
        bookings = [target]

        result = move_booking(bookings, 1, "Room 201", 600, 660)

        self.assertIs(result, target)
        self.assertEqual(bookings, [Booking(1, "Room 201", 600, 660)])
        self.assertIs(bookings[0], target)

if __name__ == "__main__":
    unittest.main()
