def solution(A):
    target = 10
    bricks_needed = (sum(A) + len(A) - 1) // target
    if sum(A) % target != 0:
        return -1
    return len(A) - 1 - A.index(min(A) if min(A) < 0 else len(A) - 1)