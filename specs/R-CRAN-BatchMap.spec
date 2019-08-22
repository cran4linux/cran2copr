%global packname  BatchMap
%global packver   1.0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2.0
Release:          1%{?dist}
Summary:          Software for the Creation of High Density Linkage Maps inOutcrossing Species

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-parallel >= 3.2.3
BuildRequires:    R-CRAN-reshape2 >= 1.4.1
BuildRequires:    R-CRAN-ggplot2 >= 1.0.1
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.700
BuildRequires:    R-CRAN-Rcpp >= 0.10.5
BuildRequires:    R-methods 
Requires:         R-parallel >= 3.2.3
Requires:         R-CRAN-reshape2 >= 1.4.1
Requires:         R-CRAN-ggplot2 >= 1.0.1
Requires:         R-methods 

%description
Algorithms that build on the 'OneMap' package to create linkage maps from
high density data in outcrossing species in reasonable time frames.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/example
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
