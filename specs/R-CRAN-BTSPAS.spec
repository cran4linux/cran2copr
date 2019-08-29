%global packname  BTSPAS
%global packver   2014.0901
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2014.0901
Release:          1%{?dist}
Summary:          Bayesian Time-Strat. Population Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-R2OpenBUGS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-coda 
Requires:         R-splines 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-R2OpenBUGS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plyr 

%description
BTSPAS provides advanced Bayesian methods to estimate abundance and
run-timing from temporally-stratified Petersen mark-recapture experiments.
Methods include hierarchical modelling of the capture probabilities and
spline smoothing of the daily run size. This version uses JAGS to sample
from the posterior distribution.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
