# Symplectically_self_polar_polytopes
This project has 4 different programms for computations connected with sympelctically self-polar polytopes.

1. **-1;0;1-self_polar_polytopes**:
   - This programm sort through all possible -1/0/1 symplectically self-polar polytopes and record their number of vertices and volume.
  
   - You can change dimension of generation. There is the variable "d" in the file "Generation_and_check.py". "d"  equals to half dimension of space.
   - Output file pointed in the file "Generation_and_check.py" in the function "recurtion_enum" and denoted by "volume_rec".
   - If you wanna run a programm, just run file "Generation_and_check.py".
   - IMPORTANT: Before runnning the programm delete existing output file.

2. **Random_self_polar_in_ball**:

    - This programm generates symplectically self-polar polytopes starting from polytope in unit euclidian ball.
    - There are following editable parameters:
      - Number of vertices of initial polytope. If you wanna generate initial centrally-symmetric polytope from $2k$ centrally-simmetric points. Change the second parametr of "rand_sphere" function in file "Rand.pl" to $k+1$.
      - Dimension. If you wanna generate polytopes in dimension $2d$ change first oarametr of "rand_sphere" function in file "Rand.pl" to $2d$.
      - Number of generated polytopes. Change number of "for" cycle in file "cycle.py"
    - Output file pointed in the file "create_self_polar.py" and denoted by "volume_rec".
    - If you wanna run a programm, just run file "cycle.py".

3. **Random_self_polar_in_polytope**:
    - This programm generates symplectically self-polar polytopes starting from polytope in fixed polytope.
    - Specify the vertices of fixed polytope in the file "Default.txt".
    - You can change number of generated polytopes. Change number of "for" cycle in file "cycle.py"
    - Output file pointed in the file "create_self_polar.py" and denoted by "volume_rec".
    - If you wanna run a programm, just run file "cycle.py".
    
4. **Self_polar_from_fix_polytope**:
    - This programm generates symplectically self-polar polytopes starting from fixed polytope.
    - Specify the vertices of your polytope in the file "Vertices.txt" and run programm by run file "create_self_polar.py"

If you have additional questions, please ask me through my email: m.berezovik@gmail.com
