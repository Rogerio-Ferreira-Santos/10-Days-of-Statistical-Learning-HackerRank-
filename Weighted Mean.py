def avg_weight(values, weights):
    final_values = []
    i = 0
    while(i < len(values)):
        final_values.append(values[i]*weights[i])
        i+=1
    
    result = sum(final_values)/sum(weights)

    print(round(result,1))







if __name__ == '__main__':
    array_lenght = input()
    values = list(map(float, input().split()))
    weights = list(map(float, input().split()))

    avg_weight(values,weights)
