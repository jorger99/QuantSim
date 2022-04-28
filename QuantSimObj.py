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
    wfn : str
        xx
        
    Methods
    -------
    info(additional=""):
        xx
    """
    
    avail_sys = {
        1 : "Infinite Square Well",
        2 : "Finite Square Well",
        3 : "Quantum Harmonic Oscillator",
    }

    def __init__(self, choice="none"):
        """
        Constructs all the necessary attributes for the quantsim object. If no system is specified, asks user to pick a system.

        Parameters
        ----------
            choice : str or int
                str - name of system, see case below for options  
                      %TODO create dict for system names
                int - alternative for str
          
        """
        
        # start initialization by determining what system to run
        # if user does not specify, then choice is "none" and we will prompt
        if choice == "none":
            choice = input("""Please pick a system to simulate:
                                \n[1] Infinite Square Well
                                \n[2] Finite Square Well
                                \n[3] Quantum Harmonic Oscillator Potential Well
                                \n\n Enter a number from 1-3: """)
            
        # save choice, whether prespecified or from prompt
        self.sys = self.avail_sys[choice]
        
        # use if/elif/else to emulate a switch/case and assign correct values
        if choice == 1 or choice == "Infinite Square Well" or choice == "ISW":
            self.wfn = "\sqrt(\\frac{L}{2}) sin(k_n x) e^{i E_n t/ \hbar}"
            self.energy = "\\frac{n^2 \hbar^2 \pi^2}{2 m L^2} "
            
        elif choice == 2 or choice == "Finite Square Well" or choice == "FSW":
            pass
        
        elif choice == 3 or choice == "Quantum Harmonic Oscillator" or choice == "QHO":
            pass
        
        else:
            print("System not found.")
            

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
