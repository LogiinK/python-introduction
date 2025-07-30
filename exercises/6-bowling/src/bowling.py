def bowling2loses(partie: str) -> int:
    # "-- -- -- -- -- ..." -> ["--", "--", "--"....]
    frames = partie.split()
    score = 0
    for frame in frames:
        if frame!="--":
            pass

    return score

def bowling2win(partie: str) -> int:
    frames = partie.split()
    score = 0
    for frame in frames:
        if frame!="--":
            score += sum(int(x) for x in frame)
    return score

# def bowling2strike(partie: str) -> int:
#     frames = partie.split()
#     score = 0
#     i = 0
#
#     while i < len(frames):
#         frame = frames[i]
#         if frame == "X":
#             score += 10
#             if i + 1 < len(frames):
#                 if frames[i + 1] == "X":
#                     score += 10
#                 else:
#                     score += sum(int(x) for x in frames[i + 1])
#             if i + 2 < len(frames):
#                 if frames[i + 2] != "--":
#                     score += sum(int(x) for x in frames[i + 2])
#             i += 1
#         else:
#             score += sum(int(x) for x in frame)
#         i += 1
#
#     return score