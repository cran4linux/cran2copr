%global packname  DRAFT
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Disease Rapid Analysis and Forecasting Tool

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-lubridate >= 1.7.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape 
Requires:         R-CRAN-lubridate >= 1.7.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape 

%description
Fits epidemic data to and generates stochastic profiles of a model with
constant or time-dependent behavior modification parameters. Two
parameters, p and q, describe the effect of reduced contact rate of
susceptible and infectious populations, respectively as described by
Brauer (2011, ISSN:1471-2458). In the absence of behavior modification,
p=q=1, we recover the familiar compartmental
Susceptible-Infectious-Recovered (SIR) equations. 'DRAFT' supports both
constant values for p and q and a time-dependent form which smoothly
changes p and q from their initial, pre-epidemic value of 1.0 to the user
chosen values that are between 0 and 1. The start and transient time of
behavior change are set by the user. 'DRAFT' can be used to compare
forecasts of epidemic incidence with and without behavior modification.
Additional parameters and data fitting methods are explained in Ben-Nun et
al (2019) <doi:10.1371/journal.pcbi.1007013>.

%prep
%setup -q -c -n %{packname}


%build

%install
test $(gcc -dumpversion) -ge 10 && export PKG_FFLAGS=-fallow-argument-mismatch
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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
