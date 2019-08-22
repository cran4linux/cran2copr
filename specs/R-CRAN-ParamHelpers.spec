%global packname  ParamHelpers
%global packver   1.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.12
Release:          1%{?dist}
Summary:          Helpers for Parameters in Black-Box Optimization, Tuning andMachine Learning

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-checkmate >= 1.8.2
BuildRequires:    R-CRAN-BBmisc >= 1.10
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-methods 
Requires:         R-CRAN-checkmate >= 1.8.2
Requires:         R-CRAN-BBmisc >= 1.10
Requires:         R-CRAN-backports 
Requires:         R-CRAN-fastmatch 
Requires:         R-methods 

%description
Functions for parameter descriptions and operations in black-box
optimization, tuning and machine learning. Parameters can be described
(type, constraints, defaults, etc.), combined to parameter sets and can in
general be programmed on. A useful OptPath object (archive) to log
function evaluations is also provided.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
