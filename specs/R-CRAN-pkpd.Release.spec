%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pkpd.Release
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Model Fitting and Simulation for Drug Release Kinetics and PK/PD

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-scales 

%description
Provides a comprehensive framework for model fitting and simulation of
drug release kinetics, pharmacokinetics (PK), and pharmacodynamics (PD).
The package implements widely used mechanistic and empirical models for in
vitro drug release, including zero-order, first-order, Higuchi,
Korsmeyer-Peppas, Hixson-Crowell, and Weibull models. Pharmacokinetic
functionality includes linear and nonlinear functions for one- and
two-compartment models for intravenous bolus and oral administration,
Michaelis-Menten kinetics, and non-compartmental analysis (NCA).
Pharmacodynamic and dose-response modeling is supported through Emax-based
models, including stimulatory (sigmoid Emax) and inhibitory (sigmoid Imax)
Hill models, four- and five-parameter logistic models, as well as median
toxic dose (TD50) and lethal dose (LD50) models. The package is intended
to support parameter estimation, simulation, and model comparison in
pharmaceutical research, drug development, and pharmacometrics education.
For more details, see Gabrielsson & Weiner (2000) <ISBN:9186274929>,
Holford & Sheiner (1981) <doi:10.2165/00003088-198106060-00002>, and
Manlapaz (2025) <doi:10.32614/CRAN.package.adsoRptionCMF>.

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
