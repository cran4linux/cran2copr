%global packname  simsurv
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Survival Data

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-stats 

%description
Simulate survival times from standard parametric survival distributions
(exponential, Weibull, Gompertz), 2-component mixture distributions, or a
user-defined hazard, log hazard, cumulative hazard, or log cumulative
hazard function. Baseline covariates can be included under a proportional
hazards assumption. Time dependent effects (i.e. non-proportional hazards)
can be included by interacting covariates with linear time or a
user-defined function of time. Clustered event times are also
accommodated. The 2-component mixture distributions can allow for a
variety of flexible baseline hazard functions reflecting those seen in
practice. If the user wishes to provide a user-defined hazard or log
hazard function then this is possible, and the resulting cumulative hazard
function does not need to have a closed-form solution. For details see the
supporting paper <doi:10.18637/jss.v097.i03>. Note that this package is
modelled on the 'survsim' package available in the 'Stata' software (see
Crowther and Lambert (2012)
<https://www.stata-journal.com/sjpdf.html?articlenum=st0275> or Crowther
and Lambert (2013) <doi:10.1002/sim.5823>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
