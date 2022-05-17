cc = gcc -Wall
file = rand_test.c
bin = app.o

all: compile run

compile:
	@clear
	@$(cc) $(file) -o $(bin)

run:
	@./$(bin) 2
	
clean:
	@rm -f $(bin) *.out *.txt