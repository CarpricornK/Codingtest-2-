def solution(brown, yellow):
    ab = brown + yellow

    for b in range(1, 13):

        if (ab / b) % 1 == 0:

            a = ab / b

            if a >= b:

                if 2 * a + 2 * b == brown + 4:
                    return [a, b]