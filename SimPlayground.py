import numpy as np

""" 

This portion exists to isolate the quantsim object creation from numpy calculations. this script will accept any form of quantsim, and will run a simulation based on the predefined object properties of the quantsim.

This is where experimental parameters are important, the user will define for what values of x and t should the simulation run over, what the dx and dt values will be, and overall control everything that is related to the simulation of the system.


- simulation parameters
    - [sq well] how many modes to show, if any
    - [sq well] potential well, depth
    - [tunneling particle] potential barrier height, thickness
    - [free particle] use wavepacket or not
"""

def load_obj(quantsim):
    """
    This method will load any quantsim object, and save its system information as local variables within this script
    
    Parameters
    ----------
        quantsim - QuantSim object
            should be generated by QuantSimObj.py, then fed into this script
        
    Returns
    -------
        wasSuccessful - bool
            True if object was loaded successfully, False if not.
    
    """
    return wasSuccessful


def set_sim_params(quantsim):
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
    
    choice = quantsim.sys
        
    # prompt user for how to choose simulation parameters
    use_default = input("""\nWould you like to enter custom experimental values, or use the default?: 
                           \n    Enter 1 for default, 0 for manual entry: """)
    if use_default == "1":
       # determine the system, then set experimental values accordingly
       # start with experimental values shared by all systems
       # add extra values by dict[key] = value assignment
       
        quantsim.sim_params = {
           'dx' : quantsim.exp_vals['length']/100,  # 100 data points
           'dt' : 0.01, 
        }  
       
        # go through each system's unique values
        if choice in ["1", "Infinite Square Well", "ISW"]:
            quantsim.sim_params['num_modes'] = 3  # number of modes
            quantsim.sim_params['do_animate'] = True
        
        elif choice in ["2", "Finite Square Well", "FSW"]:
            # no extra parameters
            pass    
        
        elif choice in ["3", "Quantum Harmonic Oscillator", "QHO"]:
            # no extra parameters
            pass
        
        else:
            print("\nSystem not found. Please retry.\n")
            set_sim_params(quantsim)  # restart method
           
        print("\nSet simulation parameters to default. Use quantsim.info() to inspect!")
        
        
    elif use_default == "0":
        print("Manual implementation WIP.")
        set_sim_params(quantsim)  # restart method
        
    else:
        print("Invalid entry. Please try again!\n")
        set_sim_params(quantsim) # restart method
        
            
    return 

''' begin simulation methods '''

def InfSqWell(quantsim):
    L = quantsim.exp_vals['length']
    dx = quantsim.sim_params['dx']
    num_of_wfns = quantsim.sim_params['num_modes']
    wfn_solns = []
    
    # save x_vals to object, choose num to include end point
    # want 0 to 10, 0.1 steps; note that num = 10.1/0.1 = 101 data points, [0, 10.1)
    x_vals = np.linspace(0, L, num=(L+dx) / dx)  
    
    # make arrays of constants for each unique wfn
    n_array = np.arange(1, num_of_wfns+1)  # 1 to n+1 to include end point :)
    kn_array = np.pi * n_array / L

    for kn in kn_array:
        wfn_solns.append(np.sqrt(L/2) * np.sin(kn * quantsim.x_vals))
    
    # save useful arrays in sim_param dict
    quantsim.sim_params['x_vals'] = x_vals
    quantsim.sim_params['kn_array'] = kn_array
    
    return wfn_solns

def FinSqWell(quantsim):
    
    return

def ParabSqWell(quantsim):
    
    return

def simulate(quantsim):
    
    """
    This method will perform numpy calculations to simulate the correct equations for each physical system. Equations and wavefunctions are hardcoded in.
    
    Parameters
    ----------
        quantsim - QuantSim object
            should be generated by QuantSimObj.py, then fed into this script
        
    Returns
    -------
        
    
    """
    choice = quantsim.sys
    
    if choice in ["1", "Infinite Square Well", "ISW"]:
        wfn_soln = InfSqWell(quantsim)
        quantsim.soln = wfn_soln
        pass

    elif choice in ["2", "Finite Square Well", "FSW"]:
        quantsim.soln = FinSqWell(quantsim)
        pass

    elif choice in ["3", "Quantum Harmonic Oscillator", "QHO"]:
        quantsim.soln = ParabSqWell(quantsim)
        pass
    
    else:
        print("\nSystem not found. Please reinitialize object.\n")
    
    return
