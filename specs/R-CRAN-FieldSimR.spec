%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FieldSimR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation of Plot-Level Data in Plant Breeding Field Trials

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-interp 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-mbend 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-interp 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-mbend 

%description
Simulates plot-level data in plant breeding field trials for multiple
traits in multiple environments. Its core function simulates spatially
correlated plot-level errors across correlated traits using bivariate
interpolation or a two-dimensional autoregressive process of order one
(AR1:AR1). 'FieldSimR' then combines this spatial error with random
measurement error at a user-defined ratio. The simulated plot-level errors
can be combined with genetic values (e.g. true, simulated or predicted) to
generate plot-level phenotypes. 'FieldSimR' provides wrapper functions to
simulate the genetic values for multiple traits in multiple environments
using the 'R' package 'AlphaSimR'.

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
