%global packname  BTSPAS
%global packver   2020.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2020.1.1
Release:          3%{?dist}
Summary:          Bayesian Time-Stratified Population Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggforce 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-R2jags 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides advanced Bayesian methods to estimate abundance and run-timing
from temporally-stratified Petersen mark-recapture experiments. Methods
include hierarchical modelling of the capture probabilities and spline
smoothing of the daily run size.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
