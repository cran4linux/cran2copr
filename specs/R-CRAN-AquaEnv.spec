%global packname  AquaEnv
%global packver   1.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}
Summary:          Integrated Development Toolbox for Aquatic Chemical ModelGeneration

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-minpack.lm 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Toolbox for the experimental aquatic chemist, focused on acidification and
CO2 air-water exchange. It contains all elements to model the pH, the
related CO2 air-water exchange, and aquatic acid-base chemistry for an
arbitrary marine, estuarine or freshwater system. It contains a suite of
tools for sensitivity analysis, visualisation, modelling of chemical
batches, and can be used to build dynamic models of aquatic systems. As
from version 1.0-4, it also contains functions to calculate the buffer
factors.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
