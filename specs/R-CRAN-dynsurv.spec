%global packname  dynsurv
%global packver   0.3-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}
Summary:          Dynamic Models for Survival Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-BH >= 1.54.0.2
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-stats 
BuildRequires:    R-survival 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape 
Requires:         R-stats 
Requires:         R-survival 
Requires:         R-utils 

%description
Functions fitting time-varying coefficient models for interval censored
and right censored survival data. Three major approaches are implemented:
1) Bayesian Cox model with time-independent, time-varying or dynamic
coefficients for right censored and interval censored data; 2) Spline
based time-varying coefficient Cox model for right censored data; 3)
Transformation model with time-varying coefficients for right censored
data using estimating equations.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
