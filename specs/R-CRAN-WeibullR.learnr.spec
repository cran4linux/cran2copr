%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WeibullR.learnr
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          An Interactive Introduction to Life Data Analysis

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-learnr 
BuildRequires:    R-CRAN-ReliaGrowR 
BuildRequires:    R-CRAN-WeibullR 
BuildRequires:    R-CRAN-WeibullR.ALT 
Requires:         R-CRAN-learnr 
Requires:         R-CRAN-ReliaGrowR 
Requires:         R-CRAN-WeibullR 
Requires:         R-CRAN-WeibullR.ALT 

%description
An interactive introduction to Life Data Analysis that depends on
'WeibullR' by David Silkworth and Jurgen Symynck (2022)
<https://CRAN.R-project.org/package=WeibullR>, a R package for Weibull
Analysis, and 'learnr' by Garrick Aden-Buie et al. (2023)
<https://CRAN.R-project.org/package=learnr>, a framework for building
interactive learning modules in R.

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
