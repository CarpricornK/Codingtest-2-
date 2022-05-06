import math

#입력받은 숫자가 소수인지 판별
#소수 : true | 소수 아니면 : false
def numberCheck(num) :
    # 0,1 은 소수가 아님
    if num == 0 or num == 1:
        return False
    else :

        # 2부터 입력받은 숫자의 제곱근 값까지 반복
        # 입력받은 값이 10이면 10^2 100번 반복
        # 그러나 100은 2의 배수로 반복 1번하고 종료됨
        for i in range(2, int(math.sqrt(num)) + 1) :

            if num % i == 0:
                return False
    return True


print(numberCheck(32))



















