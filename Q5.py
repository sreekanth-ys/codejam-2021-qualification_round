cases = int(input())
P = int(input())
for counter in range(cases):
    cheat = 0
    cheat1 = 0
    correct = 0
    correct1 = 0
    for i in range(0,100):
        answers = list(map(str,input().split()))
        #correct_temp = answers[0].count('1')
        wrong_temp = answers[0].count('0')
        correct_temp = answers[0][::2].count('1')
        correct_temp1 = answers[0][1::2].count('1')
        #print(correct_temp, correct, cheat)
        if(correct_temp > correct):
            correct = correct_temp
            cheat = i+1
        if(correct_temp1 > correct1):
            correct1 = correct_temp1
            cheat1 = i+1
    
    if(correct < correct1):
        cheat = cheat1 
    print("Case #%d: "%(counter+1),cheat)
