"""
A 'Quantsim' is an object created from the QuantSim class defined in this QuantSimObj.py file. I chose to develop this class inside of its own .py file in order to isolate the object-oriented programming from the physics numpy calculations. If I were to take this project further, I would be able to finish the class and leave it be as I use it to develop other software. For example, I am using this class to do simple quantum potential simulations, but in the future I could use this class in some kind of quantum canonical ensemble simulation (performance withstanding..)

"""

class QuantSim:
    """
    A class that defines a single object representing a single quantum mechanical system.


    Attributes
    ----------
    sys : str
        Possible Values:     %TODO define possible values in a dictionary
        "1", "Infinite Square Well", "ISW"
        "2", "Finite Square Well", "FSW"
        "3", "Quantum Harmonic Oscillator", "QHO"
        
    wfn : str
        latex equation for given wavefunction
        
    energy : str
        latex equation for energy levels of system
        
    sim_params : dict
        dictionary containing all the simulation parameters, e.g. mass, well depth, energy...
    
    Methods
    -------
    identify_sys
        this method will prompt the user to choose the quantum system they would like to simulate
        inputs:  self, choice
            self - quantsim object
            choice - equivalent to self.sys, this is the system this object represents
        outputs:
            returns nothing
            
    set_sim_params
        this method will prompt the user to input values for the quantum system simulation
        inputs: self
            self - quantsim object
        outputs:
            updates self.sim_params dictionary with appropriate values for given self.sys
            returns nothing
            
    info
        this method will make the object print several lines about the information it has gathered about its given quantum system
        inputs: self
            self - quantsim object
        outputs:
            returns nothing
    """

    def __init__(self, choice):
        """
        Python constructor that initializes the quantsim object, only run once!
        
        Parameters
        ----------
            choice : str
                str - name/identifier of system, see QuantSim docstring above for possible vals  
                          %TODO create dict for system names
        """
        # initialize object params to avoid AttributeErrors
        self.wfn = None
        self.energy = None
        self.sim_params = None
        
        # begin by identifying quantum system
        print("\n" + "~"*100)
        self.identify_sys(choice)
        
        
        
    def identify_sys(self, choice="none"):
        """
        This method will identify the quantum system to be simulated. If no choice is specified on method call, then this method will prompt for user input.
        
        Parameters
        ----------
            choice : str or int
                str - name/identifier of system, see QuantSim docstring above for possible vals  
                          %TODO create dict for system names
          
        """
        # start quantsim initialization by determining what system to run
        # if user does not specify, then choice defualts to "none" and we will prompt
        if choice == "none":
            choice = input("""Please pick a system to simulate:
                                \n[1] Infinite Square Well
                                \n[2] Finite Square Well
                                \n[3] Quantum Harmonic Oscillator (Quadratic Potential Well)
                                \n    Enter a number from 1-3: """)
            
        # save choice in object param, whether prespecified or from prompt
        self.sys = choice 
        
        # use if/elif/else and if in to emulate a switch/case and assign correct values
        if choice in ["1", "Infinite Square Well", "ISW"]:
            self.wfn = "\sqrt(\\frac{L}{2}) sin(k_n x) e^{i E_n t/ \hbar}"
            self.energy = "\\frac{n^2 \hbar^2 \pi^2}{2 m L^2}"
            
            print("\nInfinite Square Well chosen.")
            
        elif choice in ["2", "Finite Square Well", "FSW"]:
            print("\nFinite Square Well chosen.")
            pass
        
        elif choice in ["3", "Quantum Harmonic Oscillator", "QHO"]:
            print("\nQuantum Harmonic Oscillator in a Parabolic Square Well chosen.")
            pass
        
        
        else:
            print("\nSystem not found. Please retry.\n")
            self.identify_sys()  # run this method again with default param

        return
    
    def set_sim_params(self, use_default="1"):
        """ 
        This method will prompt user for simulation parameters.

        Parameters
        ----------
            quantsim - QuantSim object
                should be generated by QuantSimObj.py, then fed into this script

        Returns
        -------
        None

        """
        choice = self.sys
        
        # default values for simulation
        self.sim_params = {
           'mass' : 1,  
           'energy' : 1, 
           'length' : 12, 
           'dx' : 0.05, 
           'dt' : 0.01, 
        }  
        
        # go through each system's unique values, set defaults
        if choice in ["1", "Infinite Square Well", "ISW"]:
            self.sim_params['num_modes'] = 3  # number of modes
        elif choice in ["2", "Finite Square Well", "FSW"]:
            # no extra parameters
            pass    
        elif choice in ["3", "Quantum Harmonic Oscillator", "QHO"]:
            self.sim_params['num_modes'] = 3  # number of modes
            self.sim_params['force_constant_k'] = 3
            pass
        else:
            print("\nSystem not found. Please retry.\n")
            self.set_sim_params()  # restart method
        
        # prompt user if they want to use default values, but only if it is already set to 0l
        if use_default == "1":
            use_default = input("""\nWould you like to enter custom experimental values, or use the default?: 
                               \n    Enter 1 for default, 0 for manual entry: """)
        elif use_default == "0":
            print("Please choose your desired values for the following simulation parameters. Leave blank to keep default value. ")
            # loop over every existing default key in dict, then prompt for value
            for key in self.sim_params:
                user_input = input("    Enter value for {}, default is [{}]. ".format(key, self.sim_params[key]))
                if user_input == "":   # if input is empty, do not save it to dict
                    print("        Keeping default {}".format(self.sim_params[key]))
                else:
                    print("        Set {} to {}".format(key, user_input))
                    self.sim_params[key] = float(user_input)
                    
        else:
            print("Invalid entry. Please try again!\n")
            self.set_sim_params() # restart method

        print("\nFinished setting simulation parameters. Use quantsim.info() to inspect!")
        print("\n" + "~"*100)
    
        return 
    
    def info(self):
        """
        Prints information about the object


        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        
        print("\nReporting self.info()!:")
        print("------ Obj {} -----------".format(1))
        print("System chosen: " + str(self.sys))
        print("Wavefunction: " + str(self.wfn))
        print("Energy Levels: " + str(self.energy))
        print("Simulation Parameters:", self.sim_params)
        print("\n" + "~"*100)
        

