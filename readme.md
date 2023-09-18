# qpycalc


qpycalc is a quantum gate calculator

Its aim is to solve small quantum circuits specified with Dirac's notation

It supports
- read-line input mode, with history
- CNOT10
- CNOT01
- TOFFOLI10
- TOFFOLI01
- Swap gate
- custom gates
- Rotation gates
- debug mode
- named bits


## Supported states:
qpycal supports these states
```python
|0>
|1>

|+>
|->

|i>
|-i>
```
you can also specify a states as
```python
[1.0/sqrt(2.0)|0> - 1.0/sqrt(2.0)|1>]
```

## Supported Gates:
qpycal supports the following gates

### X Gate
X: X Pauli Gate NOT rotation of 180 deg on X axis

```python
qpycal> solve |+>
[[0.707]
 [0.707]]
```


### Y Gate
Y: Y Pauli Gate rotation of 180 deg on Y axis

```python
qpycal> solve |+> Y
[[0.-0.70710678j]
 [0.+0.70710678j]]
```


### Z Gate
Z: Z Pauli Gate rotation of 180 deg on Z axis

```python
qpycal> solve |i> Z
[[0.70710678+0.j        ]
 [0.        -0.70710678j]]
```


### S Gate
S: Phase Gate rotation of 90 deg on Z axis

```python
qpycal> solve |i> S
[[ 0.70710678+0.j]
 [-0.70710678+0.j]]
```


### T Gate
T: T Gate rotation of \pi/8 deg on Z axis

```python
qpycal> solve |i> T
[[ 0.70710678+0.j ]
 [-0.5       +0.5j]]
```


### C Control Gate
C: Control Gate

```python
solve |i>*|0> X*C
 |0> C
 |i> X
     0
```

Giving as a result

```python
[[0.70710678+0.j         0.        +0.j        ]
 [0.        +0.70710678j 0.        +0.j        ]]
```

Controls can be non-adjacent like in

```python
solve |i>*|0>*|1> X*I*C
 |1> C
 |0> I
 |i> X
     0
```

Giving as a result

```python
[[0.        +0.j         0.        +0.70710678j]
 [0.        +0.j         0.        +0.j        ]
 [0.        +0.j         0.70710678+0.j        ]
 [0.        +0.j         0.        +0.j        ]]
```

You can have up to 2 controls per column,
that can again be non-adjacent to the NOT or in respect with each other


```python
solve |i>*|0>*|1>*|0> X*I*C*C
 |0> C
 |1> C
 |0> I
 |i> X
     0
```

Giving as a result

```python
[[0.        +0.j         0.        +0.j         0.        +0.70710678j 0.        +0.j        ]
 [0.        +0.j         0.        +0.j         0.        +0.j         0.        +0.j        ]
 [0.        +0.j         0.        +0.j         0.70710678+0.j         0.        +0.j        ]
 [0.        +0.j         0.        +0.j         0.        +0.j         0.        +0.j        ]]
```


### A Anti-Control Gate
```A: Anti Control Gate```

an anti-control will do where a control ```C``` works

```python
solve |0>*|1> A*X
 |1> X
 |0> A
     0
```
resulting in

```python
[[1.000 0.000]
 [0.000 0.000]]
```
### W Swap Gate
W: Swap gate
```python
solve |0>*|1> W*W
 |1> W
 |0> W
     0
```

Resulting in

```
[[0.000 0.000]
 [1.000 0.000]]
```


### I Identity Gate
I: Identity gate
This is the 2x2 identity gate


## Example
This is the simplest example: one single qubit and one single
gate in this case a NOT

```python
qpycal> solve qbit_name |+> X
qname |+> X
          0
values:
[[0.707]
 [0.707]]
mag^2:
[[0.500]
 [0.500]]
phase:
[[0.000]
 [0.000]]
```

More complex example
```python
qpycal> solve  [1.0/sqrt(2.0)|0> - 1.0/sqrt(2.0)|1>]*|1>*|+>*|1>*aaa|0> G(sum)*I*I X*Y*Z*X*I X*I*I*I*X X*Y*Z*X*I X*Y*Z*X*I X*Y*Z*X*I  G(sum)*I*I X*Y*Z*X*I  X*Y*Z*X*I  X*Y*Z*X*I  X*Y*Z*X*I  X*Y*Z*X*I
aaa               |0> I I I X I I I I I I I I I I
                  |1> I I X I X X X I I X X X X X
                  |+> I C Z I Z Z Z I C Z Z Z Z Z
                  |1> C I Y I Y Y Y C I Y Y Y Y Y
    0.707|0>-0.707|1> X X X X X X X X X X X X X X
                      0         5        10
```
that gives

```python
values:
[[0.+0.j  0.-0.5j 0.+0.j  0.+0.j ]
 [0.+0.j  0.+0.5j 0.+0.j  0.+0.j ]
 [0.+0.j  0.+0.j  0.+0.j  0.+0.j ]
 [0.+0.j  0.+0.j  0.+0.j  0.+0.j ]
 [0.+0.j  0.+0.5j 0.+0.j  0.+0.j ]
 [0.+0.j  0.-0.5j 0.+0.j  0.+0.j ]
 [0.+0.j  0.+0.j  0.+0.j  0.+0.j ]
 [0.+0.j  0.+0.j  0.+0.j  0.+0.j ]]
```


## Custom Gate Definition:

to add a custom gate please add a line in the dictionary in
```qcustomgate.py``` inside ``` get_custom_gate ``` method
like so
```python
def get_custom_gate(label):
    # left bottom
    # right top
    custom_gates = {"sum": CustomGate([[XGate(), Ctrl(), Identity()], [XGate(), Identity(), Ctrl()]], "sum")}
    g = custom_gates.get(label)
    return g
```
