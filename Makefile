SRC=\
qgates.py \
qjson.py \
qlexer.py \
qmath.py \
qparser.py \
qpycalc.py \
qstates.py \
qunitary.py \
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

flake:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

show_md:
	grip --quiet -b readme.md

run:
	python qpycalc.py
