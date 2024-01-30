%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phylobase
%global packver   0.8.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.12
Release:          1%{?dist}%{?buildtag}
Summary:          Base Package for Phylogenetic Structures and Comparative Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ape >= 3.0
BuildRequires:    R-CRAN-rncl >= 0.6.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RNeXML 
Requires:         R-CRAN-ape >= 3.0
Requires:         R-CRAN-rncl >= 0.6.0
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-ade4 
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-RNeXML 

%description
Provides a base S4 class for comparative methods, incorporating one or
more trees and trait data.

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
