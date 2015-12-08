all: advent7

CCFLAGS="-std=c++11"

advent7: advent7.o Gates.o
	g++ -o $@ $?

%.o: %.cpp
	g++ -c $(CCFLAGS) $?
