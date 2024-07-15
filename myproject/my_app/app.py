from flask import Flask, render_template, jsonify
import random
import numpy as np

app = Flask(__name__)

# 定义星球及其属性
planets = [
    {"name": "Mercury", "multiplier": 3, "probability": 0.29},
    {"name": "Venus", "multiplier": 4, "probability": 0.22},
    {"name": "Earth", "multiplier": 6, "probability": 0.156},
    {"name": "Mars", "multiplier": 8, "probability": 0.117},
    {"name": "Uranus", "multiplier": 10, "probability": 0.096},
    {"name": "Neptune", "multiplier": 15, "probability": 0.064},
    {"name": "Saturn", "multiplier": 25, "probability": 0.038},
    {"name": "Jupiter", "multiplier": 50, "probability": 0.019},
]

cumulative_probabilities = np.cumsum([planet['probability'] for planet in planets])

def simulate_game(bets, simulations=1000000):
    total_winnings = {planet["name"]: 0 for planet in planets}
    total_bets = {planet["name"]: 0 for planet in planets}

    for _ in range(simulations):
        rand = random.random()
        for i, planet in enumerate(planets):
            if rand <= cumulative_probabilities[i]:
                chosen_planet = planet
                break

        for planet in planets:
            if planet["name"] in bets:
                total_bets[planet["name"]] += bets[planet["name"]]
                if planet == chosen_planet:
                    total_winnings[planet["name"]] += bets[planet["name"]] * planet["multiplier"]

    results = {}
    for planet in planets:
        name = planet["name"]
        if total_bets[name] > 0:
            expected_return = total_winnings[name] / total_bets[name]
        else:
            expected_return = 0
        results[name] = {
            "total_bet": total_bets[name],
            "total_winnings": total_winnings[name],
            "expected_return": expected_return
        }
    return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['GET'])
def simulate():
    bets = {planet["name"]: 1 for planet in planets}
    results = simulate_game(bets)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
