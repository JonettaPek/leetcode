def fizz_buzz(n: int) -> list[str]:
    say = list()
    for number in range(1, n+1):
        if number % 15 == 0:
            say.append('FizzBuzz')
        elif number % 5 == 0:
            say.append('Buzz')
        elif number % 3 == 0:
            say.append('Fizz')
        else:
            say.append(str(number))
    return say

if __name__  == '__main__':
    print('\n'.join(fizz_buzz(100)))
