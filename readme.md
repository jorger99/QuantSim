# PROJECT TITLE

## Project Summary

yeet

## Code Workflow

three main code sections that will interface with each other

- 'quantsim' objects defined via python class, self-contained quantum simulations

- 'playground' where quantsims will be run through a user-defined set of experiments

- 'visualizer' is the front end where quantsims will be plotted, either before or after their simulations are run

ideal usage:

1) quantsim object initialized; wavefunction, potential, experimental values, and simulation parameters are specified. OPTIONAL: quantsim fed to visualizer 
    - square well before would only show experimental values
    - tunneling particle should show experimental values
    - wave packet should show static wfn $\Psi(t=0)$


2) quantsim object fed to playground, experimental & simulation parameters are read, wavefunction is detected and then appropriate TISE is applied
    - honestly, TISE should be established as a property of quantsim obj, determining the correct one would be difficult


3) quantsim object now has data for visualizer to plot. this is the most difficult part since different quantum problems have different solutions. 
    - square well should show an X amount of harmonic modes
    - tunneling particle should show the potential, exponential & harmonic wavefunctions, and transmission/reflection amplitudes
    - wave packet should show time evolution and dissipation


### Quantsims

A "Quantsim" is an object created from the QuantumSimulationObject class defined in the QuantSimObj.py file. This function has its own .py file in order to isolate and define the quantum objects prior to being experimented on.

Important QuantSim features:

- wavefunction $(\Psi)$ definition [assumed potential]
    - harmonic modes [sq. well]  
    - tunneling particle [V = 0]
    - non-normalized free particle [V != $\inf$]
    - wave packet free particle [V != $\inf$]


- experimental parameters
    - [sq well] how many modes to show, if any
    - [sq well] potential well, depth
    - [tunneling particle] potential barrier height
    - [free particle] use wavepacket or not
 
 
- simulation values: 
    - m, q, k, E, $\omega$


Baseline QuantSims:

- Example 1: square well
    - wavefunction: sines and cosines
    - potential: V=$\inf$ at x=0, x=L, V=0 elsewhere
    - m = 2, k = 5, E = 32eV
    
    
- Example 2: tunneling particle
    - wavefunction: sines and cosines for trapped, exponential for tunneled
    - potential: V=60eV at x=L, V=0 elsewhere
    - m = 2, k = 5, E = 40eV
    
    
- Example 3: free particle
    - wavefunction: sines and cosines, or wave packet
    - potential: V=0 everywhere
    - m =2, k = 5, E = 30eV
    - show time evolution and dissipation!