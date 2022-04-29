"""
A 'Quantsim' is an object created from the QuantumSimulationObject class defined in the QuantSimObj.py file. This function has its own .py file in order to isolate and define the quantum objects prior to being experimented on.

Important QuantSim features:

- wavefunction $(\Psi)$ definition [assumed potential]
    - harmonic modes [sq. well]  
    - tunneling particle [V = 0]
    - non-normalized free particle [V != $\inf$]
    - wave packet free particle [V != $\inf$
 
 
- experimental values: 
    - m, q, k, E, $\omega$
"""

class QuantSim:
    """
    A class to represent a quantum mechanical system.

    ...

    Attributes
    ----------
    sys : str
        Possible Values:
        "1", "Infinite Square Well", "ISW"
        "2", "Finite Square Well", "FSW"
        "3", "Quantum Harmonic Oscillator", "QHO"
        
    Methods
    -------
    info(additional=""):
        xx
    """

    def __init__(self):
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
        self.exp_vals = None
        self.sim_params = None
        
        # begin by identifying quantum system
        self.identify_sys()
        
        
        
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

            
    def pick_exp_vals(self):
        """
        creates an experimental value dictionary based on the system choice, saves this dictionary as an object parameter
        
        Parameters
        ----------
            choice : str or int
                str - name/identifier of system, see QuantSim docstring above for possible vals  
        
        Returns
        -------
        None
        
        """
        choice = self.sys
        
        # prompt user for how to choose experimental values
        use_default = input("""\nWould you like to enter custom experimental values, or use the default?: 
                                \n    Enter 1 for default, 0 for manual entry: """)
        
        # use if/elif to choose value picking mode
        if use_default == "1":
            # determine the system, then set experimental values accordingly
            # start with experimental values shared by all systems
            # add extra values by dict[key] = value assignment
            
            self.exp_vals = {
                'mass' : 1,  
                'energy' : 1, 
                'length' : 12, 
            }  
            
            # go through each system's unique values
            if choice in ["1", "Infinite Square Well", "ISW"]:
                # no extra parameters
                pass
            elif choice in ["2", "Finite Square Well", "FSW"]:
                # potential barrier height  (V_0)
                pass
            elif choice in ["3", "Quantum Harmonic Oscillator", "QHO"]:
                # quadratic potential coefficient K (V = 1/2 K x^2)
                self.exp_vals['force_constant_k'] = 3
                pass
            else:
                print("\nSystem not found. Please retry.\n")

            print("\nSet experimental values to default. Use quantsim.info() to inspect!")
            
        elif use_default == "0":
            print("Manual implementation WIP.")
            self.pick_exp_vals()  # restart method
        else:
            print("Invalid entry. Please try again!\n")
            self.pick_exp_vals()  # restart method
        
        return 

    def set_sim_params(self):
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

        # prompt user for how to choose simulation parameters
        use_default = input("""\nWould you like to enter custom experimental values, or use the default?: 
                               \n    Enter 1 for default, 0 for manual entry: """)
        if use_default == "1":
           # determine the system, then set experimental values accordingly
           # start with experimental values shared by all systems
           # add extra values by dict[key] = value assignment

            self.sim_params = {
               'dx' : 0.05,  # 100 data points
               'dt' : 0.01, 
            }  

            # go through each system's unique values
            if choice in ["1", "Infinite Square Well", "ISW"]:
                self.sim_params['num_modes'] = 3  # number of modes
                self.sim_params['do_animate'] = True
            elif choice in ["2", "Finite Square Well", "FSW"]:
                # no extra parameters
                pass    
            elif choice in ["3", "Quantum Harmonic Oscillator", "QHO"]:
                self.sim_params['num_modes'] = 3  # number of modes
                pass
            else:
                print("\nSystem not found. Please retry.\n")
                self.set_sim_params()  # restart method

            print("\nSet simulation parameters to default. Use quantsim.info() to inspect!")

        elif use_default == "0":
            print("Manual implementation WIP.")
            self.set_sim_params()  # restart method
        else:
            print("Invalid entry. Please try again!\n")
            self.set_sim_params() # restart method
            
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
        
        print("\nReporting Quantsim Object info:")
        print("------ Obj {} -----------".format(1))
        print("System chosen: " + str(self.sys))
        print("Wavefunction: " + str(self.wfn))
        print("Energy Levels: " + str(self.energy))
        print("Experimental Values:", self.exp_vals)
        print("Simulation Parameters:", self.sim_params)
        

