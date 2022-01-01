numdays = int(input("How many days high temperature ?: "))
temps = []
total = 0

for i in range(numdays): ## O(n)
    temp = float(input(f'Enter Day highest {i+1} temperature: '))
    total += temp
    temps.append(temp)

avg_temp = round(total/numdays,2) 
print('Average temperature: ',avg_temp)

count = 0
for val in temps: ## O(n)
    if val>avg_temp:
        count+=1

## space complexity of O(n) -> temps array

print(f'{count} days highest temperature was above the average highest temperature')