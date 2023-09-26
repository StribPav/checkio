def checkio(time_string):

    numbers = ''.join(map(lambda n: n if len(n) == 2 else '0'+n, time_string.split(':')))
    numbers = [bin(int(n))[2:] for n in numbers]
    numbers = (f"{numbers[0].zfill(2)} {numbers[1].zfill(4)} : {numbers[2].zfill(3)} {numbers[3].zfill(4)} : {numbers[4].zfill(3)} {numbers[5].zfill(4)}")

    return numbers.replace('0','.').replace('1','-')

#the best
#def checkio(time_string):
#    h, m, s = map(int, time_string.split(':'))
#    return '{:02b} {:04b} : {:03b} {:04b} : {:03b} {:04b}'.format(h // 10, h % 10, m // 10, m % 10, s // 10, s % 10).replace('0', '.').replace('1', '-')
