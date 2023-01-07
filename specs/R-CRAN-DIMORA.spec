%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DIMORA
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Diffusion Models R Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-deSolve 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-deSolve 

%description
The implemented methods are: Standard Bass model, Generalized Bass model
(with rectangular shock, exponential shock, and mixed shock. You can
choose to add from 1 to 3 shocks), Guseo-Guidolin model and Variable
Potential Market model, and UCRCD model. The Bass model consists of a
simple differential equation that describes the process of how new
products get adopted in a population, the Generalized Bass model is a
generalization of the Bass model in which there is a "carrier" function
x(t) that allows to change the speed of time sliding. In some real
processes the reachable potential of the resource available in a temporal
instant may appear to be not constant over time, because of this we use
Variable Potential Market model, in which the Guseo-Guidolin has a
particular specification for the market function. The UCRCD model
(Unbalanced Competition and Regime Change Diachronic) is a diffusion model
used to capture the dynamics of the competitive or collaborative
transition.

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
