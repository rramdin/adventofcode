all: advent7

CCFLAGS=-std=c++11 -g

advent7: advent7.o Gates.o
	g++ -o $@ $^

advent7.o: Gates.o advent7.cpp
	g++ -c $(CCFLAGS) $?

%.o: %.cpp
	g++ -c $(CCFLAGS) $?

clean:
	rm *.o advent7
