%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CensRegSMSN
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Censored Linear Regression Models under Heavy‑tailed Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-ggplot2 

%description
Functions for fitting univariate linear regression models under Scale
Mixtures of Skew-Normal (SMSN) distributions, considering left, right or
interval censoring and missing responses. Estimation is performed via an
EM-type algorithm. Includes selection criteria, sample generation and
envelope. For details, see Gil, Y.A., Garay, A.M., and Lachos, V.H. (2025)
<doi:10.1007/s10260-025-00797-x>.

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
