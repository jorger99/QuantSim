import numpy as np

"""
A 'Quantsim' is an object created from the QuantumSimulationObject class defined in the QuantSimObj.py file. This function has its own .py file in order to isolate and define the quantum objects prior to being experimented on.

Important QuantSim features:

- wavefunction $(\Psi)$ definition [assumed potential]
    - harmonic modes [sq. well]  
    - tunneling particle [V = 0]
    - non-normalized free particle [V != $\inf$]
    - wave packet free particle [V != $\inf$]


- experimental parameters
    - [sq well] how many modes to show, if any
    - [sq well] potential well, depth
    - [tunneling particle] potential barrier height, thickness
    - [free particle] use wavepacket or not
 
 
- simulation values: 
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

    def __init__(self, choice):
        """
        Python constructor that initializes the quantsim object, only run once!
        
        Parameters
        ----------
            choice : str
                str - name/identifier of system, see QuantSim docstring above for possible vals  
                          %TODO create dict for system names
        """
        
        
        self.identify_sys(choice)
        
        
    def identify_sys(self, choice="none")
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
                                \n\n Enter a number from 1-3: """)
            
        # save choice in object param, whether prespecified or from prompt
        self.sys = choice 
        
        # use if/elif/else to emulate a switch/case and assign correct values
        if choice in ["1", "Infinite Square Well", "ISW"]:
            self.wfn = "\sqrt(\\frac{L}{2}) sin(k_n x) e^{i E_n t/ \hbar}"
            self.energy = "\\frac{n^2 \hbar^2 \pi^2}{2 m L^2}"
            
        elif choice in ["2", "Finite Square Well", "FSW"]:
            pass
        
        elif choice in ["3", "Quantum Harmonic Oscillator", "QHO"]:
            pass
        
        else:
            print("System not found. Please retry.")
            self.set(choice="none")

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
        
        print("\nInfo Requested:\n")
        print("System chosen: " + str(self.sys))
        print("Wavefunction: " + str(self.wfn))
        print("Energy Levels: " + str(self.energy))
