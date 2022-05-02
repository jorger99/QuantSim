# Quantum Simulation Suite - QuantSim!

## Project Summary

This project was started for the purpose of Spring 2022 PHYS5070 Computational Physics. I set out to practice my library development skills to make my future code projects more modular and easy to use. We've all run into the classic problem of being handed an important code from ~5 years ago that runs over 1200 lines and you're expected to become an expert of exactly where everything is. 

I got my inspiration for using classes in this way from how contemporary libraries like Pandas and Scipy like to give you objects with self-contained methods.

I'd like to expand this project in the future to have more quantum systems, more flexible parameter tweaking, and eventually host this on a Github Pages website. Also, the object class and the methods associated with the object are separated into two files for pretty much no reason besides it helped me to code it that way.

## Project Workflow

This project has two main code sections that will interface with each other.

- The QuantSimObj.py file creates 'quantsim' objects defined via python class, these are self-contained quantum system simulations

- The QuantSimVisualizer.py file contains several methods where quantsims will be run through a user-defined set of experiments, and then will be plotted.

ideal usage:

1) quantsim object initialized; wavefunction, potential, experimental values, and simulation parameters are specified. OPTIONAL: quantsim fed to visualizer 
    - square well before would only show experimental values
    - tunneling particle should show experimental values
    - wave packet should show static wfn $\Psi(t=0)$


2) quantsim object fed to playground, experimental & simulation parameters are read, wavefunction is detected and then appropriate TISE is applied. Then, since quantsim object now has data for visualizer to plot, feed it into a plotting function and see the results. 
    - square well should show an X amount of harmonic modes
    - tunneling particle should show the potential, exponential & harmonic wavefunctions, and transmission/reflection amplitudes
    - wave packet should show time evolution and dissipation

## Project Outline

The rest of this README.md contains the outline I wrote for this project. A lot of the features are unimplemented, but I saved this here for future reference.

#### Quantsims

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
    - m, q, k, E, $\omega$


Current Example QuantSims (random values):

- Example 1: square well
    - wavefunction: sines and cosines
    - potential: V=$\inf$ at x=0, x=L, V=0 elsewhere
    - m = 2, k = 5, E = 32eV
    
- Example 2: quantum harmonic oscillator 
    - wavefunction: some dumb polynomial... zernike? hermite? who knows
    - potential: V= 1/2 k x^2 
    - m = 2, k = 5, E = 30eV
    
#### QuantVisualizer: Simulation

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
    
    
#### QuantVisualizer: Plotting

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