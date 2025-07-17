%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adapt3
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Dynamics and Community Matrix Model Projections

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-lefko3 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-lefko3 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-grDevices 

%description
Runs projections of groups of matrix projection models (MPMs), allowing
density dependence mechanisms to work across MPMs. This package was
developed to run both adaptive dynamics simulations such as pairwise and
multiple invasibility analyses, and community projections in which species
are represented by MPMs. All forms of MPMs are allowed, including integral
projection models (IPMs). Also includes individual-based modeling (IBM)
versions of these.

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
