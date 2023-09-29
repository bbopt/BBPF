# BBPF

BBPF, Blackbox Power Flow

BBPF is a blackbox optimization problem instance for the Power Flow problem. 

 _____________________________________________________________________________________________________________________________________________
 
For a network with n generators, 0 slack bus and 1 external grid :

  Input  :  Pg1, Pg2, ..., Pgn, |vg1|, |vg2|, ..., |vgn|
  
                    Pg1, Pg2, ..., Pgn are generator active powers
                    |vg1|, |vg2|, ..., |vgn| are generator magnitude voltages

  Output :  f, CSTR   OR   f, CSTR1, CSTR2, ..., CSTRk
  
                    f > 0 is the operating costs of power system due to generators
                    f = np.inf if an error occurs in the BBPF such as no convergence during the Power Flow analysis
                    CSTR is the value of the aggregated constraint violation of all contraints
                    CSTR1, CSTR2, ..., CSTRk are the constraint violation of all contraints
                    CSTR = 0 if the constraint i is respected
                    CSTR > 0 if the constraint i is violated (higher value of constraint violation means more important constraint violations) 

 _____________________________________________________________________________________________________________________________________________

Run a BBPF instance : BBPF.py nb_buses nb_cstr x.txt

                    nb_buses : Number of buses: integer in {14, 39, 118}
                                Import the cooresponding network available on Pandapower

                    nb_cstr  : Number of output constraints: String in {-one or -all}
                                 -one : all constraints are agregated    : output = f, CSTR 
                                 -all : all constraint value are output  : output = f, CSTR1, CSTR2, ..., CSTRk 

                    x.txt    : Input vector in a txt file  : Point at which the simulator is evaluated
                                 Please use Help(2) to have input bounds for a specific network
                                 For a network with n generators, 0 slack bus and 1 external grid :
                                 input : x = Pg1, Pg2, ..., Pgn, |vg1|, |vg2|, ..., |vgn| 

 _____________________________________________________________________________________________________________________________________________

For more information :
                     Help (1) : BBPF.py -h
 
                     Install  : BBPF.py -i
 
                     Version  : BBPF.py -v
 
                     Help (2) : BBPF.py nb_buses -h
 
                     Run      : BBPF.py nb_buses nb_cstr x.txt
 

 _____________________________________________________________________________________________________________________________________________

Please install Python libraries numpy, pandapower and numba with these instructions :

                    pip install numpy      (to perform mathematical operations on arrays)
  
                    pip install pandapower (to load existing networks and run a Power Flow)
  
                    pip install numba      (to accelerate the Power Flow computation)
