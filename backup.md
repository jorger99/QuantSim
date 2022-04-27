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
    - [tunneling particle] potential barrier height, thickness
    - [free particle] use wavepacket or not
 
 
- simulation values: 
    - m, q, k, E, $\omega$


Baseline QuantSims (random values):

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
    - m = 2, k = 5, E = 30eV
    - show time evolution and dissipation!
    
- Example 4: quantum harmonic oscillator 
    - wavefunction: some stupid polynomial... zernike? hermite? who knows
    - potential: V=kx^2 baby
    - m = 2, k = 5, E = 30eV
    - show time evolution!!
    
### QuantSim Playground

Should be easiest implementation, this portion exists to isolate the quantsim objects from the numpy calculations. this script will accept any form of quantsim, and will run a simulation based on the predefined object properties of the quantsim.

This is where experimental parameters are important, the user will define for what values of x and t should the simulation run over, what the dx and dt values will be, and overall control everything that is related to the calculation of the problems.

Baseline Playground Sims:

- Example 1: square well
    - wavefunctions will be sines and cosines, so solve the SE and fourier decompose to get the coefficients for the first N modes
    - once fourier coefficients are obtained, save them in an array to be plotted with matplotlib in the next section
    - perhaps show time evolution of these?

- Example 2: tunneling particle
    - wavefunctions will be a sine/cosine, or exponential, so solve the TISE in each region
    - show amplitude/reflection coefficients
    - need to find a way to identify bound & tunneling regions, perhaps first predefine them and then later on detect them?
    
- Example 3: free particle
    - wavefunction will be a wavepacket, time evolve it with the wiggle factor $e^{iE/\hbar t}$, show dissipation
    - is it even worth showing the non-normalized free particle? probably only interesting if it follows after a $\delta$ potential
    
- Example 4: quantum harmonic oscillator
    - wavefunction will be hermite polynomials, derive the coefficients for each mode and then time evolve
    - save coefficients for each mode for visualization
    - time evolution?
    
    
### Visualizer

This portion will include all the matplotlib code. All of the numpy number crunching should already be done, this section will take finalized arrays and then plot them accordingly.

this section will probably be the most rigid, in order to produce nice plots, the data will be forced to look a certain way

- Example 1: square well
    - plot potential barriers 
    - design choice: show each mode on its own subplot in a large grid, or show each mode stacked together on one large plot?
    
- Example 2: tunneling particle
    - plot potential barriers, thickness, perhaps include color
    - how to identify regions??

- Example 3: free particle
    - plot wavepacket and then time evolve it!!
    
- Example 4: quantum harmonic oscillator
    - plot potential, show value of k
    - design choice similar to square well, might want to do subplots since these get very messy