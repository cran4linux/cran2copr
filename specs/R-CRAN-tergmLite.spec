%global __brp_check_rpaths %{nil}
%global packname  tergmLite
%global packver   2.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.5
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Simulation of Simple Temporal Exponential Random Graph Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-statnet.common >= 4.4.0
BuildRequires:    R-CRAN-ergm >= 4.0
BuildRequires:    R-CRAN-tergm >= 4.0
BuildRequires:    R-CRAN-network >= 1.17.0
BuildRequires:    R-CRAN-networkDynamic >= 0.11.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-methods 
Requires:         R-CRAN-statnet.common >= 4.4.0
Requires:         R-CRAN-ergm >= 4.0
Requires:         R-CRAN-tergm >= 4.0
Requires:         R-CRAN-network >= 1.17.0
Requires:         R-CRAN-networkDynamic >= 0.11.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-tibble 
Requires:         R-methods 

%description
Provides functions for the computationally efficient simulation of dynamic
networks estimated with the statistical framework of temporal exponential
random graph models, implemented in the 'tergm' package.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
