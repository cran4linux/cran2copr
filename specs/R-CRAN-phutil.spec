%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phutil
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Persistence Homology Utilities

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 

%description
A low-level package for hosting persistence data. It is part of the
'TDAverse' suite of packages, which is designed to provide a collection of
packages for enabling machine learning and data science tasks using
persistent homology. Implements a class for hosting persistence data, a
number of coercers from and to already existing and used data structures
from other packages and functions to compute distances between persistence
diagrams. A formal definition and study of bottleneck and Wasserstein
distances can be found in Bubenik, Scott and Stanley (2023)
<doi:10.1007/s41468-022-00103-8>. Their implementation in 'phutil' relies
on the 'C++' Hera library developed by Kerber, Morozov and Nigmetov (2017)
<doi:10.1145/3064175>.

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
