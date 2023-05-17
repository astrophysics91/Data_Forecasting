Hi,

This code compares between a perfect model and a weak model to forecast a parameter detection in pulsar timing.
The basic idea is that the missed parameter causes a structure in the timing residuals.
Based on the likelihood method as well as fitting, this code forecasts the expected first detection time of the parameter.

Using this code requires

1. libstempo (see https://paper.dropbox.com/doc/So-you-want-to-install-enterprise-uhmTCxW0wm7mkCaanMwtx)
2. pandas
3. numpy
4. astropy
5. matplotlib


How to use this code?

First, you can add a specific parameter in the "Perfect_Model.par" either manually and a generator.
Second, run the code in the second section. This determined the likelihood, fitting values at a specific date for each realization ("num_sim")
Third, plot figures to see the result. Currently, the significance of the likelihood and the fitting exceeding three is the first detection criteria.

** I will update this manual and the code. Currently, the description is limited.
** Shapiro delay, PBDOT effect are only parameters you can add into "Perfect_Model.par" with the automatic parameter file generator.

Thank you

