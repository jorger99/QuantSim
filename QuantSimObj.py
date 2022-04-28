import numpy as np

def test_method(x="sus"):
    print(x)
    return

print('test')

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

    def __init__(self, sys_choice="none"):
        """
        Constructs all the necessary attributes for the quantsim object. If no system is specified, asks user to pick a system.

        Parameters
        ----------
            sys_choice : str or int
                str corresponding to 
          
        """
        
     
            

    def info(self, additional=""):
        """
        Prints the person's name and age.

        If the argument 'additional' is passed, then it is appended after the main info.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        None
        """

        print(f'My name is {self.name} {self.surname}. I am {self.age} years old.' + additional)