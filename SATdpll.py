import csv
import time
import os
import matplotlib.pyplot as plt #for plotting 

def main():
    file = input("Please enter the base name of the file you would like to use (without extension): ")
    times = []
    sizes = []
    
    for i in range(1, 7):  # creating 10 test cases
        cnf_file = f'{file}_{i}.cnf' #formatting for cnf files
        csv_file = f'{file}_{i}.csv' #formatting for csv files
        
        CNF = [] #create a CNF list
        if os.path.exists(cnf_file): #check if a CNF file exists for the given test case
            CNF, _ = create_cnf(cnf_file) #create the CNF from the cnf file
        elif os.path.exists(csv_file): #check if a CSV file exists for the given test case
            CNF, _ = create_cnf(csv_file) #create the CNF from the csv file
        else:
            print(f"File {cnf_file} or {csv_file} does not exist. Skipping this one.") #if the file does not exists
            continue  # Skip to the next iteration if neither file exists

        assignment = {} #create assignment dictionary to be used in later functions
        
        #set timers for DPLL execution
        start_time = time.time()
        result = dpll(CNF, assignment) #obtain result from dpll algorithm
        end_time = time.time()
        exec_time = end_time - start_time #calculate execution time
        times.append(exec_time) #append the time taken for each test case
        sizes.append(len(CNF)) #append the number of clauses to sizes list
        
    #display result
        if result != None:
            print(f"Case {i}: Satisfiable in {exec_time:.6f} seconds")
        else:
            print(f"Case {i}: Unsatisfiable in {exec_time:.6f} seconds")
            
    plot_time_size(times, sizes) #plot the times vs the sizes of the cnf

    
    
def create_cnf(f):
    '''Returns a list of clauses from a CSV or CNF file'''
    clauseList = []
    variables= 0
    clauses = 0
    with open(f, 'r') as file:
        if f.endswith('.csv'):  # if the file is a csv file
            csv_file = csv.reader(file)  # use the csv library
            for row in csv_file:
                if row[0].startswith('c'):
                    continue  # just describing the problem
                elif row[0].startswith('p'):
                    # Read the problem line (e.g., "p cnf 3 5")
                    vars_clauses = row
                    variables = int(vars_clauses[2])
                    clauses = int(vars_clauses[3])
                else:  # the clause lines
                    if row:  # ensure the row is not empty
                        clause = [int(literal) for literal in row[:-1]]  # convert literals to integers and get rid of the trailing 0
                        clauseList.append(clause)  # add the clause to the initialized clause list
        elif f.endswith('.cnf'):  # if the file is a cnf file
            for line in file:
                line = line.strip()  # remove whitespace and set that as the current line
                if line.startswith('c'):  # describing the problem type
                    continue  # just describing the problem
                elif line.startswith('p'):  # indicating that it is a cnf file with however many variables and clauses
                    vars_clauses = line.split()  # the following parts of the line indicate how many variables and how many clauses
                    variables = int(vars_clauses[2])  # convert to int because they are strings
                    clauses = int(vars_clauses[3])  # convert to int because they are strings
                else:  # in this case, it is the clause lines
                    if line:  # ensure the line is not empty
                        clause = [int(literal) for literal in line.split()[:-1]]  # need to get rid of the trailing 0 and convert literals to integers
                        clauseList.append(clause)  # add the clause to the initialized clause list
    return clauseList, False
    
def unit_propagation(clauseList, assignment): #unit propogation part of the DPLL algorithm
    '''Performs unit propogation where if a clause has an unassigned literal, it assigns that literal'''
    while True:
        unit_clauses = [clause for clause in clauseList if len(clause) == 1]
        if not unit_clauses: #no unit clauses left
            break
        
        for unit in unit_clauses:
            literal = unit[0] #since each unit clause contains only one literal, this will extract that literal from the unit clause
            if literal > 0:
                assignment[literal] = True #if it is positive, it is true
            else:
                assignment[-literal] = False #if it is negative, it is false. If the literal is negative, we assign the positive variable as false.
    
            clauseList = simplify_and_choose(clauseList, assignment)[0] #simplify the clauses
    
        if any(len(clause) == 0 for clause in clauseList): #no more left
            return clauseList, True
    
    return clauseList, False

def simplify_and_choose(clauseList, assignment):
    '''Simplify clauses: assign value to a variable then choose the next unassigned variable for splitting (for dpll)'''
    clauses = []
    next_one = None
    
    for clause in clauseList: #loop over each clause and check if clause is satisfied by current assignment
        for literal in clause: #loop over the literals in the clauses
            variable = abs(literal) #does not matter the sign of the literal when assigning it to a variable
            if variable not in assignment:
                next_one = variable #set it as the next variable to assign
                break
        if next_one != None:
            break #you can stop after finding the next variable
    
    #skip any satisfied clauses
    for clause in clauseList:
        satisfied = False #set a flag to track if clause is satisfied 
        for literal in clause:
            if abs(literal) in assignment: #see if the literal's absolute valuse is assigned already
                assigned_val = assignment.get(abs(literal)) #get the assigned value of the literal (True of False)
                if (literal > 0 and assigned_val == True) or (literal < 0 and assigned_val == False): #condition for the clause to be satisfied
                    satisfied = True #set the satisfied flag to true
                    break #keep looping if it is not satisfied, but break if it is satisfied
                
        if satisfied:
            continue #if the clause is satisfied go to the next one
        
        #remove any false literals from the clause based on current assignment (if literal > 0 and False or literal < 0 and True)
        new_clause = [literal for literal in clause if abs(literal) not in assignment or assignment.get(abs(literal)) != (literal < 0)] #keep any literals whose values have not been assigned or whose assignments do not make the clause false
        clauses.append(new_clause)
        
    return clauses, next_one 
        
                

              
#dpll algorithm should include recursion                    
def dpll(clauseList, assignment={}): #assignment is a dictionary where the keys are variables and denoted as the integers and the values are true or false
    '''DPLL algorithm for checking satisfiability of a CNF'''
    if not clauseList: #base case for if the formula is satisfied
        return assignment
    
    if any(len(clause) == 0 for clause in clauseList):
        return None #empty clause- unsatisfiable
    
    clauseList, conflict = unit_propagation(clauseList, assignment) #perform unit propogation
    if conflict:
        return None #there is a conflicting assignment
    
    clauseList, next_one = simplify_and_choose(clauseList, assignment) #choose next variable
    if next_one == None:
        return assignment #this means that all variables are assigned
    
    #try to assign the next variable as True
    true_assignment = assignment.copy()
    true_assignment[next_one] = True 
    clause_true = simplify_and_choose(clauseList, true_assignment)[0] #simplify the clause, extract simplified clause (0 selects the first item from the returned pair which is the simplified clause list)
    result = dpll(clause_true, true_assignment) #recursive call to check if there is satisfiability for next
    if result != None: #there is a satisfying assignment
        return result
    
    #try assigning next variable as False
    false_assignment = assignment.copy()
    false_assignment[next_one] = False
    clause_false = simplify_and_choose(clauseList, false_assignment)[0] #simplify the clause, extract simplified clause (0 selects the first item from the returned pair which is the simplified clause list)
    
    return dpll(clause_false, false_assignment) #recursive call to continue searching for a satisfying assignment

def plot_time_size(sizes, times): #plot the execution time vs the size of the CNF
    '''Plots the execution time versis the size of the CNF problem'''
    plt.figure(figsize=(10, 6)) #initialize the plot
    plt.plot(times, sizes, marker='o', linestyle='-', color='b', label="Execution Time") #figure attributes
    plt.xlabel("Number of Clauses") #x-axis label
    plt.ylabel("Execution Time (seconds)") #y-axis label
    plt.title("DPLL Algorithm: Execution Time VS CNF Size") #graph title
    plt.grid(True) #turn grid on (optional)
    plt.yticks(ticks=plt.yticks()[0], labels=[f'{y:.6f}' for y in plt.yticks()[0]])
    plt.show() #show the plot
    plt.savefig('Project_1_Graph.png', format='png')  # Save the plot to a png file
    plt.close()  # Close the figure to free up memory
    
if __name__ == "__main__":
    main()     
        
        
        
    
    
    
    
