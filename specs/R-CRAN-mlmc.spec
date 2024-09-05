%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlmc
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Level Monte Carlo

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 

%description
An implementation of MLMC (Multi-Level Monte Carlo), Giles (2008)
<doi:10.1287/opre.1070.0496>, Heinrich (1998)
<doi:10.1006/jcom.1998.0471>, for R.  This package builds on the original
'Matlab' and 'C++' implementations by Mike Giles to provide a full MLMC
driver and example level samplers. Multi-core parallel sampling of levels
is provided built-in.

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
