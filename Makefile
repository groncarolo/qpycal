
SRC=qgates.py \
qjson.py \
qlexer.py \
qparser.py \
qpycalc.py \
qstates.py \
qutils.py \
test_qgates.py \
test_qjson.py \
test_qparser.py \
test_qutils.py


all: tests

tests:
	pytest test_*.py

pylint:
	pylint --good-names "a,b,c,f,g,i,j,o,p,ph,r,s,s1,s2,t,th,v,x,y,z" $(SRC)
