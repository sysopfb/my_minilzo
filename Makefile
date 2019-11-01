all:
	gcc -I. -fPIC -c minilzo.c
	gcc -I. -shared -Lstatic -fPIC -o minilzo.so minilzo.o

clean:
	rm minilzo.o
	rm minilzo.so
