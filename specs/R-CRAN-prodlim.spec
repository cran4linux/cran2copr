%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  prodlim
%global packver   2023.03.31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2023.03.31
Release:          1%{?dist}%{?buildtag}
Summary:          Product-Limit Estimation for Censored Event History Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-diagram 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-lava 
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-diagram 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-lava 

%description
Fast and user friendly implementation of nonparametric estimators for
censored event history (survival) analysis. Kaplan-Meier and
Aalen-Johansen method.

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
