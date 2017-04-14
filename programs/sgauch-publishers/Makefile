convert: convert.o hashtable.o
	g++ convert.o hashtable.o -o convert

convert.o : convert.cpp 
	g++ -Wall -c convert.cpp

hashtable.o : hashtable.cpp hashtable.h
	g++ -Wall -c hashtable.cpp

clean :
	rm *.o convert
