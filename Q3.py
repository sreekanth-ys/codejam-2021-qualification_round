def cost_func(l):
    cost = 0
    length = len(l);
    for i in range(0, length-1):
        minimum = l.index(min(l[i:length+1]))
        mini = minimum + 1
        l[i:mini] = reversed(l[i:mini])
        cost += (minimum - i +1)
    return cost;

def find_out(N,C):
    minimum = N-1;
    median = (2*N) - 2
    maximum = int((((N) * (N+1))/2) -1)
    cutoff = N + N - 1+ N - 3;
    #print(minimum, median,maximum)
    if(C == minimum) :
        result = (list(range(1,N+1)))
    elif (C > minimum and C < minimum + N):
        result = list(range(1,N+1))
        diff = C - minimum
        index = N - 1 - diff
        result.insert(index, result[N-1])
        result.pop()
    elif((C >= minimum + N) and (C <= cutoff )):
        result = list(range(1,N+1))
        result =  result[::-1]
        diff = C - (minimum + N) + 2
        result.insert(diff, result[0])
        result.pop(0)
    else:
        result = list(range(1,N+1))
        result[0] = 2
        result[N-1] = 1
        rem = C-(N+N-1)
        rem_num = N -2;
        result_internal = find_out(rem_num,rem);
        result_internal = [x+2 for x in result_internal]
        result[1:N-1] = result_internal[0:(rem_num+1)]
        #print(result_internal)
    return result

cases = int(input())

for counter in range(cases):
    N,C = list(map(int,input().split()))
    minimum = N-1;
    maximum = int((((N) * (N+1))/2) -1)
    if( C < minimum or C > maximum):
        print("Case #%d: IMPOSSIBLE"%(counter+1))
    else:
        result = find_out(N,C)
        print("Case #%d:"%(counter+1),*result)
