def solution(A):
    digit_sums = {}
    max_sum = -1

    for num in A:
        num_str = str(num)
        num_sum = sum(int(digit) for digit in num_str)
        if num_sum in digit_sums:
            max_sum = max(max_sum, num + digit_sums[num_sum])
    return max_sum        