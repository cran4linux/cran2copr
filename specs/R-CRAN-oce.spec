%global packname  oce
%global packver   1.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Analysis of Oceanographic Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-gsw 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-gsw 
Requires:         R-CRAN-Rcpp 

%description
Supports the analysis of Oceanographic data, including 'ADCP'
measurements, measurements made with 'argo' floats, 'CTD' measurements,
sectional data, sea-level time series, coastline and topographic data,
etc. Provides specialized functions for calculating seawater properties
such as potential temperature in either the 'UNESCO' or 'TEOS-10' equation
of state. Produces graphical displays that conform to the conventions of
the Oceanographic literature. This package is discussed extensively in Dan
Kelley's book Oceanographic Analysis with R, published in 2018 by
'Springer-Verlag' with ISBN 978-1-4939-8842-6.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/po
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
