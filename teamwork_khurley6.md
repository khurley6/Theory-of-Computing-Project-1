Theory of Computing Project 1 readme 

1. Team name: Katie Hurley

2. Names of all team members: Katie Hurley

3. Link to github repository: https://github.com/khurley6/Theory-of-Computing-Project-1.git

4. Which project options were attempted: 
- Implementing a Polynomial 2SAT solver using the DPLL algorithm and including unit propagation.

5. Approximately total time spent on project: 
- This project took me two weeks to complete.

6. The language you used, and a list of libraries you invoked: 
- Python- csv, time, os, matplotlib

7. How would a TA run your program (did you provide a script to run a test case?): 
- A TA should type "python3 SATdpll.py" into the terminal, and when asked for a file, type "test_case". The program with then run through the test files, check satisfiability, and output a graph of time vs size.

8. A brief description of the key data structures you used, and how the program functioned.
- The key data structures used in this program are lists for CNF, times, and sizes, and dictionaries for the assignments. The CNF list contains clauses composed of integer literals. The times and sizes lists store the execution times for the dpll algorithm, and the number of clauses, respectively. The assignments dictionary holds variable assignments in key-value pairs.
- The program will first prompt the user for the test case file, then it loops through all of the test cases (files provided). For each of these files, the program processes the CNF data and calls a DPLL algorithm, using unit propogation, to determine the satisfiability of each case.

9. A discussion as to what test cases you added and why you decided to add them (what did they tell you about the correctness of your code). Where did the data come from? (course website, handcrafted, a data generator, other)
- The test cases I used were meant to reflect the example test cases given on canvas and in the CNF format file. I was able to determine they were run correctly because the output of my script tells me if they were satisfied, and how long the execution time was.

10. An analysis of the results, such as if timings were called for, which plots showed what? What was the approximate complexity of your program?
- This program reveals that the DPLL algorithm can vary based on the size and structure of the CNF being analyzed at a given time. The visualizations show that the test files with more clauses included have a greater execution time.

11. A description of how you managed the code development and testing.
- I researched a bit about the DPLL algorithm and what goes into it. That is how I found unit propogation and I also found pseudocode that helped me a lot in writing my functions. I also refered to old classes, like Engineering computing and systems programming when it came to file handling and plottong.
https://fanpu.io/blog/2021/a-dpll-sat-solver/ - The pseudocode I used to guide my process

12. Did you do any extra programs, or attempted any extra test cases
- No.
