%global __brp_check_rpaths %{nil}
%global packname  RestRserve
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Framework for Building HTTP API

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-R6 >= 2.4.0
BuildRequires:    R-CRAN-checkmate >= 1.9.4
BuildRequires:    R-CRAN-Rserve >= 1.7.3
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-mime >= 0.7
BuildRequires:    R-CRAN-uuid >= 0.1.2
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-CRAN-R6 >= 2.4.0
Requires:         R-CRAN-checkmate >= 1.9.4
Requires:         R-CRAN-Rserve >= 1.7.3
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-mime >= 0.7
Requires:         R-CRAN-uuid >= 0.1.2
Requires:         R-methods 
Requires:         R-parallel 

%description
Allows to easily create high-performance full featured HTTP APIs from R
functions. Provides high-level classes such as 'Request', 'Response',
'Application', 'Middleware' in order to streamline server side application
development. Out of the box allows to serve requests using 'Rserve'
package, but flexible enough to integrate with other HTTP servers such as
'httpuv'.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
