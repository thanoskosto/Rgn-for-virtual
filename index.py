import random
import time

teams = {
    "Παναθηναϊκός": {"attack": 75, "defense": 70},
    "Ολυμπιακός": {"attack": 80, "defense": 65},
    "ΑΕΚ": {"attack": 70, "defense": 68},
    "ΠΑΟΚ": {"attack": 73, "defense": 66}
}

def choose_teams():
    return random.sample(list(teams.keys()), 2)

def simulate_goal_chance(team_name, team_stats):
    chance = random.randint(1, 100)
    if chance <= team_stats["attack"] // 2:
        print(f"{team_name} κάνει επίθεση...")
        time.sleep(1)
        if random.randint(1, 100) < 60:
            print(f" Γκολ από τον {team_name}!\n")
            return 1
        else:
            print(f" Αποκρούει ο τερματοφύλακας!\n")
    return 0

def simulate_match(team1, team2):
    t1_score = 0
    t2_score = 0

    print(f"\n Αγώνας: {team1} vs {team2}")
    time.sleep(1)
    print("Ξεκινάει ο αγώνας!\n")
    time.sleep(1)

    for minute in range(1, 91, 10):
        print(f" Λεπτό {minute}")
        t1_score += simulate_goal_chance(team1, teams[team1])
        t2_score += simulate_goal_chance(team2, teams[team2])
        time.sleep(1)

    print(f" Τελικό σκορ: {team1} {t1_score} - {t2_score} {team2}")
    winner = None
    if t1_score > t2_score:
        winner = team1
    elif t2_score > t1_score:
        winner = team2
    else:
        winner = "Ισοπαλία"

    print(f" Νικητής: {winner}\n")

# Εκτέλεση
teamA, teamB = choose_teams()
simulate_match(teamA, teamB)
