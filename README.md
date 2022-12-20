# Constraint-Satisfaction-Problem
The constraint satisfaction sudoku problem is approached through 4 parts: <br />
	&nbsp;&nbsp;1. The initial board must be input and properly formatted, mostly for aesthetic purposes <br />
	&nbsp;&nbsp;2. A coordinate system must be established to navigate the empty/zero assigned spaces <br />
	&nbsp;&nbsp;3. A function is created to triple verify each number to discern if that number falls withinthe constrains <br />
		&nbsp;&nbsp;&nbsp;&nbsp;a. With respect to the row <br />
		&nbsp;&nbsp;&nbsp;&nbsp;b. With respect to the column <br />
		&nbsp;&nbsp;&nbsp;&nbsp;c. With respect to the 3x3 box <br />
	&nbsp;&nbsp;4. The backtracking algorithm must be created <br />
		&nbsp;&nbsp;&nbsp;&nbsp;a. Establish zeros as the search space <br />
		&nbsp;&nbsp;&nbsp;&nbsp;b. Then, iterate through 1-9, checking to see if a number meets the constraints. <br />
		If it does, place that digit at the coordinates of the zero. <br />
		&nbsp;&nbsp;&nbsp;&nbsp;c. Next, Recursively call the backtracking algorithm which again checks to see if  
		there are any zeros remaining. Continue recursion until the result is True <br />
		&nbsp;&nbsp;&nbsp;&nbsp;d. If/when the recursive call returns failure, set that coordinate back equal to zero because we have reached a dead end in the search place. (In setting that coordinate back equal to zero we continue the process by iterating through the previous element in the zero space). <br />
        <br />
The initial and completed boards are provided for the easy and difficult boards. And lastly, an additional True or False statement is included to determine whether or not the puzzle is even possible. Chronological backtracking search streamlines efficiency while only eliminating impossible	combinations, so if there is a correct answer, the algorithm will find it.  


