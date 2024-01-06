start = int(input())
end = int(input())

firstStart = start // 1000
secondStart = (start // 100) % 10
thirdStart = (start // 10) % 10
fourthStart = start % 10

firstEnd = end // 1000
secondEnd = (end // 100) % 10
thirdEnd = (end // 10) % 10
fourthEnd = end % 10

for i in range(firstStart, firstEnd + 1):
    for j in range(secondStart, secondEnd + 1):
        for k in range(thirdStart, thirdEnd + 1):
            for l in range(fourthStart, fourthEnd + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
                    print(f"{i}{j}{k}{l}", end=" ")

