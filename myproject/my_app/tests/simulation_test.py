import unittest
from app import simulate_game, planets

class SimulationTest(unittest.TestCase):
    def test_simulation(self):
        bets = {planet["name"]: 1 for planet in planets}
        results = simulate_game(bets)
        for planet in planets:
            name = planet["name"]
            expected_return = results[name]["expected_return"]
            print(f"{name}: Expected Return = {expected_return:.3f}")
            self.assertLess(abs(expected_return - 0.9), 0.1, f"{name} expected return is off")

if __name__ == '__main__':
    unittest.main()
