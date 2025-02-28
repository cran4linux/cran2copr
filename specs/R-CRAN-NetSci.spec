%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NetSci
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculates Basic Network Measures Commonly Used in Network Medicine

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-wTO 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-binr 
BuildRequires:    R-CRAN-cubature 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-wTO 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Rfast 
Requires:         R-utils 
Requires:         R-CRAN-binr 
Requires:         R-CRAN-cubature 

%description
Calculates network measures commonly used in Network Medicine. Measures
such as the Largest Connected Component, the Relative Largest Connected
Component, Proximity and Separation are calculated along with their
statistical significance. Significance can be computed both using a
degree-preserving randomization and non-degree preserving.

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
