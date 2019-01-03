all:
	@echo 'To regenerate the antlr4 python code, do "make antlr"'


antlr:
	@echo "Using ${ANTLR}"
	${ANTLR} -Dlanguage=Python2 Deviation.g4 -visitor


clean:
	rm -f *.pyc D*.py *.tokens
