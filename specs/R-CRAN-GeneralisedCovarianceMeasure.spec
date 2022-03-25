%global __brp_check_rpaths %{nil}
%global packname  GeneralisedCovarianceMeasure
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Test for Conditional Independence Based on the Generalized Covariance Measure (GCM)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CVST 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-CVST 
Requires:         R-graphics 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-mgcv 
Requires:         R-stats 
Requires:         R-CRAN-xgboost 

%description
A statistical hypothesis test for conditional independence. It performs
nonlinear regressions on the conditioning variable and then tests for a
vanishing covariance between the resulting residuals. It can be applied to
both univariate random variables and multivariate random vectors. Details
of the method can be found in Rajen D. Shah and Jonas Peters: The Hardness
of Conditional Independence Testing and the Generalised Covariance
Measure, Annals of Statistics 48(3), 1514--1538, 2020.

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
