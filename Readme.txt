Hi,

This code compares between a perfect model and a weak model to forecast a parameter detection in pulsar timing.
The basic idea is that the missed parameter causes a structure in the timing residuals.
Based on the likelihood method as well as fitting, this code indicates when the first detection of the parameter will be available.

This Python code requires those python packages:

1. libstempo (see https://paper.dropbox.com/doc/So-you-want-to-install-enterprise-uhmTCxW0wm7mkCaanMwtx)
2. pandas
3. numpy
4. astropy
5. matplotlib

How to use this code?

First, you can add a specific parameter in the "Perfect_Model.par", either manually or using a generator ("ephemeris_gen(incli,Invest,d)").
Second, run the code (in the second section). This determined the likelihood, fitting values at a specific date for each realization ("num_sim").
Third, plot figures to see the result. The significance (value/uncertainty) of the likelihood and the fitting results exceeding three is the first detection criteria.

** I will update this manual and the code. Currently, the description is limited.
** Shapiro delay, PBDOT effect are only parameters you can add into "Perfect_Model.par" with the automatic parameter file generator.

If you use this code, please cite the paper (It is still under review. Submitted to A&A)

Thank you

** contact mail: jjang@mpifr-bonn.mpg.de
