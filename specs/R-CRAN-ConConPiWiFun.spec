%global packname  ConConPiWiFun
%global packver   0.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6
Release:          3%{?dist}%{?buildtag}
Summary:          Optimisation with Continuous Convex Piecewise (Linear andQuadratic) Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.10.3
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Rcpp >= 0.10.3
Requires:         R-methods 
Requires:         R-graphics 

%description
Continuous convex piecewise linear (ccpl) resp. quadratic (ccpq) functions
can be implemented with sorted breakpoints and slopes. This includes
functions that are ccpl (resp. ccpq) on a convex set (i.e. an interval or
a point) and infinite out of the domain. These functions can be very
useful for a large class of optimisation problems. Efficient manipulation
(such as log(N) insertion) of such data structure is obtained with map
standard template library of C++ (that hides balanced trees). This package
is a wrapper on such a class based on Rcpp modules.

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
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
