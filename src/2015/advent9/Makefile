all: advent9

CCFLAGS=-std=c++11 -g

advent9: advent9.o Graph.o
	g++ -o $@ $^

%.o: %.cpp
	g++ -c $(CCFLAGS) $?

clean:
	rm *.o advent9
