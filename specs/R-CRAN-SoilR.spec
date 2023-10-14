%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SoilR
%global packver   1.2.107
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.107
Release:          1%{?dist}%{?buildtag}
Summary:          Models of Soil Organic Matter Decomposition

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-sets 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-deSolve 
Requires:         R-methods 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-assertthat 
Requires:         R-parallel 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-sets 
Requires:         R-CRAN-purrr 

%description
Functions for modeling Soil Organic Matter decomposition in terrestrial
ecosystems with linear and nonlinear systems of differential equations.
The package implements models according to the compartmental system
representation described in Sierra and others (2012)
<doi:10.5194/gmd-5-1045-2012> and Sierra and others (2014)
<doi:10.5194/gmd-7-1919-2014>.

%prep
%setup -q -c -n %{packname}
find %{packname} -type f -exec sed -Ei 's@#!( )*(/usr)*/bin/(env )*python@#!/usr/bin/python3@g' {} \;
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
