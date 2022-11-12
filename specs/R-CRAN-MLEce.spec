%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MLEce
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Inference for Asymptotic Efficient Closed-Form Estimators

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-sirt 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-sirt 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-mvtnorm 

%description
Estimate asymptotic efficient closed-form estimators and provide goodness
of fit, estimates, plot and etc. Yue, S. (2001) <doi:10.1002/hyp.259>.
Mosimann, James E. (1962) <doi:10.1093/biomet/49.1-2.65>.

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
