
def average(n):
    mean = sum(n)/len(n)
    print(mean)



def median(n):
    numbers = sorted(n)
    if(len(n)%2 == 0):
        median1 = numbers[(len(n)//2)]
        median2 = numbers[(len(n)//2)-1] 
        median_final = (median1+median2)/2
        print(median_final)
    else:
        median1 = numbers[len(n)//2]
        print(median1)

def mode(n):
    i = 0
    freq = []
    n = sorted(n)
    while i < len(n):
        freq.append(n.count(n[i]))
        i+=1
    
    d1 = dict(zip(n,freq))
    
    mode = [k for (k,v) in d1.items() if v == max(freq)]
    print(str(mode[0]))


if __name__ == '__main__':
    array_lenght = int(input())
    n = list(map(int,(input().split())))

    average(n)
    median(n)
    mode(n)
