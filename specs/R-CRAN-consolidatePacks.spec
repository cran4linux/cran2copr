%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  consolidatePacks
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Eliminate '@import' by Incorporating Dependencies Directly into the Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vprint 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-devtools 
Requires:         R-CRAN-vprint 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-devtools 

%description
The purpose of this package is to remove the '@import' dependence of an
external package by consolidating the functions into your package. This
may be necessary when the '@import' package is decommissioned by CRAN, and
you do not want your dependent package to also be decommissioned. The
functions in this package recursively retrieve dependencies in the
external package. It also performs the other needed bookkeeping, such as
retrieving .Rd files in the man subdirectory.

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
