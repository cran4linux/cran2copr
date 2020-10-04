%global packname  pomp
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          2%{?dist}%{?buildtag}
Summary:          Statistical Inference for Partially Observed Markov Processes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plyr 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plyr 

%description
Tools for data analysis with partially observed Markov process (POMP)
models (also known as stochastic dynamical systems, hidden Markov models,
and nonlinear, non-Gaussian, state-space models).  The package provides
facilities for implementing POMP models, simulating them, and fitting them
to time series data by a variety of frequentist and Bayesian methods.  It
is also a versatile platform for implementation of inference methods for
general POMP models.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
