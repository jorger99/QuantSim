# PROJECT TITLE

## Project Summary

yeet

## Code Workflow

three main code sections that will interface with each other

- 'quantsim' objects defined via python class, self-contained quantum simulations

- 'quantsim playground' where quantsims will be run through a user-defined set of experiments

- 'visualizer' is the front end where quantsims will be plotted, either before or after their simulations are run

### Quantsims

A "Quantsim" is an object created from the QuantumSimulationObject class defined in the QuantSimObj.py file. This function has its own .py file in order to isolate and define the quantum objects prior to being experimented on.

Important QuantSim features:

- wavefunction $(\Psi)$ definition [assumed potential]
    - harmonic modes [sq. well]  
    - tunneling particle [V = 0]
    - non-normalized free particle [V != $\inf$]
    - wave packet free particle [V != $\inf$]
   
- simulation parameters: m, q, k, E, $\omega$


Example QuantSims:

- 