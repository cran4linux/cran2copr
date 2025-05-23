%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Matching
%global packver   4.10-15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.10.15
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate and Propensity Score Matching with Balance Optimization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.0
Requires:         R-core >= 2.6.0
BuildRequires:    R-CRAN-MASS >= 7.2.1
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS >= 7.2.1
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Provides functions for multivariate and propensity score matching and for
finding optimal balance based on a genetic search algorithm. A variety of
univariate and multivariate metrics to determine if balance has been
obtained are also provided. For details, see the paper by Jasjeet Sekhon
(2007, <doi:10.18637/jss.v042.i07>).

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
