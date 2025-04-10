%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OptHoldoutSize
%global packver   0.1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Optimal Size for a Holdout Set for Updating a Predictive Score

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-mle.tools 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-mle.tools 

%description
Predictive scores must be updated with care, because actions taken on the
basis of existing risk scores causes bias in risk estimates from the
updated score. A holdout set is a straightforward way to manage this
problem: a proportion of the population is 'held-out' from computation of
the previous risk score. This package provides tools to estimate a size
for this holdout set and associated errors. Comprehensive vignettes are
included. Please see: Haidar-Wehbe S, Emerson SR, Aslett LJM, Liley J
(2022) <doi:10.48550/arXiv.2202.06374> (to appear in Annals of Applied
Statistics) for details of methods.

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
