%global packname  RHMS
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          2%{?dist}
Summary:          Hydrologic Modelling System for R Users

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-network 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggplot2 

%description
Hydrologic modelling system is an object oriented tool which enables R
users to simulate and analyze hydrologic events. The package proposes
functions and methods for construction, simulation, visualization, and
calibration of hydrologic systems.

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
%{rlibdir}/%{packname}/INDEX
