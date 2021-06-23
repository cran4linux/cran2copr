%global __brp_check_rpaths %{nil}
%global packname  tergm
%global packver   3.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fit, Simulate and Diagnose Models for Network Evolution Based on Exponential-Family Random Graph Models

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-MASS >= 7.3.51.4
BuildRequires:    R-CRAN-statnet.common >= 4.4.0
BuildRequires:    R-CRAN-ergm >= 3.11.0
BuildRequires:    R-CRAN-nlme >= 3.1.139
BuildRequires:    R-CRAN-network >= 1.15
BuildRequires:    R-CRAN-robustbase >= 0.93.5
BuildRequires:    R-CRAN-coda >= 0.19.2
BuildRequires:    R-CRAN-networkDynamic >= 0.10.0
Requires:         R-CRAN-MASS >= 7.3.51.4
Requires:         R-CRAN-statnet.common >= 4.4.0
Requires:         R-CRAN-ergm >= 3.11.0
Requires:         R-CRAN-nlme >= 3.1.139
Requires:         R-CRAN-network >= 1.15
Requires:         R-CRAN-robustbase >= 0.93.5
Requires:         R-CRAN-coda >= 0.19.2
Requires:         R-CRAN-networkDynamic >= 0.10.0

%description
An integrated set of extensions to the 'ergm' package to analyze and
simulate network evolution based on exponential-family random graph models
(ERGM). 'tergm' is a part of the 'statnet' suite of packages for network
analysis.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
