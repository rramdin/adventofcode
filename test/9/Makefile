all: test

CCFLAGS=-std=c++11 -g -I . ../../src/advent9/Graph.cpp

test: test.o Graph.o
	g++ -o $@ $^

%.o: %.cpp
	g++ -c $(CCFLAGS) $?

clean:
	rm *.o test
