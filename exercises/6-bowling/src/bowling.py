

def bowling2strike(partie: str) -> int:
    frames = partie.split()
    score = 0

    for i, frame in enumerate(frames):
        if frame == "X":
            score += handle_strike()
        else:
            for throw in frame:
                if throw == "-":
                    score += 0
                else:
                    score += int(throw)

    return score

def handle_strike() -> int:
    return 10
