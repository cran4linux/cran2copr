%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hmmm
%global packver   1.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Multinomial Marginal Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-methods 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-nleqslv 
Requires:         R-methods 

%description
Functions for specifying and fitting marginal models for contingency
tables proposed by Bergsma and Rudas (2002) <doi:10.1214/aos/1015362188>
here called hierarchical multinomial marginal models (hmmm) and their
extensions presented by Bartolucci, Colombi and Forcina (2007)
<https://www.jstor.org/stable/24307737>; multinomial Poisson homogeneous
(mph) models and homogeneous linear predictor (hlp) models for contingency
tables proposed by Lang (2004) <doi:10.1214/aos/1079120140> and Lang
(2005) <doi:10.1198/016214504000001042>. Inequality constraints on the
parameters are allowed and can be tested.

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
