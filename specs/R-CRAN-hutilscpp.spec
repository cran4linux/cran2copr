%global packname  hutilscpp
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}
Summary:          Miscellaneous Functions in C++

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-hutils 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-hutils 
Requires:         R-utils 

%description
Provides utility functions that are simply, frequently used, but may
require higher performance that what can be obtained from base R.
Incidentally provides support for 'reverse geocoding', such as matching a
point with its nearest neighbour in another array. Used as a complement to
package 'hutils' by sacrificing compilation or installation time for
higher running speeds. The name is a portmanteau of the author and 'Rcpp'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
