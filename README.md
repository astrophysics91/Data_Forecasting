These codes compare between a perfect model and a weak model to forecast a parameter detection in pulsar timing.
The basic idea is that the missed parameter causes a structure in the timing residuals.
Based on the likelihood method as well as fitting, this code indicates when the first detection of the parameter will be available.

This Python code requires those python packages:

1. libstempo (see https://paper.dropbox.com/doc/So-you-want-to-install-enterprise-uhmTCxW0wm7mkCaanMwtx)
2. pandas
3. numpy
4. astropy
5. matplotlib


How to use this code?

A. If you already have TOAs and want to predict future trend (Known_Source)

- You need to specify your TOAs (original.csv) as well as timing ephemeris (sim_wt_pbd.par).
- Run "Data_Forecasting_With_a_Given_Data.ipynb". 
- Carefully check the setting.

  How many realizations? num_sim=80 

  The detection threshold (sigma)? sel=3

  Set feac: ef_cntrl=1.2

  Upgrade of telescope: meerkat_extension=60675

  Upgrade of telescope2: phase_ska=61465

  The interval of the observing days? days=90

  Random of observing date: obs_random_interval=0.3

  RMS level of your TOAs. In this example, I used rms of the current meerkat telescope mk_rms=4.76

  At each phase of telescope upgrade, the expected rms levels are calculated.

  phase1_rms=mk_rms*0.72

  phase2_rms=mk_rms*0.28


\n
\n
\n



B. If you want to simulate an imaginary pulsar (for multimessenger astrophysics, like LISA)

First, you can add a specific parameter in the "Perfect_Model.par", either manually or using a generator ("ephemeris_gen(incli,Invest,d)").
Second, run the code (in the second section). This determined the likelihood, fitting values at a specific date for each realization ("num_sim").
Third, plot figures to see the result. The significance (value/uncertainty) of the likelihood and the fitting results exceeding three is the first detection criteria.

** I will update this manual and the code. Currently, the description is limited.
** Shapiro delay, PBDOT effect are only parameters you can add into "Perfect_Model.par" with the automatic parameter file generator.

If you use this code, please cite the paper (It is still under review. Submitted to A&A)

Thank you

** contact mail: jjang@mpifr-bonn.mpg.de
