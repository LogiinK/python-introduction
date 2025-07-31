
def get_or_default(frames: list[str], index: int) -> str:
    try:
        return frames[index]
    except IndexError:
        return "-"

def bowling2strike(partie: str) -> int:
    frames = partie.split()
    score = 0

    for i, frame in enumerate(frames[:10]):
        if frame == "X":
            score += handle_strike(get_or_default(frames, i +1), get_or_default(frames, i + 2))
        elif frame[1] == "/":
            score += handle_spare(get_or_default(frames, i +1))
        else:
            for throw in frame:
                if throw == "-":
                    score += 0
                else:
                    score += int(throw)

    return score

def handle_strike(next_frame: str, next_next_frame: str) -> int:
    next_throw: int = 0
    next_next_throw: int = 0

    if next_frame == "X":
        next_throw = 10

        if next_next_frame == "X":
            next_next_throw = 10
        elif next_next_frame in ["-", "--"]:
            next_next_throw = 0
        else:
            if next_next_frame[0] == "-":
                next_next_throw += 0
            else:
                next_next_throw += int(next_next_frame[0])

    elif next_frame in ["-", "--"]:
        next_throw = 0

    else :
        next_frame2 = list(next_frame)
        for throw in next_frame2:
            if throw == "-":
                next_throw += 0
            elif "/" in throw:
                next_next_throw = 10-next_throw
            else:
                next_throw += int(throw)
    return 10+ next_throw + next_next_throw

def handle_spare(next_frame: str) -> int:
    next_throw: int = 0

    if next_frame == "/":
        next_throw = 10

    elif next_frame in ["-", "--"]:
        next_throw = 0

    else:
        for throw in next_frame:
            if throw == "-":
                next_throw += 0
            elif "/" not in throw:
                next_throw += int(throw)

    return 10+ next_throw
