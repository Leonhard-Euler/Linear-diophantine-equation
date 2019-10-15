# Linear-diophantine-equation
A Linear-diophantine-equation problem solved.

### Counting the number of non-negative solutions for a linear diophantine equation.
#### Example
```
x + y = 0

input: [1,1], 0
output: 1
```
```
x + y = 1

input: [1,1], 1
output: 2
```

```
x + y = 2

input: [1,1], 2
output: 3
```

```
x + y = 3

input: [1,1], 3
output: 4
```

```
x + y + z + k = 30

input: [1,1,1,1], 30
output: 5456
```

```
x + 2y + 3z + 4k = 30

input: [1,2,3,4], 30
output: 297
```
```
3x + 2y + z + k = 47

input: [3,2,1,1], 47
output: 2282
```

#### SolutionA: 
dynamic programming

# SolutionB:
let 𝑃𝑁(𝑎1,𝑎2,...,𝑎𝑁,𝑛) be the number of solutions to the linear Diophatine equation
