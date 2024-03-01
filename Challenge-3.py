def solution(N):
    if N % 26 == 0:
        return ''.join(chr(i) for i in range(ord('a'), ord('z') + 1)) * (N * 26)
    else:
        return ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))[:N % 26] + ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))[:N % 26 - 1]
