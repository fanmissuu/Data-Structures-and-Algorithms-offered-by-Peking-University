#ac 完全自己编写
line = input().strip().split()
N = int(line[0])
S = int(line[1])
cost_deliver = []
for i in range(N):
    cost_deliver.append(input().strip().split())
#读入N weeks的cost&deliver
f = 0
f_cost = int(cost_deliver[f][0])
f_produ = int(cost_deliver[f][1])
produce_cost = 0
saving_cost = 0
for i in range(1,N):
    if f_cost + (i-f) * S < int(cost_deliver[i][0]):        #核心是：如果前序的生产成本+存储成本<后序生产成本，则前序生产
        f_produ += int(cost_deliver[i][1])
        saving_cost += S * (i-f) * int(cost_deliver[i][1])
    else:
        produce_cost += f_cost * f_produ
        f = i
        f_cost = int(cost_deliver[f][0])
        f_produ = int(cost_deliver[f][1])

print(produce_cost + saving_cost + f_cost * f_produ)
