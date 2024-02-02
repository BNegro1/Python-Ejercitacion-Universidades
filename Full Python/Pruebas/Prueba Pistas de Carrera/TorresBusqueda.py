def min_towers(cubes):
    n = len(cubes)
    towers = 1
    tower = [cubes[0]]
    for i in range(1, n):
        j = len(tower)-1
        while j >= 0 and tower[j] >= cubes[i]:
            j -= 1
        if j != len(tower)-1:
            tower[j+1] = cubes[i]
        else:
            tower.append(cubes[i])
            towers += 1
    return towers

n = int(input())
cubes = list(map(int, input().split()))
print(min_towers(cubes))
