Team Name: Katie Hurley

Team members names and netids: khurley6

Overall Project Attempted: Implementing a Polynomial 2SAT solver using the DPLL algorithm and including unit propagation.

Overall success of the project: The project went pretty well and the code ran correctly. The graph file, along with submitting the wrong readme file were the only discrepancies.

Approximately total time (in hours) to complete: 15 hours

Link to github repository:  https://github.com/khurley6/Theory-of-Computing-Project-1.git

List of included files: 
- Code files: SATdpll.py
Test Case Files: 
test_case_1.csv
test_case_2.csv
test_case_3.cnf
test_case_4.cnf
test_case_5.csv
test_case_6.csv
- Output files:
Project_1_Output.png
Project_1_Graph.png
- Timing plots:
Project_1_Graph.png
- Readme_team:
khurley6.md

Programming languages used, and associated libraries: Python- csv, time, os, matplotlib

Key data structures (for each sub-project): The key data structures used in this program are lists for CNF, times, and sizes, and dictionaries for the assignments. The CNF list contains clauses composed of integer literals. The times and sizes lists store the execution times for the dpll algorithm, and the number of clauses, respectively. The assignments dictionary holds variable assignments in key-value pairs.

General operation of code (for each subproject): 
The program will first prompt the user for the test case file, then it loops through all of the test cases (files provided). For each of these files, the program processes the CNF data and calls a DPLL algorithm, using unit propogation, to determine the satisfiability of each case.
A TA should type "python3 SATdpll.py" into the terminal, and when asked for a file, type "test_case". The program with then run through the test files, check satisfiability, and output a graph of time vs size.
The code implements the DPLL algorithm to check the satisfiability of CNF formulas. It starts by loading test cases from CNF or CSV files, parsing the clauses into a list of literals. For each test case, the DPLL algorithm recursively applies unit propagation (simplifying clauses by assigning truth values to unit clauses), selects variables to assign truth values, and backtracks when conflicts occur. The code also tracks and plots the execution time against the size of the CNF formulas for performance analysis.

Test Cases: 
The test cases I used were meant to reflect the example test cases given on canvas and in the CNF format file. I was able to determine they were run correctly because the output of my script tells me if they were satisfied, and how long the execution time was.
Code Development: In order to write this code, I did lots of research into the DPLL algorithm, then into unit propogation. I found pseudocode for both (attatched at the bottom), which guided me in writing the program. I also made sure that the test cases reflected those in the example file, which helped a lot. I also refered to old classes, like Engineering computing and systems programming when it came to file handling and plottong. https://fanpu.io/blog/2021/a-dpll-sat-solver/ - The pseudocode I used to guide my process.

Detailed discussion of results: This program reveals that the DPLL algorithm can vary based on the size and structure of the CNF being analyzed at a given time. The visualizations show that the test files with more clauses included have a greater execution time. The time complexity of the DPLL algorithm is O(2^n) in the worst case because it explores all possible truth assignments for the n variables in the CNF formula. For each unassigned variable, the algorithm recursively tries both possible truth values (True and False), leading to a binary branching tree with a depth of n. In the absence of optimizations like unit propagation or early termination, this results in an exponential growth of recursive calls, where the total number of possible assignments is 2^n, making the time complexity exponential.

How team was organized: I worked alone on this project, so I had to manage my time very well and work ahead.
What you might do differently if you did the project again: I think I might try to work with someone else if I were to do this project again, to get more opinions and learn from different styles of programming. 
