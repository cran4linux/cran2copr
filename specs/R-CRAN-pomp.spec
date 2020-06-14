%global packname  pomp
%global packver   2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8
Release:          2%{?dist}
Summary:          Statistical Inference for Partially Observed Markov Processes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
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

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/GPL
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
