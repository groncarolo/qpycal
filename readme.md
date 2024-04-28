# qpycalc


qpycalc is a quantum circuit calculator

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
X Pauli Gate NOT rotation of 180 deg on X axis

```python
qpycal> solve |0> X
[[0.+0.j]
 [1.+0.j]]
```


### Y Gate
Y Pauli Gate rotation of 180 deg on Y axis

```python
qpycal> solve |+> Y
[[0.-0.70710678j]
 [0.+0.70710678j]]
```


### Z Gate
Z Pauli Gate rotation of 180 deg on Z axis

```python
qpycal> solve |i> Z
[[0.70710678+0.j        ]
 [0.        -0.70710678j]]
```

### H Gate
H Hadamard gate

```python
qpycal> solve |0> H
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


### X Generic Gate
X Pauli Gate rotation of \theta rad or deg on Z axis

```python
qpycal> solve |i> X(pi/4.0)
[[ 0.85355339+0.35355339j]
 [-0.14644661+0.35355339j]]

solve |i> X(45.0)
[[4.32978028e-17+7.07106781e-01j]
 [7.07106781e-01-4.32978028e-17j]]

```

### Y Generic Gate
Y Pauli Gate rotation of \theta rad or deg on Z axis

```python
qpycal> solve |-i> Y(pi/2.0)
[[1.11022302e-16+7.07106781e-01j]
 [7.07106781e-01-1.11022302e-16j]]
```

### Z Generic Gate
Z Pauli Gate rotation of \theta rad or deg on Z axis

```python
qpycal> solve |+> Z(pi/2.0)
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
qpycal> solve |+> Z(pi/4.0)
 |+> R
     0
values:
[[0.70710678+0.j ]
 [0.5       +0.5j]]
mag^2:
[[0.500]
 [0.500]]
phase:
[[0.000]
 [45.000]]
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

### CNOT10
```python
solve |0>*|1> C*X
 |1> X
 |0> C
     0
values:
[[0.+0.j 1.+0.j]
 [0.+0.j 0.+0.j]]
```

Control and NOT can be non ajacent, like
```
X
.
.
.
C or A
```

### CNOT01
```python
qpycal> solve |0>*|1> X*C
 |1> C
 |0> X
     0
values:
[[0.+0.j 0.+0.j]
 [0.+0.j 1.+0.j]]
```
Control and NOT can be non ajacent, like
```
C or A
.
.
.
X
```

### TOFFOLI10
```
qpycal> solve |0>*|1>*|+> C*C*X
 |+> X
 |1> C
 |0> C
     0
values:
[[0.   +0.j 0.   +0.j]
 [0.707+0.j 0.707+0.j]
 [0.   +0.j 0.   +0.j]
 [0.   +0.j 0.   +0.j]]
```
Control and NOT can be non ajacent, like
```
X
.
.
C or A
.
.
C or A

```

### TOFFOLI01
```
qpycal> solve |0>*|1>*|+> X*C*C
 |+> C
 |1> C
 |0> X
     0
values:
[[0.   +0.j 0.   +0.j]
 [0.707+0.j 0.   +0.j]
 [0.   +0.j 0.   +0.j]
 [0.   +0.j 0.707+0.j]]
```

Control and NOT can be non ajacent, like
```
C or A
.
.
C or A
.
.
X
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

More complex example, adding two bits
```python
qpycal>

solve cout|0>*|0>*|0>*s|0>*|0>*b|1>*a|1>*cin|1> I*I*I*I*X*I*C*I I*I*I*I*X*C*I*I I*I*I*X*C*I*I*I I*I*I*X*I*I*I*C I*I*X*I*I*C*C*I I*X*I*I*C*I*I*C X*I*I*I*I*I*I*I X*A*A*I*I*I*I*I I*X*I*I*C*I*I*C I*I*X*I*I*C*C*I I*I*I*I*X*C*I*I I*I*I*I*X*I*C*I
 cin |1> I I I C I C I I C I I I
   a |1> C I I I C I I I I C I C
   b |1> I C I I C I I I I C C I
     |0> X X C I I C I I C I X X
   s |0> I I X X I I I I I I I I
     |0> I I I I X I I A I X I I
     |0> I I I I I X I A X I I I
cout |0> I I I I I I X X I I I I
         0         5        10
```
that gives

```python
values:
[[0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 1.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]]
mag^2:
[[0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 1.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]]
phase:
[[0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]
 [0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]]
Probability ON
 cin    a      b             s                    cout
[1.+0.j 1.+0.j 1.+0.j 0.+0.j 1.+0.j 0.+0.j 0.+0.j 1.+0.j]
```

so we add a + b + cin
and we get
```
s    = 1
cout = 1
```

there is a pre-define custom gate called sum
equivalently
```python
qpycal> solve cout|0>*|0>*|0>*s|0>*|0>*b|1>*a|1>*cin|1> G(sum)
 cin |1> I I I C I C I I C I I I
   a |1> C I I I C I I I I C I C
   b |1> I C I I C I I I I C C I
     |0> X X C I I C I I C I X X
   s |0> I I X X I I I I I I I I
     |0> I I I I X I I A I X I I
     |0> I I I I I X I A X I I I
cout |0> I I I I I I X X I I I I
         0         5        10
Probability ON
 cin    a      b             s                    cout
[1.+0.j 1.+0.j 1.+0.j 0.+0.j 1.+0.j 0.+0.j 0.+0.j 1.+0.j]
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
