from sys import stdin, stdout

def f(case0, case1, number):
    if number == 0:
        result = case1
    else:
        result = f(case1, case0+case1, number-1)
    return result
def main():
    N = stdin.readline().strip()
    while N != '':
        x,y = stdin.readline().split()
        value = str(f(int(x),int(y),int(N)))
        string = f'El {N}-nombre es: {value}\n'
        stdout.write(string)
        N = stdin.readline().strip()

if __name__ == '__main__':
    main()
