%global packname  coarseDataTools
%global packver   0.6-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.5
Release:          3%{?dist}
Summary:          Analysis of Coarsely Observed Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-MCMCpack 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 

%description
Functions to analyze coarse data. Specifically, it contains functions to
(1) fit parametric accelerated failure time models to interval-censored
survival time data, and (2) estimate the case-fatality ratio in scenarios
with under-reporting. This package's development was motivated by
applications to infectious disease: in particular, problems with
estimating the incubation period and the case fatality ratio of a given
disease.  Sample data files are included in the package. See Reich et al.
(2009) <doi:10.1002/sim.3659>, Reich et al. (2012)
<doi:10.1111/j.1541-0420.2011.01709.x>, and Lessler et al. (2009)
<doi:10.1016/S1473-3099(09)70069-6>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
