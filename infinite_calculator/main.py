# This is a simple beginner's python calculator.
import sys

while True:
    class user_input():
        math_problem = input("Your mathematical problem (input without space):")

        if math_problem.isalpha() == True:
            print("You are only allowed to use numbers in your mathematical problem.")
            sys.exit()

        math_operation = ["+", "-", "*", "/"]
        for i in math_operation:
            if i in math_problem:
                value_checker = math_problem.split(i)

        res = all(i.isdigit() for i in value_checker)
        if res == False:
            print("You are only allowed to use numbers in your mathematical problem.")
            sys.exit()

    class solution():
        def __init__(self, math_problem):
            self.math_problem = math_problem

        def solving(self):
            evaluation = eval(self.math_problem)
            return evaluation

    class output():
        solution = solution(user_input().math_problem)
        print(solution.solving())
