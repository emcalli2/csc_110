def differences(set_1,set_2):
    count = 0
    for x in set_1:
        if x not in set_2:
                count += 1
    for y in set_2:
        if y not in set_1:
                count += 1
    return count
        
print( differences({1, 2, 3}, {2, 3, 4, 5}) ) # 3
print( differences({'john', 'mark', 'paul'}, {'john', 'mark'}) ) # 1