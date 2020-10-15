%global packname  ergm
%global packver   3.11.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.11.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fit, Simulate and Diagnose Exponential-Family Models for Networks

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    openmpi-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-MASS >= 7.3.51.4
BuildRequires:    R-CRAN-lpSolve >= 5.6.13
BuildRequires:    R-CRAN-statnet.common >= 4.4.0
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-Matrix >= 1.2.17
BuildRequires:    R-CRAN-network >= 1.15
BuildRequires:    R-CRAN-robustbase >= 0.93.5
BuildRequires:    R-CRAN-rlang >= 0.3.4
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-coda >= 0.19.2
BuildRequires:    R-CRAN-trust >= 0.1.7
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rle 
Requires:         R-CRAN-MASS >= 7.3.51.4
Requires:         R-CRAN-lpSolve >= 5.6.13
Requires:         R-CRAN-statnet.common >= 4.4.0
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-Matrix >= 1.2.17
Requires:         R-CRAN-network >= 1.15
Requires:         R-CRAN-robustbase >= 0.93.5
Requires:         R-CRAN-rlang >= 0.3.4
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-coda >= 0.19.2
Requires:         R-CRAN-trust >= 0.1.7
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-rle 

%description
An integrated set of tools to analyze and simulate networks based on
exponential-family random graph models (ERGMs). 'ergm' is a part of the
Statnet suite of packages for network analysis.

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
