%global __brp_check_rpaths %{nil}
%global packname  BayesCTDesign
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Two Arm Bayesian Clinical Trial Design with and Without Historical Control Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-CRAN-eha >= 2.9.0
BuildRequires:    R-CRAN-survival >= 2.41.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
Requires:         R-stats >= 3.5.0
Requires:         R-CRAN-eha >= 2.9.0
Requires:         R-CRAN-survival >= 2.41.3
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-reshape2 >= 1.4.3

%description
A set of functions to help clinical trial researchers calculate power and
sample size for two-arm Bayesian randomized clinical trials that do or do
not incorporate historical control data.  At some point during the design
process, a clinical trial researcher who is designing a basic two-arm
Bayesian randomized clinical trial needs to make decisions about power and
sample size within the context of hypothesized treatment effects.  Through
simulation, the simple_sim() function will estimate power and other user
specified clinical trial characteristics at user specified sample sizes
given user defined scenarios about treatment effect,control group
characteristics, and outcome.  If the clinical trial researcher has access
to historical control data, then the researcher can design a two-arm
Bayesian randomized clinical trial that incorporates the historical data.
In such a case, the researcher needs to work through the potential
consequences of historical and randomized control differences on trial
characteristics, in addition to working through issues regarding power in
the context of sample size, treatment effect size, and outcome.  If a
researcher designs a clinical trial that will incorporate historical
control data, the researcher needs the randomized controls to be from the
same population as the historical controls.  What if this is not the case
when the designed trial is implemented?  During the design phase, the
researcher needs to investigate the negative effects of possible
historic/randomized control differences on power, type one error, and
other trial characteristics.  Using this information, the researcher
should design the trial to mitigate these negative effects.  Through
simulation, the historic_sim() function will estimate power and other user
specified clinical trial characteristics at user specified sample sizes
given user defined scenarios about historical and randomized control
differences as well as treatment effects and outcomes.  The results from
historic_sim() and simple_sim() can be printed with print_table() and
graphed with plot_table() methods.  Outcomes considered are Gaussian,
Poisson, Bernoulli, Lognormal, Weibull, and Piecewise Exponential.  The
methods are described in Eggleston et al. (2021)
<doi:10.18637/jss.v100.i21>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
