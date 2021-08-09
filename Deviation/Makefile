THISDIR   =  $(shell pwd)
#CLASSPATH =  ${THISDIR}/antlers/antlr-4.5-complete.jar
CLASSPATH =  ${THISDIR}/antlers/antlr-4.9.2-complete.jar
ANTLR     =  "java -Xmx500M -cp ${CLASSPATH} org.antlr.v4.Tool"


all:
	@echo ''
	@echo 'Here are the targets:'
	@echo ''
	@echo 'To regenerate the antlr4 python code :  "make antlr"'
	@echo 'To develop                           :  "make develop"'
	@echo 'To test                              :  "make check"'
	@echo 'To pylint                            :  "make lint"'
	@echo ''



antlr:
	make -C deviation/antlr antlr ANTLR=${ANTLR}


#local editable install for developing
develop:
	pip install -e .


check: tasks unsats frontier incrementals tower

tasks:
	./scripts/tasks.py &> /tmp/tasks.log
	diff ./tests/tasks_10_19_18_log.txt /tmp/tasks.log
	echo "tasks OK"

unsats:
	./scripts/unsats.py &> /tmp/unsats.log
	diff ./tests/unsats_10_19_18_log.txt /tmp/unsats.log
	echo "unsats OK"

frontier:
	./scripts/frontier.py &> /tmp/frontier.log
	diff ./tests/frontier_10_19_18_log.txt /tmp/frontier.log
	echo "frontier OK"

incrementals:
	./scripts/incrementals.py &> /tmp/incrementals.log
	diff ./tests/incrementals_10_19_18_log.txt /tmp/incrementals.log
	echo "incrementals OK"

tower:
	./scripts/tower.py &> /tmp/tower.log
	diff ./tests/tower_10_19_18_log.txt /tmp/tower.log
	echo "tower OK"


clean:
	rm -f tests/*.pyc deviation/*.pyc deviation/*/*.pyc deviation/*/*~


very_clean: clean
	make -C deviation/antlr clean


PYLINT = $(shell which pylint)

lint:
ifeq ($(PYLINT),)
	$(error lint target requires pylint)
endif
	@ $(PYLINT) --rcfile=.pylintrc \
	deviation/*.py                 \
    deviation/logic/*.py           \
    deviation/visitor/*.py         \
    deviation/util/*.py
