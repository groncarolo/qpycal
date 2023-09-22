SRC=\
qconsole.py \
qcustomgate.py \
qgates.py \
qjson.py \
qlexer.py \
qparser.py \
qpycalc.py \
qsolver.py \
qstates.py \
qunitary.py \
qutils.py \
qvisualization.py


all: tests

tests:
	coverage run -m pytest test_*.py
	coverage report -m

pylint:
	pylint --good-names "a,b,c,d,f,g,i,j,o,p,ph,r,s,s1,s2,t,th,v,x,y,z" $(SRC)

flake:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

show_md:
	grip --quiet -b readme.md

run:
	python qpycalc.py
