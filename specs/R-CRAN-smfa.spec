%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smfa
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Stochastic Metafrontier Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sfaR 
BuildRequires:    R-stats 
Requires:         R-CRAN-sfaR 
Requires:         R-stats 

%description
Implements stochastic metafrontier analysis for productivity and
performance benchmarking across firms operating under different
technologies. Contains routines for the deterministic metafrontier
envelope of O'Donnell et al. (2008) <doi:10.1007/s00181-007-0119-4> via
linear and quadratic programming, and the stochastic metafrontier of Huang
et al. (2014) <doi:10.1007/s11123-014-0402-2>. Also supports latent class
stochastic metafrontier analysis and sample selection correction
stochastic metafrontier models. Depends on the 'sfaR' package by Dakpo et
al. (2023) <https://CRAN.R-project.org/package=sfaR>.

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
